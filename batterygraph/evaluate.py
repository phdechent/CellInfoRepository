"""Evaluate GraphRAG against the Q&A set and reproduce the paper figures.

Column naming (as in ``evaluation/results/graphrag_evaluation_results.csv``):

* with retrieval:    ``rag_answer_<model>``, ``is_correct_<model>``, ``identifiably_wrong_<model>``
* without retrieval: ``no_rag_answer_<model>``, ``no_rag_is_correct_<model>``, ``no_rag_identifiably_wrong_<model>``

``is_correct`` is graded by an LLM judge (1 = correct); as in the recorded runs,
the judge defaults to the answering model. For incorrect answers,
``identifiably_wrong`` is 1 when the answer admits that it does not know or that
data is missing, and 0 when it states a wrong value (a hallucination); this
check used ``gemini-3.5-flash`` for all recorded runs.
"""

from __future__ import annotations

import os
from typing import Dict, List, Optional, Sequence

import pandas as pd

from . import prompts
from .llm import LLM

ID_WRONG_JUDGE = "gemini-3.5-flash"  # "identifiably wrong" judge of the recorded results


def _to_score(text: str) -> float:
    text = (text or "").strip()
    return 1.0 if text.startswith("1") or text == "1.0" else 0.0


def grade(answer: str, solution: str, judge: LLM) -> float:
    reply = judge.complete(f"Answer: {answer}\n\nSolution: {solution}", system=prompts.GRADER_SYSTEM)
    return _to_score(reply)


def identifiably_wrong(answer: str, solution: str, is_correct: float, judge: LLM) -> float:
    if float(is_correct) == 1.0:
        return 0.0
    if answer is None or (isinstance(answer, float) and pd.isna(answer)) or not str(answer).strip():
        return 1.0
    reply = judge.complete(
        f"{prompts.IDENTIFIABLY_WRONG}\n\nGround Truth Solution: {solution}\nAI Answer: {answer}\n\n"
        "Identifiably wrong (1 or 0):"
    )
    return 1.0 if "1" in reply else 0.0


def columns(model: str, rag: bool = True) -> Dict[str, str]:
    prefix = "" if rag else "no_rag_"
    return {
        "answer": f"{prefix}rag_answer_{model}" if rag else f"no_rag_answer_{model}",
        "correct": f"{prefix}is_correct_{model}",
        "id_wrong": f"{prefix}identifiably_wrong_{model}",
    }


def run_evaluation(
    questions: pd.DataFrame,
    rag,
    use_rag: bool = True,
    judge_model: Optional[str] = None,
    id_wrong_model: str = ID_WRONG_JUDGE,
    output_csv: Optional[str] = None,
    start_id: int = 1,
    save_every: int = 10,
) -> pd.DataFrame:
    """Answer every question with ``rag`` (a :class:`GraphRAG`) and grade it.

    Resume an interrupted run by passing the partially written ``output_csv``
    as ``questions`` and the next ``start_id``.
    """
    df = questions.copy()
    judge = LLM(judge_model or rag.llm.model, pause=rag.llm.pause)
    id_judge = LLM(id_wrong_model, pause=rag.llm.pause)
    cols = columns(rag.llm.model, use_rag)
    for col in cols.values():
        if col not in df.columns:
            df[col] = None

    for n, (idx, row) in enumerate(df.iterrows(), 1):
        if int(row["ID"]) < start_id:
            continue
        try:
            answer = rag.answer(row["query"]) if use_rag else rag.answer_without_rag(row["query"])
            score = grade(answer, row["answer"], judge)
            id_wrong = identifiably_wrong(answer, row["answer"], score, id_judge)
        except Exception as exc:  # keep going; the error text is graded as "identifiably wrong"
            answer, score, id_wrong = f"ERROR: {str(exc)[:100]}", 0.0, 1.0
        df.at[idx, cols["answer"]] = answer
        df.at[idx, cols["correct"]] = score
        df.at[idx, cols["id_wrong"]] = id_wrong
        print(f"[Q{row['ID']}] correct={score:.0f} identifiably_wrong={id_wrong:.0f} | {str(answer)[:60]}")
        if output_csv and n % save_every == 0:
            df.to_csv(output_csv, index=False)
    if output_csv:
        df.to_csv(output_csv, index=False)
    return df


def summarize(results: pd.DataFrame) -> pd.DataFrame:
    """Accuracy and hallucination robustness for every evaluated run in ``results``.

    * accuracy = correct / all questions
    * hallucination robustness = "I don't know" answers / incorrect answers
    """
    rows = []
    for col in results.columns:
        for prefix, mode in (("is_correct_", "GraphRAG"), ("no_rag_is_correct_", "LLM only")):
            if not col.startswith(prefix) or (prefix == "is_correct_" and col.startswith("no_rag_")):
                continue
            model = col[len(prefix):]
            id_col = col.replace("is_correct_", "identifiably_wrong_")
            correct = pd.to_numeric(results[col], errors="coerce")
            wrong = correct == 0
            ident = pd.to_numeric(results.loc[wrong, id_col], errors="coerce") == 1 if id_col in results else pd.Series(dtype=bool)
            rows.append({
                "model": model,
                "mode": mode,
                "questions": int(correct.notna().sum()),
                "correct": int((correct == 1).sum()),
                "incorrect": int(wrong.sum()),
                "identifiably_wrong": int(ident.sum()),
                "accuracy": (correct == 1).sum() / len(results),
                "hallucination_robustness": ident.sum() / wrong.sum() if wrong.sum() else float("nan"),
            })
    return pd.DataFrame(rows)


# Runs shown in the paper figures, in plot order: (model, mode, label)
PAPER_RUNS: Sequence = (
    ("gemini-3.5-flash", "GraphRAG", "Gemini-Flash3.5\n+RAG"),
    ("gemini-3.5-flash", "LLM only", "Gemini-Flash3.5\n only"),
    ("claude-sonnet-5", "GraphRAG", "Claude Sonnet 5\n+RAG"),
    ("gpt-5.4", "GraphRAG", "OpenAI GPT-5.4\n+RAG"),
)


def plot_figures(results: pd.DataFrame, outdir: str, runs: Sequence = PAPER_RUNS, fmt: str = "svg") -> List[str]:
    """Write the accuracy (a) and hallucination-robustness (b) bar charts."""
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    summary = summarize(results).set_index(["model", "mode"])
    labels = [label for _, _, label in runs]
    accuracy = [summary.loc[(m, mode), "accuracy"] for m, mode, _ in runs]
    robustness = [summary.loc[(m, mode), "hallucination_robustness"] for m, mode, _ in runs]
    os.makedirs(outdir, exist_ok=True)
    written = []
    specs = (
        ("RAG_Accuracy", accuracy, "skyblue", "(a)", "accuracy", r"ratio of $\frac{Correct}{All\ Questions}$"),
        ("RAG_HallucinationRobustness", robustness, "orange", "(b)", "hallucination robustness",
         r"ratio of $\frac{I\ don't\ know}{incorrect\ answers}$"),
    )
    for name, values, color, tag, ylabel, legend in specs:
        fig, ax = plt.subplots(figsize=(7, 4))
        bars = ax.bar(labels, values, color=color)
        for bar in bars:
            h = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, h / 2, f"{h:.2f}", ha="center", va="center", fontsize=10)
        ax.text(-0.1, 1.05, tag, transform=ax.transAxes, fontsize=14, fontweight="bold")
        ax.set_ylabel(ylabel)
        ax.set_ylim(0, 1)
        ax.legend(labels=[legend])
        path = os.path.join(outdir, f"{name}.{fmt}")
        fig.savefig(path, format=fmt, bbox_inches="tight")
        plt.close(fig)
        written.append(path)
    return written
