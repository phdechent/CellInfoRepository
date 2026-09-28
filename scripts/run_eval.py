"""Run the GraphRAG evaluation on the Q&A set.

Examples:
    python scripts/run_eval.py --check claude-sonnet-5 gpt-5.4 gemini-3.5-flash   # API smoke test
    python scripts/run_eval.py --model claude-sonnet-5 --limit 5                  # quick test
    python scripts/run_eval.py --model gemini-3.5-flash --no-rag                  # LLM-only baseline
    python scripts/run_eval.py --model gpt-5.4 --output evaluation/results/run.csv --start-id 114   # resume

API keys are read from the environment or a local .env file (see .env.example).
"""
import argparse
import os
import sys

import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from batterygraph import BatteryGraph, GraphRAG  # noqa: E402
from batterygraph.evaluate import ID_WRONG_JUDGE, run_evaluation, summarize  # noqa: E402
from batterygraph.llm import check_models  # noqa: E402


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--model", help="model that generates queries and answers")
    p.add_argument("--no-rag", action="store_true", help="baseline: answer without the knowledge graph")
    p.add_argument("--judge", help="grading model (default: same as --model, as in the recorded runs)")
    p.add_argument("--id-judge", default=ID_WRONG_JUDGE,
                   help=f"model for the 'identifiably wrong' check (default {ID_WRONG_JUDGE})")
    p.add_argument("--questions", default="evaluation/qa_dataset.csv")
    p.add_argument("--data", default="BatteryTypeJson")
    p.add_argument("--output", help="results CSV (default evaluation/results/<model>[_no_rag].csv)")
    p.add_argument("--start-id", type=int, default=1, help="resume from this question ID")
    p.add_argument("--limit", type=int, help="only the first N questions")
    p.add_argument("--pause", type=float, default=0.0, help="seconds to wait after each model call")
    p.add_argument("--check", nargs="+", metavar="MODEL", help="only test API access for these models")
    args = p.parse_args()

    if args.check:
        check_models(*args.check)
        return
    if not args.model:
        p.error("--model is required")

    output = args.output or os.path.join(
        "evaluation", "results", f"{args.model}{'_no_rag' if args.no_rag else ''}.csv"
    )
    # resume from the partial output if it exists
    source = output if args.start_id > 1 and os.path.exists(output) else args.questions
    questions = pd.read_csv(source)
    if args.limit:
        questions = questions.head(args.limit)

    bg = BatteryGraph(args.data)
    rag = GraphRAG(bg, model=args.model, pause=args.pause)
    print(f"{len(bg.cells)} cells, {len(bg):,} triples | model {args.model} | judge {args.judge or args.model} | "
          f"{'no RAG' if args.no_rag else 'GraphRAG'} | {len(questions)} questions")
    results = run_evaluation(questions, rag, use_rag=not args.no_rag, judge_model=args.judge,
                             id_wrong_model=args.id_judge,
                             output_csv=output, start_id=args.start_id)
    print(summarize(results).to_string(index=False))
    print(f"Saved {output}")


if __name__ == "__main__":
    main()
