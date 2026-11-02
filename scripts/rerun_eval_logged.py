"""Re-run the GraphRAG evaluation with current models, full logging and a spending cap.

    python scripts/rerun_eval_logged.py --check                      # API access + model lists (no cost)
    python scripts/rerun_eval_logged.py --check-references           # reference answers vs. current cell data
    python scripts/rerun_eval_logged.py --limit 10                   # pilot: first 10 questions per configuration
    python scripts/rerun_eval_logged.py                              # full run, resumes where it stopped
    python scripts/rerun_eval_logged.py --rerun-changed-retrieval    # after a correction of the graph code or the data

Differences to scripts/run_eval.py (the recorded 2026 run):
* every call is logged: generated query, graph result, answer, grades, token usage incl. reasoning, stop reason, cost;
* one judge model grades all configurations (instead of each model grading itself); a run resumed with another
  --judge or --grader-prompt grades the logged answers again and keeps the earlier grading calls as
  superseded_grades;
* all answering models run at their low reasoning setting (effort / reasoning_effort / thinking_level);
* negative controls (reference "Not available"): an answer that the judge recognises as stating that the information
  is not available counts as correct, as in the recorded runs; the judge compares answers literally and would otherwise
  grade "not recorded" against "Not available" as wrong (records carry correct_by_rule; --rescore applies it to
  logged records without new calls);
* every answer that is not correct is assigned to the step where it went wrong:
  query_failed      - no runnable query (parse error, unknown function, SPARQL error)
  nothing_retrieved - the query ran but returned no value for the question
  other_data        - the query returned data, but not the reference value
  answer_step       - the reference value was retrieved, but the final answer is not correct
* per-provider spending caps; the run stops cleanly before a cap is reached and can be resumed;
* corrections: a logged answer whose reference answer has changed in the question set is graded again (the earlier
  reference is kept in earlier_references); with --rerun-changed-retrieval, every RAG question whose logged query
  returns other data from the current knowledge graph is posed again (the earlier records are kept in
  superseded_records.jsonl).

The question set is evaluation/qa_dataset_v2.csv: evaluation/qa_dataset.csv with the reference answers corrected that
no longer matched the cell data (evaluation/qa_dataset_v2_changes.csv). The prompts and the graph code are the
published ones (batterygraph/).
API keys are read from .env (OPENAI_API_KEY, ANTHROPIC_API_KEY, GEMINI_API_KEY); they are never printed.
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import csv
import datetime
import hashlib
import json
import os
import re
import sys
import threading
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from batterygraph import prompts  # noqa: E402
from batterygraph.graph import NUMERIC_PROPERTIES, BatteryGraph  # noqa: E402
from batterygraph.rag import execute_query  # noqa: E402

try:
    from dotenv import load_dotenv
    load_dotenv(ROOT / ".env", override=True)  # .env wins over keys already set in the shell
except ImportError:
    pass

OUT = ROOT / "evaluation" / "results_rerun_2026-10"

# USD per 1M tokens: (input, cached input, output). Claude: Anthropic list prices. Gemini and OpenAI: list prices
# plus a 25 % safety margin, because they come from price lists that could not all be verified; the spending cap
# therefore triggers early rather than late.
PRICES = {
    "claude-sonnet-5-5": (2.00, 0.20, 10.00),
    "claude-haiku-5-5": (0.10, 0.01, 0.50),
    "claude-opus-5-5": (4.00, 0.40, 20.00),
    "gemini-3.8-flash": (0.94, 0.94, 4.69),
    "openai-default": (2.50, 0.25, 12.50),
}


# Grading prompts: the published one (answer and solution only) and one that also shows the question and names the
# equivalences a judge should accept (choose with --grader-prompt; compared in scripts/compare_judges.py).
GRADER_WITH_QUESTION = (
    "You grade an answer to a question about battery cells against the reference solution. Reply with 1 if the "
    "answer is correct and 0 if it is not, and nothing else.\n"
    "The answer is correct if it gives the same information as the solution, even in other words:\n"
    "- numbers in other units or rounded, if they agree with the solution at the solution's precision "
    "(e.g. 21.2 mm for 0.021 m, 4.4 Ah for 4400 mAh);\n"
    "- class or material names in another common form (e.g. Prismatic for PrismaticCase, NMC for "
    "LithiumNickelManganeseCobaltOxide);\n"
    "- for a question which of two cells has the higher value: the right cell, with or without the values;\n"
    "- for a yes/no question: the right yes or no, with or without the values;\n"
    "- if the solution is \"Not available\": any answer saying that the information is not available, not recorded "
    "or does not apply.\n"
    "The answer is not correct if a value, name or cell differs from the solution, if a part of the solution is "
    "missing, if it gives a value where the solution is \"Not available\", or if it says the information is not "
    "available where the solution gives it."
)
GRADER_PROMPTS = {  # name -> (question, solution, answer) -> (user prompt, system prompt)
    "published": lambda q, s, a: (f"Answer: {a}\n\nSolution: {s}", prompts.GRADER_SYSTEM),
    "with_question": lambda q, s, a: (f"Question: {q}\nSolution: {s}\nAnswer: {a}", GRADER_WITH_QUESTION),
}


def provider(model: str) -> str:
    if model.startswith("stub"):
        return "stub"
    if model.startswith("claude"):
        return "anthropic"
    if model.startswith("gemini"):
        return "gemini"
    return "openai"


def price(model: str):
    return PRICES.get(model, PRICES["openai-default"] if provider(model) == "openai" else (5.0, 5.0, 25.0))


# --------------------------------------------------------------------------------------------- spending guard
class Budget:
    """Running cost per provider; refuses new work once the cap minus a reserve is reached."""

    def __init__(self, caps: dict, path: Path):
        self.caps, self.path, self.lock = caps, path, threading.Lock()
        self.spent = json.loads(path.read_text()) if path.exists() else {}

    def add(self, prov: str, usd: float):
        with self.lock:
            self.spent[prov] = self.spent.get(prov, 0.0) + usd
            self.path.write_text(json.dumps(self.spent, indent=1))

    def allows(self, prov: str, reserve: float) -> bool:
        if prov == "stub":
            return True
        with self.lock:
            return self.spent.get(prov, 0.0) + reserve <= self.caps.get(prov, 0.0)


# ------------------------------------------------------------------------------------------------ model calls
_clients, _client_lock = {}, threading.Lock()


def client(prov: str):
    with _client_lock:
        if prov not in _clients:
            if prov == "anthropic":
                import anthropic
                _clients[prov] = anthropic.Anthropic()
            elif prov == "openai":
                from openai import OpenAI
                _clients[prov] = OpenAI()
            else:
                from google import genai
                _clients[prov] = genai.Client(api_key=os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY"))
        return _clients[prov]


def call(model: str, prompt: str, system: str | None, effort: str, max_tokens: int = 8000, retries: int = 3) -> dict:
    """One model call. Returns text, token usage (input, cached, output incl. reasoning, reasoning), stop reason, cost."""
    prov = provider(model)
    if prov == "stub":  # dry run without API calls: a fixed query, a fixed answer, grade 0
        text = ('query_cell_property(cell_name="INR18650 MJ1", property_name="RatedCapacity", manufacturer="LG Chem")'
                if "Code:" in prompt else "0" if "Solution:" in prompt or "Identifiably" in prompt else "3.5 Ah")
        return {"model": model, "text": text, "input": len(prompt) // 4, "cached": 0, "output": 5, "reasoning": 0,
                "stop": "stub", "cost": 0.0, "seconds": 0}
    for attempt in range(retries):
        try:
            t0 = time.time()
            if prov == "anthropic":
                kw = {"system": system} if system else {}
                r = client(prov).messages.create(model=model, max_tokens=16000, output_config={"effort": effort},
                                                 messages=[{"role": "user", "content": prompt}], **kw)
                text = "".join(getattr(b, "text", "") for b in r.content if getattr(b, "type", "") == "text")
                u = r.usage
                inp, cached, out = u.input_tokens + (u.cache_creation_input_tokens or 0), u.cache_read_input_tokens or 0, u.output_tokens
                reasoning = getattr(getattr(u, "output_tokens_details", None), "thinking_tokens", None)
                stop = r.stop_reason
            elif prov == "openai":
                msgs = ([{"role": "system", "content": system}] if system else []) + [{"role": "user", "content": prompt}]
                r = client(prov).chat.completions.create(model=model, messages=msgs, reasoning_effort=effort,
                                                         max_completion_tokens=max_tokens)
                text = r.choices[0].message.content or ""
                u = r.usage
                cached = (u.prompt_tokens_details.cached_tokens or 0) if u.prompt_tokens_details else 0
                inp, out = u.prompt_tokens - cached, u.completion_tokens
                reasoning = (u.completion_tokens_details.reasoning_tokens or 0) if u.completion_tokens_details else None
                stop = r.choices[0].finish_reason
            else:
                from google.genai import types
                cfg = types.GenerateContentConfig(system_instruction=system, max_output_tokens=max_tokens,
                                                  thinking_config=types.ThinkingConfig(thinking_level=effort.upper()))
                r = client(prov).models.generate_content(model=model, contents=prompt, config=cfg)
                text = r.text or ""
                u = r.usage_metadata
                cached = u.cached_content_token_count or 0
                inp = (u.prompt_token_count or 0) - cached
                reasoning = u.thoughts_token_count or 0
                out = (u.candidates_token_count or 0) + reasoning
                stop = str(r.candidates[0].finish_reason) if r.candidates else None
            pi, pc, po = price(model)
            cost = (inp * pi + cached * pc + out * po) / 1e6
            return {"model": model, "text": text.strip(), "input": inp, "cached": cached, "output": out,
                    "reasoning": reasoning, "stop": stop, "cost": cost, "seconds": round(time.time() - t0, 2)}
        except Exception as exc:  # retried, then recorded as an error
            if attempt == retries - 1:
                return {"model": model, "text": "", "error": f"{type(exc).__name__}: {str(exc)[:300]}", "input": 0,
                        "cached": 0, "output": 0, "reasoning": 0, "stop": "error", "cost": 0.0, "seconds": 0}
            time.sleep(4 * (attempt + 1))


# ------------------------------------------------------------------------------------------- classification
CATS = (("Negative control", None), ("Multi-property summary", r"rated capacity and nominal voltage|operating voltage window"),
        ("Comparison of two cells", r"^Which battery has a higher rated capacity|^Is the .* heavier than"),
        ("Case and chemistry", r"case form factor|cathode active material chemistry"),
        ("Derived value", r"energy capacity in Wh|milliampere-hours"))


def category(q: dict) -> str:
    if q["answer"].strip() == "Not available":
        return "Negative control"
    for name, pat in CATS[1:]:
        if re.search(pat, q["query"]):
            return name
    return "Single-property lookup"


def numbers(text: str):
    return [float(x) for x in re.findall(r"-?\d+(?:\.\d+)?", str(text))]


def retrieval_status(result) -> str:
    """error / empty / data, judged from what the graph returned."""
    rows = result if isinstance(result, list) else [result]
    flat = []
    for r in rows:
        flat.extend(r if isinstance(r, list) else [r])
    if any(isinstance(r, dict) and "error" in r for r in flat) and not any(
            isinstance(r, dict) and r.get("value") is not None for r in flat):
        return "error"
    useful = [r for r in flat if isinstance(r, dict) and not r.get("note") and
              (r.get("value") is not None or r.get("case") or r.get("positive_electrode_active_material") not in (None, "not recorded")
               or (set(r) - {"cell", "id", "manufacturer", "note"}))]
    return "data" if useful else "empty"


def reference_values(ref: str) -> str:
    """The value part of a reference answer; comparisons carry their values in parentheses, after cell names
    that contain digits themselves (e.g. "Saft VL 5U (5 Ah vs 4.15 Ah)")."""
    m = re.search(r"\(([^)]*)\)\s*$", ref)
    return m.group(1) if m else ref


def reference_in_result(ref: str, result) -> bool:
    blob = json.dumps(result, default=str)
    nums = numbers(reference_values(ref))
    if nums:
        got = numbers(blob)
        return all(any(abs(n - g) <= max(1e-6, 1e-3 * abs(n)) or abs(n - 1000 * g) <= 1e-3 * abs(n) for g in got) for n in nums)
    return ref.strip().lower() in blob.lower()


def stage(q: dict, status: str, result, correct: bool) -> str:
    if correct:
        return "correct"
    if q.get("reference_issue"):
        return "reference_mismatch"
    if status == "error":
        return "query_failed"
    if status == "empty":
        return "nothing_retrieved"
    if category(q) == "Derived value" or reference_in_result(q["answer"], result):
        return "answer_step"
    return "other_data"


# -------------------------------------------------------------------------------------------------- the run
def bit(text: str):
    """The judge's 0/1: a bare digit, a digit on the last line, or a leading digit; None if unclear."""
    t = text.strip()
    for match, pat in ((re.fullmatch, r"\**([01])\**\.?"), (re.fullmatch, r"(?s).*\n\s*\**([01])\**\.?"),
                       (re.match, r"\**([01])\**\b(?![.,]\d)")):
        m = match(pat, t)
        if m:
            return int(m.group(1))
    return None


def judged(judge, prompt, system, effort, step, calls):
    """Ask the judge; re-ask up to twice if the reply holds no clear 0/1. Unclear replies count as 0 and are flagged."""
    for _ in range(3):
        g = call(judge, prompt, system, effort, max_tokens=2000)
        v = bit(g["text"])
        calls.append(dict(g, step=step, parsed=v))
        if v is not None:
            return v, False
    return 0, True


def grade(judge: str, question: str, answer: str, solution: str, effort: str, grader: str = "published"):
    calls = []
    v, unclear = judged(judge, *GRADER_PROMPTS[grader](question, solution, answer), effort, "grade", calls)
    correct, idk = v == 1, False
    if not correct:
        if not answer.strip():
            idk = True
        else:
            k, unclear_k = judged(judge, f"{prompts.IDENTIFIABLY_WRONG}\n\nGround Truth Solution: {solution}\nAI Answer: {answer}\n\n"
                                         "Identifiably wrong (1 or 0):", None, effort, "idk_check", calls)
            idk, unclear = k == 1, unclear or unclear_k
    return correct, idk, calls, unclear


def run_one(q, cfg, bg, query_prompt, direct_prompt, judge, effort, grader):
    rec = {"ID": int(q["ID"]), "category": category(q), "question": q["query"], "reference": q["answer"],
           "reference_issue": q.get("reference_issue", ""), "config": cfg["name"], "model": cfg["model"],
           "rag": cfg["rag"], "calls": []}
    if cfg["rag"]:
        gen = call(cfg["model"], query_prompt + "\nQuestion: " + q["query"] + "\nCode:", None, effort)
        rec["calls"].append(dict(gen, step="query_generation"))
        rec["generated_query"] = gen["text"]
        try:
            result = execute_query(bg, gen["text"])
        except Exception as exc:
            result = [{"error": f"execution failed: {exc}"}]
        rec["graph_result"] = json.loads(json.dumps(result, default=str))
        rec["retrieval"] = retrieval_status(result)
        ans = call(cfg["model"], f"Question: {q['query']}\n\nQuery Result: {json.dumps(result, indent=1, default=str)}",
                   prompts.FINAL_ANSWER_SYSTEM, effort)
    else:
        ans = call(cfg["model"], direct_prompt + "\nQuestion: " + q["query"], None, effort)
        result, rec["retrieval"] = None, None
    rec["calls"].append(dict(ans, step="answer"))
    rec["answer"] = ans["text"] if not ans.get("error") else f"ERROR: {ans['error']}"
    return grade_record(rec, q, judge, effort, grader)


def grade_record(rec, q, judge, effort, grader):
    """Grade the logged answer and derive the outcome and the step that failed."""
    _, _, gcalls, unclear = grade(judge, q["query"], rec["answer"], q["answer"], effort, grader)
    rec["calls"].extend(gcalls)
    rec.update(judge=judge, grader_prompt=grader, grade_unclear=unclear)
    score(rec, q)
    rec["cost"] = round(sum(c["cost"] for c in rec["calls"] + rec.get("superseded_grades", [])), 6)
    return rec


def score(rec, q):
    """Outcome from the judge's logged grades, the rule for negative controls, then the step that failed."""
    grades = [c for c in rec["calls"] if c["step"] == "grade"]
    checks = [c for c in rec["calls"] if c["step"] == "idk_check"]
    correct = bool(grades) and grades[-1].get("parsed") == 1
    idk = not correct and (not rec["answer"].strip() or (bool(checks) and checks[-1].get("parsed") == 1))
    rec.pop("correct_by_rule", None)
    if idk and q["answer"].strip() == "Not available":
        correct, idk = True, False
        rec["correct_by_rule"] = "negative control answered with “not available”"
    rec.update(correct=correct, i_dont_know=idk, wrong=not correct and not idk)
    rec["stage"] = (stage(q, rec["retrieval"], rec["graph_result"], rec["correct"]) if rec["rag"]
                    else "correct" if rec["correct"] else "i_dont_know" if rec["i_dont_know"] else "wrong")


def regrade(rec, q, judge, effort, grader):
    """Grade a logged answer again with another judge or prompt; earlier grading calls are kept as superseded_grades."""
    old = [c for c in rec["calls"] if c["step"] in ("grade", "idk_check")]
    rec["superseded_grades"] = rec.get("superseded_grades", []) + old
    rec["calls"] = [c for c in rec["calls"] if c["step"] not in ("grade", "idk_check")]
    if rec["reference"] != q["answer"]:
        rec["earlier_references"] = rec.get("earlier_references", []) + [rec["reference"]]
        rec["reference"] = q["answer"]
    rec["reference_issue"] = q.get("reference_issue", "")
    return grade_record(rec, q, judge, effort, grader)


def replayed(bg, rec):
    """What the logged query of a RAG record returns from the current knowledge graph."""
    try:
        result = execute_query(bg, rec["generated_query"])
    except Exception as exc:
        result = [{"error": f"execution failed: {exc}"}]
    return json.loads(json.dumps(result, default=str))


def judge_of(rec):
    """(judge model, grading prompt) of a logged record."""
    return (rec.get("judge") or next((c["model"] for c in rec["calls"] if c["step"] == "grade"), None),
            rec.get("grader_prompt", "published"))


def read_jsonl(f: Path) -> list:
    """Records of one configuration; a line cut off by an interrupted run is skipped (that question runs again)."""
    recs = []
    if f.exists():
        for line in f.read_text(encoding="utf-8").splitlines():
            try:
                recs.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    return recs


def summarize(configs, out: Path):
    rows = []
    for cfg in configs:
        f = out / f"{cfg['name']}.jsonl"
        if not f.exists():
            continue
        recs = read_jsonl(f)
        n = len(recs)
        c = sum(r["correct"] for r in recs)
        k = sum(r["i_dont_know"] for r in recs)
        stages = {s: sum(r["stage"] == s for r in recs)
                  for s in ("query_failed", "nothing_retrieved", "other_data", "answer_step", "reference_mismatch")}
        rows.append({"config": cfg["name"], "model": cfg["model"], "mode": "GraphRAG" if cfg["rag"] else "LLM only",
                     "questions": n, "correct": c, "incorrect": n - c, "identifiably_wrong": k,
                     "accuracy": round(c / n, 4) if n else None,
                     "hallucination_robustness": round(k / (n - c), 4) if n - c else None,
                     **(stages if cfg["rag"] else {}), "grade_unclear": sum(r.get("grade_unclear", False) for r in recs),
                     "cost_usd": round(sum(r["cost"] for r in recs), 4)})
    keys = sorted({k for r in rows for k in r}, key=lambda k: list(rows[0]).index(k) if k in rows[0] else 99)
    with open(out / "summary.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=keys)
        w.writeheader()
        w.writerows(rows)
    return rows


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--rag", nargs="+", default=["gemini-3.8-flash", "claude-sonnet-5-5"],
                    help="answering models with the knowledge graph (add the OpenAI model ID after --check)")
    ap.add_argument("--no-rag", nargs="*", default=["gemini-3.8-flash"], help="LLM-only baseline models")
    ap.add_argument("--judge", default="claude-sonnet-5-5", help="one judge for all configurations")
    ap.add_argument("--grader-prompt", default="published", choices=list(GRADER_PROMPTS))
    ap.add_argument("--effort", default="low", help="reasoning setting for every model")
    ap.add_argument("--caps", nargs="+", default=["openai=3.0", "gemini=8.0", "anthropic=14.0"], help="USD per provider")
    ap.add_argument("--limit", type=int, help="only the first N questions (pilot)")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--questions", default=str(ROOT / "evaluation" / "qa_dataset_v2.csv"))
    ap.add_argument("--out", default=str(OUT))
    ap.add_argument("--check", action="store_true", help="test API access with one tiny call per model and list models")
    ap.add_argument("--check-references", action="store_true", help="compare reference answers with the current cell data")
    ap.add_argument("--rescore", action="store_true", help="apply the outcome rules to the logged records (no model calls)")
    ap.add_argument("--rerun-changed-retrieval", action="store_true",
                    help="pose every RAG question again whose logged query returns other data from the current graph")
    args = ap.parse_args()

    if args.check:
        return check(args)
    questions = list(csv.DictReader(open(args.questions, encoding="utf-8")))
    bg = BatteryGraph(str(ROOT / "BatteryTypeJson"))
    if args.check_references:
        return check_references(bg, questions)

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    caps = {k: float(v) for k, v in (c.split("=") for c in args.caps)}
    budget = Budget(caps, out / "spent_usd.json")
    configs = [{"name": f"{m}_rag", "model": m, "rag": True} for m in args.rag] + \
              [{"name": f"{m}_llm_only", "model": m, "rag": False} for m in args.no_rag]
    issues = reference_issues(bg, questions)
    for q in questions:
        q["reference_issue"] = issues.get(q["ID"], "")
    (out / "reference_issues.json").write_text(json.dumps(issues, indent=1, ensure_ascii=False))
    by_id = {int(q["ID"]): q for q in questions}
    if args.rescore:
        for cfg in configs:
            f = out / f"{cfg['name']}.jsonl"
            recs = read_jsonl(f)
            for r in recs:
                score(r, by_id[r["ID"]])
            tmp = f.with_suffix(".tmp")
            tmp.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in recs), encoding="utf-8")
            tmp.replace(f)
        for r in summarize(configs, out):
            print(json.dumps(r))
        return
    info_path = out / "run_info.json"
    earlier = json.loads(info_path.read_text()) if info_path.exists() else None
    info_path.write_text(json.dumps({
        "started": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
        "configs": configs, "judge": args.judge, "grader_prompt": args.grader_prompt, "effort": args.effort, "caps_usd": caps, "prices_usd_per_mtok": PRICES,
        "questions": os.path.relpath(Path(args.questions).resolve(), ROOT),  # relative: no local paths in the record
        "questions_sha256": hashlib.sha256(Path(args.questions).read_bytes()).hexdigest(),
        "cells": len(bg.cells),
        "earlier_invocations": (earlier.pop("earlier_invocations", []) + [earlier]) if earlier else []}, indent=1))
    query_prompt = prompts.query_generation_prompt(NUMERIC_PROPERTIES, bg.manufacturers)
    direct_prompt = prompts.DIRECT_ANSWER.format(manufacturers=bg.manufacturers)
    todo = questions[: args.limit] if args.limit else questions
    lock = threading.Lock()
    stopped = []
    for cfg in configs:
        f = out / f"{cfg['name']}.jsonl"
        recs = read_jsonl(f)
        if args.rerun_changed_retrieval and cfg["rag"]:
            redo = [r for r in recs if replayed(bg, r) != r["graph_result"]]
            if redo:
                with open(out / "superseded_records.jsonl", "a", encoding="utf-8") as fh:
                    for r in redo:
                        fh.write(json.dumps(dict(r, superseded_because="the logged query returns other data from the "
                                                 "corrected knowledge graph", superseded_on=str(datetime.date.today())),
                                            ensure_ascii=False) + "\n")
                recs = [r for r in recs if r not in redo]
                tmp = f.with_suffix(".tmp")
                tmp.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in recs), encoding="utf-8")
                tmp.replace(f)
                print(f"{cfg['name']}: {len(redo)} questions return other data now and are posed again: "
                      f"{sorted(r['ID'] for r in redo)}", flush=True)
        stale = [r for r in recs if judge_of(r) != (args.judge, args.grader_prompt)
                 or r["reference"] != by_id[r["ID"]]["answer"]]
        if stale:
            print(f"{cfg['name']}: grading {len(stale)} logged answers again with {args.judge} ({args.grader_prompt})",
                  flush=True)

            def rework(rec):
                if not budget.allows(provider(args.judge), 0.05):
                    return False
                regrade(rec, by_id[rec["ID"]], args.judge, args.effort, args.grader_prompt)
                for c in rec["calls"]:
                    if c["step"] in ("grade", "idk_check"):
                        budget.add(provider(c["model"]), c["cost"])
                return True

            with cf.ThreadPoolExecutor(args.workers) as pool:
                if not all(list(pool.map(rework, stale))):
                    stopped.append(cfg["name"])
            tmp = f.with_suffix(".tmp")
            tmp.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in recs), encoding="utf-8")
            tmp.replace(f)
        done = {r["ID"] for r in recs}
        open_q = [q for q in todo if int(q["ID"]) not in done]
        print(f"{cfg['name']}: {len(done)} done, {len(open_q)} to run", flush=True)

        def work(q, cfg=cfg, f=f):
            provs = {provider(cfg["model"]), provider(args.judge)}
            if not all(budget.allows(p, 0.05) for p in provs):
                return None
            rec = run_one(q, cfg, bg, query_prompt, direct_prompt, args.judge, args.effort, args.grader_prompt)
            for c in rec["calls"]:
                budget.add(provider(c["model"]), c["cost"])
            with lock:
                with open(f, "a", encoding="utf-8") as fh:
                    fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
            return rec

        with cf.ThreadPoolExecutor(args.workers) as pool:
            for i, rec in enumerate(pool.map(work, open_q), 1):
                if rec is None:
                    stopped.append(cfg["name"])
                    continue
                if i % 25 == 0 or i == len(open_q):
                    print(f"  {cfg['name']}: {i}/{len(open_q)}  spent {json.dumps(budget.spent)}", flush=True)
    rows = summarize(configs, out)
    for r in rows:
        print(json.dumps(r))
    print("spent (USD, estimated from token counts):", json.dumps(budget.spent))
    if stopped:
        print(f"STOPPED at the spending cap for: {sorted(set(stopped))}. Raise --caps and run again to resume.")


def check(args):
    for prov, env in (("openai", "OPENAI_API_KEY"), ("anthropic", "ANTHROPIC_API_KEY"), ("gemini", "GEMINI_API_KEY")):
        print(f"{prov}: key {'present' if os.environ.get(env) else 'MISSING'}")
    try:
        ids = sorted(m.id for m in client("openai").models.list())
        print("openai models:", ", ".join(i for i in ids if i.startswith(("gpt-", "o"))))
    except Exception as exc:
        print("openai models: error", type(exc).__name__, str(exc)[:160])
    try:
        names = sorted(m.name.split("/")[-1] for m in client("gemini").models.list())
        print("gemini models:", ", ".join(n for n in names if "flash" in n or "pro" in n))
    except Exception as exc:
        print("gemini models: error", type(exc).__name__, str(exc)[:160])
    for m in args.rag + args.no_rag + [args.judge]:
        r = call(m, "Reply with the single word: ok", None, args.effort, max_tokens=2000)
        print(f"{m:28s} {'OK' if not r.get('error') else 'FAIL'}  reply={r['text'][:20]!r} in={r['input']} out={r['output']} "
              f"reasoning={r['reasoning']} stop={r['stop']} cost=${r['cost']:.5f} {r.get('error', '')}")


def check_references(bg, questions):
    issues = reference_issues(bg, questions)
    print(f"{len(issues)} of {len(questions)} questions have a reference that differs from the current cell data")
    for qid, why in issues.items():
        print(" ", qid, why)


def reference_issues(bg, questions) -> dict:
    """Does each reference answer still match the current cell data? (No model calls.) ID -> reason"""
    norm = lambda s: re.sub(r"[^0-9a-z]", "", str(s).lower())
    cells = sorted(bg.cells, key=lambda c: -len(c.full_name))
    issues = {}
    for q in questions:
        cat = category(q)
        if cat in ("Negative control", "Derived value"):
            continue
        nq = norm(q["query"])
        named = [c for c in cells if norm(c.full_name) in nq or (norm(c.name) in nq and norm(c.manufacturer) in nq)]
        if not named:
            issues[q["ID"]] = f"{cat}: cell not found under this name in the current data"
            continue
        blob = json.dumps([bg.get_all_cell_properties(c.name, c.manufacturer) + bg.get_cell_info(c.name, c.manufacturer)
                           for c in named[:2]], default=str)
        ref = q["answer"]
        if not reference_in_result(ref, json.loads(blob)):
            issues[q["ID"]] = f"{cat}: reference {ref!r} not in the current data"
    return issues


if __name__ == "__main__":
    main()
