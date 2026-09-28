# Cell Info Repository

Battery-cell specifications as structured, semantic, linked data, and a GraphRAG workflow that answers questions about the cells from the knowledge graph instead of from an LLM's memory.

* **382 cell profiles** (JSON-LD) in [`BatteryTypeJson/`](BatteryTypeJson/), typed with the [EMMO battery domain ontology](https://w3id.org/emmo/domain/battery/context): rated capacity, voltages, currents, cycle life, mass, dimensions, case and cathode chemistry, plus DOI links to publications that use or reference each cell.
* **`batterygraph`**, a small Python package that loads the profiles into an RDF graph (RDFLib), provides query helpers, and runs the GraphRAG workflow with OpenAI, Anthropic, Google Gemini or local Ollama models.
* **Evaluation**: a 300-question benchmark with recorded results for three models with GraphRAG and one LLM-only baseline.

## Repository layout

```
BatteryTypeJson/            382 cell profiles (JSON-LD)
batterygraph/
    graph.py                load the graph, EMMO term <-> IRI mapping, query helpers
    llm.py                  one interface for OpenAI, Anthropic, Gemini and Ollama
    prompts.py              query-generation, answer and grading prompts
    rag.py                  GraphRAG: question -> helper calls / SPARQL -> answer
    evaluate.py             grading, "identifiably wrong" check, summary, figures
notebooks/
    KnowledgeGraphDemo.ipynb    SPARQL and helper-function examples
    GraphRAG.ipynb              ask questions, small evaluation, recorded figures
scripts/
    run_eval.py             run the benchmark for a model (with or without RAG)
    make_figures.py         recreate figures and summary from recorded results
    generate_qa_dataset.py  generate a Q&A benchmark from the profiles
evaluation/
    qa_dataset.csv          the 300 questions and reference answers
    results/                recorded answers and grades, summary.csv
    figures/                RAG_Accuracy.svg, RAG_HallucinationRobustness.svg
```

## Installation

```sh
pip install -r requirements.txt      # or: pip install -e ".[all]"
```

Only the packages for the LLM providers you use are needed. The knowledge graph itself needs `rdflib`, `requests` and `pandas`.

**API keys.** Copy `.env.example` to `.env` and fill in the keys you need (`OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `GEMINI_API_KEY`). `.env` is git-ignored. Local models via [Ollama](https://ollama.com) need no key.

**Offline use.** The profiles reference the context `https://w3id.org/emmo/domain/battery/context`, which is downloaded once when the graph loads. To work offline, save [context.json](https://raw.githubusercontent.com/emmo-repo/domain-battery/master/context/context.json) and set `BATTERYGRAPH_CONTEXT=/path/to/context.json`.

## Quick start

```python
from batterygraph import BatteryGraph, GraphRAG

bg = BatteryGraph("BatteryTypeJson")
bg.query_cell_property("INR21700-50E", "RatedCapacity", manufacturer="Samsung SDI")
# [{'cell': 'Samsung SDI INR21700-50E', 'property': 'RatedCapacity', 'value': 4.9, 'unit': 'Ah'}]

bg.get_cell_info("LF280K")      # manufacturer, case, cathode material, linked publications

# SPARQL with readable EMMO terms in {braces}
bg.sparql("""
SELECT (COUNT(DISTINCT ?cell) AS ?n) WHERE {
    ?cell {hasPositiveElectrode}/{hasActiveMaterial} ?m . ?m a {LFP} .
}""")

rag = GraphRAG(bg, model="claude-sonnet-5")
rag.answer("Which battery has a higher rated capacity: the Saft VL 5U or the Lishen LR2170SA?")
```

## How GraphRAG works

1. The LLM receives the question, the graph structure, the property names and the manufacturer list, and writes calls to three helper functions (`query_cell_property`, `get_all_cell_properties`, `get_cell_info`) or, for questions across many cells, a SPARQL query with `{Term}` placeholders.
2. The output is run against the graph. Helper calls are parsed, not evaluated: only these three functions with literal arguments are executed, and SPARQL must be read-only (`SELECT`/`ASK`).
3. The LLM answers from the query result only. If the graph has no data, the answer should say so rather than guess.

## Evaluation

The benchmark (`evaluation/qa_dataset.csv`) covers single-property lookups, multi-property summaries, comparisons, case and chemistry questions, derived values (Wh, mAh) and negative controls (made-up cells, missing specifications). Each answer was graded against the reference answer by the answering model itself; whether an incorrect answer admits missing data was judged by `gemini-3.5-flash` for all runs (a few unparseable grades were also re-graded by `gemini-3.5-flash`).

| Model | Mode | Accuracy | Hallucination robustness |
|---|---|---|---|
| gemini-3.5-flash | GraphRAG | 0.81 | 0.66 |
| claude-sonnet-5 | GraphRAG | 0.79 | 0.24 |
| gpt-5.4 | GraphRAG | 0.76 | 0.54 |
| gemini-3.5-flash | LLM only | 0.42 | 0.01 |

*Accuracy* = correct answers / all questions. *Hallucination robustness* = answers that admit missing data ("I don't know") / incorrect answers.

Recreate the figures and `summary.csv` from the recorded results (no model calls):

```sh
python scripts/make_figures.py
```

Run the benchmark yourself:

```sh
python scripts/run_eval.py --check gemini-3.5-flash         # test API access
python scripts/run_eval.py --model claude-sonnet-5          # GraphRAG
python scripts/run_eval.py --model gemini-3.5-flash --no-rag   # LLM-only baseline
```

The recorded results were produced with an earlier version of the profiles and of the query prompt. A new run on the current data and code will give somewhat different numbers.

## Data

Each file in `BatteryTypeJson/` describes one cell as JSON-LD with the [EMMO battery domain context](https://w3id.org/emmo/domain/battery/context):

* `@type` `BatteryCell`, `schema:name` (model) and `schema:manufacturer` (with a Wikidata link where known)
* `hasProperty`: numerical properties such as `RatedCapacity`, `NominalVoltage`, `CycleLife` or `Mass`, each with its value, unit (where applicable) and a `schema:citation` of its source
* `hasCase`: case / form factor (e.g. `PrismaticCase`, `R21700`); `hasPositiveElectrode`/`hasActiveMaterial`: cathode chemistry
* `schema:subjectOf`: publications that mention the cell, identified by DOI only (3,930 links to 3,406 papers for 176 cells). `schema:additionalType` holds this project's classification of each link: `USED`, `REFERENCED` or `UNCLEAR` (154 links are unlabelled).

**Identifiers.** 358 cells have a persistent battinfo IRI (`https://w3id.org/battinfo/spec/…`) as `@id`. The other 24 are not yet registered there and carry a local UID, which JSON-LD resolves against the document URL.

## License

BSD 3-Clause License, see [LICENSE](LICENSE).
