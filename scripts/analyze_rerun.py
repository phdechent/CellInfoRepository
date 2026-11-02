"""Tables from the logged re-run (scripts/rerun_eval_logged.py).

    python scripts/analyze_rerun.py [results folder]

Writes into the results folder:
  table_categories.csv  correct answers per question category (%) and the outcome counts per configuration
  error_stages.csv      for the GraphRAG configurations: the step at which each answer that is not correct went wrong
  without_flagged.csv   the outcome counts without the questions whose reference differs from the current cell data
and prints all three, plus answers whose grade the judge left unclear.
"""
import collections
import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = ["Single-property lookup", "Multi-property summary", "Comparison of two cells", "Case and chemistry",
              "Derived value", "Negative control"]
STAGES = ["query_failed", "nothing_retrieved", "other_data", "answer_step", "reference_mismatch"]


def load(out: Path):
    info = json.loads((out / "run_info.json").read_text())
    runs = []
    for cfg in info["configs"]:
        f = out / f"{cfg['name']}.jsonl"
        if f.exists():
            recs = sorted((json.loads(l) for l in f.read_text().splitlines() if l.strip()), key=lambda r: r["ID"])
            runs.append((cfg, recs))
    return runs


def outcome(recs):
    c = sum(r["correct"] for r in recs)
    k = sum(r["i_dont_know"] for r in recs)
    return c, k, len(recs) - c - k


def write(path: Path, rows):
    with open(path, "w", newline="", encoding="utf-8") as fh:
        csv.writer(fh).writerows(rows)
    print(f"\n{path.name}")
    for r in rows:
        print("  " + " | ".join(str(x) for x in r))


def main(out: Path):
    runs = load(out)
    head = ["Category", "n"] + [cfg["name"] for cfg, _ in runs]

    rows = [head]
    for cat in CATEGORIES:
        n = {len([r for r in recs if r["category"] == cat]) for _, recs in runs}
        cells = []
        for _, recs in runs:
            sub = [r for r in recs if r["category"] == cat]
            cells.append(f"{100 * sum(r['correct'] for r in sub) / len(sub):.0f}%" if sub else "")
        rows.append([cat, "/".join(map(str, sorted(n)))] + cells)
    outs = [outcome(recs) for _, recs in runs]
    n_all = "/".join(map(str, sorted({len(recs) for _, recs in runs})))
    rows.append(["All questions: correct", n_all] + [f"{c} ({100 * c / (c + k + w):.0f}%)" for c, k, w in outs])
    rows.append(["All questions: “I don’t know”", ""] + [k for _, k, _ in outs])
    rows.append(["All questions: wrong answer", ""] + [w for _, _, w in outs])
    rows.append(["Hallucination robustness", ""] + [f"{k / (k + w):.2f}" if k + w else "" for _, k, w in outs])
    write(out / "table_categories.csv", rows)

    rows = [["Configuration", "not correct"] + STAGES]
    for cfg, recs in runs:
        if cfg["rag"]:
            st = collections.Counter(r["stage"] for r in recs if not r["correct"])
            rows.append([cfg["name"], sum(st.values())] + [st.get(s, 0) for s in STAGES])
    write(out / "error_stages.csv", rows)

    rows = [["Configuration", "questions", "correct", "I don't know", "wrong", "accuracy", "hallucination robustness"]]
    for cfg, recs in runs:
        sub = [r for r in recs if not r.get("reference_issue")]
        c, k, w = outcome(sub)
        rows.append([cfg["name"], len(sub), c, k, w, f"{c / len(sub):.3f}", f"{k / (k + w):.2f}" if k + w else ""])
    write(out / "without_flagged.csv", rows)

    unclear = [(cfg["name"], r["ID"], r["answer"][:60]) for cfg, recs in runs for r in recs if r.get("grade_unclear")]
    print(f"\ngrades left unclear by the judge: {len(unclear)}", *unclear[:20], sep="\n  ")
    spent = json.loads((out / "spent_usd.json").read_text())
    print("\nspent (USD, from token counts, incl. pilot):", {k: round(v, 2) for k, v in spent.items()})


if __name__ == "__main__":
    main(Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "evaluation" / "results_rerun_2026-10")
