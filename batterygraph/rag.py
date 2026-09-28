"""GraphRAG: the LLM writes helper calls or SPARQL, the graph answers, and the
LLM phrases the final answer from the retrieved facts only."""

from __future__ import annotations

import ast
import json
import re
from typing import Any, Dict, List, Optional

from . import prompts
from .graph import NUMERIC_PROPERTIES, BatteryGraph
from .llm import LLM

HELPERS = ("query_cell_property", "get_all_cell_properties", "get_cell_info")
_SPARQL_START = re.compile(r"^\s*(PREFIX|SELECT|ASK)\b", re.IGNORECASE | re.MULTILINE)
_FORBIDDEN_SPARQL = re.compile(r"\b(INSERT|DELETE|LOAD|CLEAR|DROP|CREATE|SERVICE)\b", re.IGNORECASE)


def strip_code_fences(text: str) -> str:
    text = text.strip()
    match = re.search(r"```[a-zA-Z]*\s*\n?(.*?)```", text, re.DOTALL)
    return (match.group(1) if match else text).strip()


def _literal(node: ast.AST) -> Any:
    return ast.literal_eval(node)


def _run_call(bg: BatteryGraph, node: ast.AST) -> Any:
    """Execute one helper call. Only the three helper functions with literal
    arguments are allowed; nothing else from the LLM output is evaluated."""
    if not (isinstance(node, ast.Call) and isinstance(node.func, (ast.Name, ast.Attribute))):
        raise ValueError("not a helper call")
    name = node.func.id if isinstance(node.func, ast.Name) else node.func.attr
    if name not in HELPERS:
        raise ValueError(f"function '{name}' is not allowed")
    args = [_literal(a) for a in node.args]
    kwargs = {k.arg: _literal(k.value) for k in node.keywords if k.arg}
    # tolerate the old signature helper(graph, ctx, ...)
    args = [a for a in args if a not in ("graph", "ctx")]
    return getattr(bg, name)(*args, **kwargs)


def _run_python(bg: BatteryGraph, code: str) -> List[Any]:
    tree = ast.parse(code, mode="exec")
    results: List[Any] = []
    for stmt in tree.body:
        value = stmt.value if isinstance(stmt, (ast.Expr, ast.Assign)) else None
        if value is None:
            continue
        nodes = value.elts if isinstance(value, (ast.List, ast.Tuple)) else [value]
        for node in nodes:
            results.append(_run_call(bg, node))
    if not results:
        raise ValueError("no helper call found")
    return results[0] if len(results) == 1 else results


def execute_query(bg: BatteryGraph, generated: str) -> Any:
    """Run LLM output against the graph: helper call(s) or a read-only SPARQL query."""
    if not generated or not generated.strip():
        return [{"error": "no query generated"}]
    code = strip_code_fences(generated)

    if any(h in code for h in HELPERS) and not _SPARQL_START.match(code):
        try:
            return _run_python(bg, code)
        except Exception:
            # the model mixed prose and code: run each line that is a call
            lines = [l.strip().rstrip(",") for l in code.splitlines() if l.strip().startswith(HELPERS)]
            try:
                return [_run_python(bg, l) for l in lines] or [{"error": "could not parse helper call"}]
            except Exception as exc:
                return [{"error": f"helper call failed: {exc}"}]

    if _FORBIDDEN_SPARQL.search(code):
        return [{"error": "only read-only SELECT/ASK queries are allowed"}]
    try:
        rows = bg.sparql(code)
    except Exception as exc:
        return [{"error": f"SPARQL error: {exc}"}]
    if rows:
        return rows
    # Empty result: fall back to a property lookup if the query names a cell and a property.
    prop = next((p for p in NUMERIC_PROPERTIES if p.lower() in code.lower()), None)
    names = [s for s in re.findall(r'"([^"]{2,})"', code) if not s.startswith("http")]
    if prop and names:
        fallback = [r for n in names for r in bg.query_cell_property(n, prop) if r.get("value") is not None]
        if fallback:
            return fallback
    return rows


class GraphRAG:
    """Answer questions about battery cells from the knowledge graph.

    >>> rag = GraphRAG(BatteryGraph("BatteryTypeJson"), model="claude-sonnet-5")
    >>> rag.answer("What is the rated capacity of the Samsung SDI INR21700-50E?")
    """

    def __init__(self, bg: BatteryGraph, model: str, pause: float = 0.0, verbose: bool = False):
        self.bg = bg
        self.llm = LLM(model, pause=pause)
        self.verbose = verbose
        self.query_prompt = prompts.query_generation_prompt(NUMERIC_PROPERTIES, bg.manufacturers)
        self.direct_prompt = prompts.DIRECT_ANSWER.format(manufacturers=bg.manufacturers)

    def generate_query(self, question: str) -> str:
        return self.llm.complete(self.query_prompt + "\nQuestion: " + question + "\nCode:")

    def retrieve(self, question: str) -> Dict[str, Any]:
        query = self.generate_query(question)
        result = execute_query(self.bg, query)
        return {"query": query, "result": result}

    def answer(self, question: str, details: bool = False):
        step = self.retrieve(question)
        result_text = json.dumps(step["result"], indent=1, default=str)
        if self.verbose:
            print("Generated query:\n" + step["query"] + "\n\nGraph result:\n" + result_text + "\n")
        answer = self.llm.complete(
            f"Question: {question}\n\nQuery Result: {result_text}", system=prompts.FINAL_ANSWER_SYSTEM
        )
        if details:
            return {**step, "answer": answer}
        return answer

    def answer_without_rag(self, question: str) -> str:
        """Baseline: the model answers from its own knowledge only."""
        return self.llm.complete(self.direct_prompt + "\nQuestion: " + question)
