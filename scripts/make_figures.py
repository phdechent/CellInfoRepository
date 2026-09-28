"""Recreate the evaluation figures and summary table from recorded results
(no model calls).

    python scripts/make_figures.py
"""
import argparse
import os
import sys

import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from batterygraph.evaluate import plot_figures, summarize  # noqa: E402


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--results", default="evaluation/results/graphrag_evaluation_results.csv")
    p.add_argument("--outdir", default="evaluation/figures")
    p.add_argument("--format", default="svg", choices=["svg", "png", "pdf"])
    args = p.parse_args()

    results = pd.read_csv(args.results)
    summary = summarize(results)
    summary_path = os.path.join(os.path.dirname(args.results), "summary.csv")
    summary.round(4).to_csv(summary_path, index=False)
    print(summary.round(3).to_string(index=False))
    for path in plot_figures(results, args.outdir, fmt=args.format):
        print("wrote", path)
    print("wrote", summary_path)


if __name__ == "__main__":
    main()
