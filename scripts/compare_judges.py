"""Compare judge models and grading prompts on the answers of the logged re-run.

    python scripts/compare_judges.py build     # test set with rule-based reference labels
    python scripts/compare_judges.py run       # every judge x prompt on the test set (logged, resumable, capped)
    python scripts/compare_judges.py report    # agreement of each judge with the reference labels
    python scripts/compare_judges.py crosscheck --config claude-opus-5-5_llm_only --judges gemini-3.8-flash
                                               # a second judge on one configuration (e.g. where the judge graded
                                               # its own answers); agreement with the logged grades

Test set: each distinct (question, answer) of the four configurations in results_rerun_2026-10, once.
Reference labels come from fixed rules (rule_label: numbers compared in the reference's unit at the reference's
precision, label synonyms, the cell named in comparisons, negative controls). Where the rules were wrong, a
hand-checked label with its reason is kept in judges/label_overrides.json. Items the rules cannot decide are
"ambiguous" and left out of the scores.
"""
from __future__ import annotations

import argparse
import collections
import concurrent.futures as cf
import hashlib
import json
import math
import re
import sys
import threading
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from rerun_eval_logged import GRADER_PROMPTS, Budget, bit, call, provider, read_jsonl  # noqa: E402

RUN = ROOT / "evaluation" / "results_rerun_2026-10"
OUT = RUN / "judges"
CONFIGS = ("gemini-3.8-flash_rag", "claude-sonnet-5-5_rag", "gpt-6.1-sol_rag", "gemini-3.8-flash_llm_only")
JUDGES = ("claude-sonnet-5-5", "claude-opus-5-5", "claude-haiku-5-5", "gpt-6.1-sol", "gemini-3.8-flash")

PROMPTS = {name: (lambda f: lambda it: f(it["question"], it["reference"], it["answer"]))(f)
           for name, f in GRADER_PROMPTS.items()}

# ------------------------------------------------------------------------------------------- reference labels
UNITS = {"m": ("m", 1), "mm": ("m", 1e-3), "cm": ("m", 1e-2), "ah": ("Ah", 1), "mah": ("Ah", 1e-3),
         "wh": ("Wh", 1), "kwh": ("Wh", 1e3), "mwh": ("Wh", 1e-3), "v": ("V", 1), "mv": ("V", 1e-3),
         "a": ("A", 1), "ma": ("A", 1e-3), "kg": ("kg", 1), "g": ("kg", 1e-3), "cycles": ("cycles", 1),
         "cycle": ("cycles", 1)}
QTY = re.compile(r"(?<![\w.])(-?\d{1,3}(?:,\d{3})+(?:\.\d+)?|-?\d+(?:\.\d+)?)\s*"
                 r"(kWh|mWh|Wh|mAh|Ah|mV|V|mA|A|mm|cm|m|kg|g|cycles|cycle)(?![A-Za-z/])")
LABELS = {  # canonical label: answer patterns
    "PrismaticCase": r"prismatic", "CylindricalCase": r"cylindrical", "PouchCase": r"pouch",
    "R18650": r"\b(r)?18650\b", "R21700": r"\b(r)?21700\b", "R26650": r"\b(r)?26650\b",
    "LithiumNickelManganeseCobaltOxide": r"nickel ?manganese ?cobalt|\bnmc\b|\bncm\b",
    "LithiumNickelCobaltAluminiumOxide": r"nickel ?cobalt ?alumin|\bnca\b|\blncao\b",
    "LithiumIronPhosphate": r"iron ?phosphate|\blfp\b|lifepo4",
    "LithiumCobaltOxide": r"lithium ?cobalt ?oxide|\blco\b|licoo2",
    "LithiumManganeseOxide": r"lithium ?manganese ?oxide|\blmo\b|limn2o4",
}
CYLINDRICAL = {"CylindricalCase", "R18650", "R21700", "R26650"}
NOT_AVAILABLE = re.compile(r"not (available|recorded|applicable|known|found|specified|listed|provided|in the)|"
                           r"no (value|data|information|diameter|record)|unknown|n/a|(do not|don't|cannot|can't) "
                           r"(know|give|determine|provide|find)|does not (have|apply)|isn't|is not (available|recorded)",
                           re.I)


UNIT_RE = r"(kWh|mWh|Wh|mAh|Ah|mV|V|mA|A|mm|cm|m|kg|g|cycles|cycle)(?![A-Za-z/])"
RANGE = re.compile(r"(-?\d+(?:\.\d+)?)\s*(?:–|—|-|to)\s*(-?\d+(?:\.\d+)?)\s*" + UNIT_RE)


def quantities(text, question=""):
    """(dimension, value in base unit, decimals in base unit) of every number with a unit; "2.4–4.2 V" gives two.
    Designations taken from the question (e.g. the cell name "94Ah") are not values."""
    for token in re.findall(r"[\w-]*\d[\w-]*", question):
        if re.search(r"[A-Za-z]", token):
            text = text.replace(token, " ")
    text = RANGE.sub(r"\1 \3 to \2 \3", text)
    out = []
    for num, unit in QTY.findall(text):
        num = num.replace(",", "")
        dim, factor = UNITS[unit.lower()]
        dec = len(num.split(".")[1]) if "." in num else 0
        out.append((dim, float(num) * factor, dec - round(math.log10(factor))))  # value and decimals in base unit
    return out


def same_value(ref, ans):
    """ans agrees with ref: at the reference's precision (at least one decimal in the reference unit), or, if the
    answer is coarser, at the answer's precision and within 0.5 % (20.4 Wh for 20.44 Wh, not 3.6 V for 3.65 V)."""
    (dim_r, v_r, dec_r), (dim_a, v_a, dec_a) = ref, ans
    if dim_r != dim_a:
        return False
    close = lambda a, b: abs(a - b) <= 1e-9 * max(1.0, abs(b))
    need = dec_r + 1 if dec_r <= 0 and abs(v_r) < 100 else dec_r  # "3 Ah" (stored 3.0) is not matched by 3.2 Ah
    if dec_a >= need:
        return close(round(v_a, need), round(v_r, need))
    return close(round(v_a, dec_a), round(v_r, dec_a)) and abs(v_a - v_r) <= 0.005 * abs(v_r)


def labels_in(text):
    t = text.lower()
    return {k for k, pat in LABELS.items() if re.search(pat, t)}


def rule_label(it):
    """(1 | 0 | "ambiguous", reason) for one answer."""
    ans, ref, q, cat = it["answer"].strip(), it["reference"].strip(), it["question"], it["category"]
    if ans.startswith("ERROR:") or not ans:
        return 0, "no answer"
    if ref == "Not available":
        if quantities(ans, q):
            return 0, "gives a value where the solution is not available"
        if NOT_AVAILABLE.search(ans):
            return 1, "says the information is not available"
        return "ambiguous", "neither a value nor a clear not-available"
    if cat == "Comparison of two cells":
        m = re.match(r"(Yes|No)\b", ref)
        if m:
            a = re.match(r"\W*(yes|no)\b", ans, re.I)
            return (int(a.group(1).lower() == m.group(1).lower()), "yes/no") if a else ("ambiguous", "no yes/no")
        names = re.search(r"the (.+?) or the (.+?)\?\s*$", q)
        winner = ref.split(" (")[0].strip()
        if not names:
            return "ambiguous", "cell names not found in the question"
        norm = lambda s: re.sub(r"[^0-9a-z]", "", s.lower())
        ident = lambda name: norm(max((t for t in name.split() if re.search(r"\d", t)), key=len, default=name))
        loser = [n for n in names.groups() if norm(n) != norm(winner)]
        has_w = ident(winner) in norm(ans)
        has_l = bool(loser) and ident(loser[0]) in norm(ans)
        if has_w and not has_l:
            return 1, "names the right cell"
        if has_l and not has_w:
            return 0, "names the other cell"
        return "ambiguous", "names both cells or neither"
    if cat == "Case and chemistry":
        want = labels_in(ref) if ref not in LABELS else {ref}
        if "ambig" in ref.lower() or not want:
            return "ambiguous", "reference label unclear"
        got = labels_in(ans)
        if NOT_AVAILABLE.search(ans) and not got:
            return 0, "says not available where the solution gives a label"
        if want == {"PrismaticCase"} and "PouchCase" in got:
            return "ambiguous", "pouch for PrismaticCase (pouch cells are stored as PrismaticCase)"
        if want <= CYLINDRICAL - {"CylindricalCase"} and got == {"CylindricalCase"}:
            return "ambiguous", "cylindrical without the size"
        if want <= got and (not (got - want) or (want | got) <= CYLINDRICAL):
            return 1, "same label"
        return 0, f"different label: {sorted(got) or ans[:40]}"
    want = quantities(ref)
    if not want:
        return ("ambiguous", "reference without a value") if ans.lower() != ref.lower() else (1, "identical")
    got = quantities(ans, q)
    if not got and {w[0] for w in want} == {"cycles"}:  # a cycle life is often given without the unit
        got = quantities(re.sub(r"(\d[\d,]*)\s*$", r"\1 cycles", ans), q)
    if not got:
        return 0, ("says not available" if NOT_AVAILABLE.search(ans) else "no value in the answer")
    missing = [w for w in want if not any(same_value(w, g) for g in got)]
    return (1, "values agree") if not missing else (0, f"value differs or missing: {missing[0][1]:g} {missing[0][0]}")


def key(rec):
    answer = re.sub(r"\s+", " ", rec["answer"].strip().lower())
    return f"{rec['ID']}:" + hashlib.sha1(answer.encode()).hexdigest()[:10]


def build():
    items = {}
    for cfg in CONFIGS:
        for r in read_jsonl(RUN / f"{cfg}.jsonl"):
            it = items.setdefault(key(r), {"key": key(r), "ID": r["ID"], "category": r["category"], "question": r["question"],
                                           "reference": r["reference"], "answer": r["answer"],
                                           "reference_issue": r.get("reference_issue", ""), "configs": []})
            it["configs"].append(cfg)
    overrides = json.loads((OUT / "label_overrides.json").read_text()) if (OUT / "label_overrides.json").exists() else {}
    for it in items.values():
        it["label"], it["label_reason"] = rule_label(it)
        if it["key"] in overrides:
            it["label"], it["label_reason"] = overrides[it["key"]]["label"], "by hand: " + overrides[it["key"]]["reason"]
    OUT.mkdir(parents=True, exist_ok=True)
    rows = sorted(items.values(), key=lambda i: (i["ID"], i["key"]))
    (OUT / "testset.jsonl").write_text("".join(json.dumps(i, ensure_ascii=False) + "\n" for i in rows), encoding="utf-8")
    print(f"{len(rows)} items:", dict(collections.Counter(str(i["label"]) for i in rows)), f"({len(overrides)} by hand)")
    return rows


# ----------------------------------------------------------------------------------------------- judging
def run(args):
    items = read_jsonl(OUT / "testset.jsonl")
    budget = Budget({k: float(v) for k, v in (c.split("=") for c in args.caps)}, RUN / "spent_usd.json")
    lock, stopped = threading.Lock(), set()
    tasks = []
    for judge in args.judges:
        for name in args.prompts:
            f = OUT / f"{judge}__{name}.jsonl"
            done = {r["key"] for r in read_jsonl(f)}
            tasks += [(judge, name, f, it) for it in items if it["key"] not in done]

    def work(t):
        judge, name, f, it = t
        if not budget.allows(provider(judge), 0.05):
            stopped.add(judge)
            return
        prompt, system = PROMPTS[name](it)
        g = call(judge, prompt, system, args.effort, max_tokens=2000)
        budget.add(provider(judge), g["cost"])
        rec = {"key": it["key"], "judge": judge, "prompt": name, "effort": args.effort, "parsed": bit(g["text"]), **g}
        with lock, open(f, "a", encoding="utf-8") as fh:
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")

    print(f"{len(tasks)} judge calls to make", flush=True)
    with cf.ThreadPoolExecutor(args.workers) as pool:
        for i, _ in enumerate(pool.map(work, tasks), 1):
            if i % 500 == 0:
                print(f"  {i}/{len(tasks)}  spent {json.dumps({k: round(v, 2) for k, v in budget.spent.items()})}", flush=True)
    print("spent:", {k: round(v, 2) for k, v in budget.spent.items()}, "STOPPED at cap: " + str(sorted(stopped)) if stopped else "")


def report(args):
    items = {i["key"]: i for i in read_jsonl(OUT / "testset.jsonl")}
    rows = []
    for f in sorted(OUT.glob("*__*.jsonl")):
        recs = read_jsonl(f)
        sc = collections.Counter()
        by_cat = collections.defaultdict(collections.Counter)
        for r in recs:
            it = items.get(r["key"])
            if it is None:
                continue
            lab, got = it["label"], r["parsed"]
            if got is None:
                sc["unclear"] += 1
            if lab == "ambiguous":
                sc["ambiguous_" + str(got)] += 1
                continue
            sc["scored"] += 1
            if got == lab:
                sc["agree"] += 1
            elif got == 1:
                sc["false_accept"] += 1
                by_cat[it["category"]]["false_accept"] += 1
            else:
                sc["false_reject"] += 1
                by_cat[it["category"]]["false_reject"] += 1
        n = sc["scored"]
        rows.append({"judge": f.stem, "items": len(recs), "scored": n, "agree": round(sc["agree"] / n, 4) if n else None,
                     "false_accept": sc["false_accept"], "false_reject": sc["false_reject"], "unclear": sc["unclear"],
                     "ambiguous_as_1/0": f"{sc['ambiguous_1']}/{sc['ambiguous_0']}",
                     "cost_usd": round(sum(r["cost"] for r in recs), 3),
                     "errors_by_category": {c: dict(v) for c, v in by_cat.items()}})
    for r in rows:
        print(json.dumps(r, ensure_ascii=False))
    (OUT / "report.json").write_text(json.dumps(rows, indent=1, ensure_ascii=False), encoding="utf-8")


def disagreements(args):
    """Items where judges with the question-aware prompt disagree with the reference label (for checking by hand)."""
    items = {i["key"]: i for i in read_jsonl(OUT / "testset.jsonl")}
    votes = collections.defaultdict(dict)
    for f in OUT.glob("*__*.jsonl"):
        for r in read_jsonl(f):
            votes[r["key"]][f.stem] = r["parsed"]
    for k, it in items.items():
        v = votes.get(k, {})
        wq = [x for j, x in v.items() if j.endswith("with_question")]
        if it["label"] == "ambiguous" or (wq and any(x != it["label"] for x in wq)):
            print(json.dumps({"key": k, "label": it["label"], "why": it["label_reason"], "q": it["question"],
                              "ref": it["reference"], "ans": it["answer"][:200],
                              "votes": {j.replace("__with_question", "+Q").replace("__published", ""): x
                                        for j, x in sorted(v.items())}}, ensure_ascii=False))


def crosscheck(args):
    recs = read_jsonl(RUN / f"{args.config}.jsonl")
    budget = Budget({k: float(v) for k, v in (c.split("=") for c in args.caps)}, RUN / "spent_usd.json")
    for judge in args.judges:
        f = OUT / f"crosscheck_{args.config}__{judge}__{args.prompts[-1]}.jsonl"
        done = {r["ID"] for r in read_jsonl(f)}
        lock = threading.Lock()

        def work(r):
            if r["ID"] in done or not budget.allows(provider(judge), 0.05):
                return
            g = call(judge, *PROMPTS[args.prompts[-1]](r), args.effort, max_tokens=2000)
            budget.add(provider(judge), g["cost"])
            logged = next(c for c in reversed(r["calls"]) if c["step"] == "grade")
            out = {"ID": r["ID"], "judge": judge, "logged_judge": r["judge"], "logged": logged.get("parsed"),
                   "parsed": bit(g["text"]), **g}
            with lock, open(f, "a", encoding="utf-8") as fh:
                fh.write(json.dumps(out, ensure_ascii=False) + "\n")

        with cf.ThreadPoolExecutor(args.workers) as pool:
            list(pool.map(work, recs))
        rows = read_jsonl(f)
        same = sum(r["parsed"] == r["logged"] for r in rows)
        print(f"{args.config}: {judge} agrees with the logged grades ({rows[0]['logged_judge'] if rows else '?'}) "
              f"on {same} of {len(rows)} answers")
        by_id = {r["ID"]: r for r in recs}
        for r in rows:
            if r["parsed"] != r["logged"]:
                a = by_id[r["ID"]]
                print(f"   {r['ID']}: logged {r['logged']}, {judge} {r['parsed']} | ref {a['reference'][:40]!r} | "
                      f"ans {a['answer'][:80]!r}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("step", choices=["build", "run", "report", "disagreements", "crosscheck"])
    ap.add_argument("--config", help="configuration for crosscheck, e.g. claude-opus-5-5_llm_only")
    ap.add_argument("--judges", nargs="+", default=list(JUDGES))
    ap.add_argument("--prompts", nargs="+", default=list(PROMPTS))
    ap.add_argument("--effort", default="low")
    ap.add_argument("--caps", nargs="+", default=["openai=3.0", "gemini=8.0", "anthropic=14.0"])
    ap.add_argument("--workers", type=int, default=12)
    a = ap.parse_args()
    {"build": lambda: build(), "run": lambda: run(a), "report": lambda: report(a),
     "disagreements": lambda: disagreements(a), "crosscheck": lambda: crosscheck(a)}[a.step]()
