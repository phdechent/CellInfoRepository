# Cell Info Repository

This repository contains battery-cell specifications as linked data and a GraphRAG workflow. The workflow answers questions about the cells from the knowledge graph. The repository supports the article [Demonstrating Linked Battery Data to Accelerate Knowledge Flow in Battery Science](https://doi.org/10.1016/j.electacta.2026.150404).

## Contents

```
BatteryTypeJson/    382 cell profiles (JSON-LD, EMMO battery ontology): properties with
                    their sources, case, cathode chemistry, DOIs of linked publications
batterygraph/       Python package: RDF graph, helper functions, GraphRAG
notebooks/          examples for SPARQL, the helper functions and GraphRAG
scripts/            question generation, evaluation, tables and figures
evaluation/         questions, reference answers and results
llm-wiki-2025-oa/   agentic literature review of 2025 open-access papers
```

## Installation

```sh
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and write your API keys into it. Local models through [Ollama](https://ollama.com) need no key.

## Quick start

```python
from batterygraph import BatteryGraph, GraphRAG

bg = BatteryGraph("BatteryTypeJson")
bg.query_cell_property("INR21700-50E", "RatedCapacity", manufacturer="Samsung SDI")
# [{'cell': 'Samsung SDI INR21700-50E', 'property': 'RatedCapacity', 'value': 4.9, 'unit': 'Ah'}]

rag = GraphRAG(bg, model="claude-sonnet-5")
rag.answer("Which battery has a higher rated capacity: the Saft VL 5U or the Lishen LR2170SA?")
```

## Evaluation

`evaluation/qa_dataset_v2.csv` contains 300 questions with reference answers. Three LLMs answered them with GraphRAG and four LLMs without it. One judge (`claude-opus-5-5`) graded all answers. `evaluation/results_rerun_2026-10/` contains a record of each step.

Correct answers of 300, as in the article:

| Model | GraphRAG | LLM only |
|---|---|---|
| gemini-3.8-flash | 300 | 138 |
| claude-sonnet-5-5 | 300 | 102 |
| gpt-6.1-sol | 299 | 145 |
| claude-opus-5-5 | – | 141 |

To run the evaluation again with the same settings:

```sh
python scripts/rerun_eval_logged.py --out evaluation/new_run \
    --rag gemini-3.8-flash claude-sonnet-5-5 gpt-6.1-sol \
    --no-rag gemini-3.8-flash claude-sonnet-5-5 claude-opus-5-5 gpt-6.1-sol \
    --judge claude-opus-5-5 --grader-prompt with_question \
    --caps openai=3.6 gemini=8.0 anthropic=16.6
python scripts/analyze_rerun.py evaluation/new_run
```

`evaluation/results/` contains the results of an earlier evaluation (`scripts/run_eval.py`).

## How to cite

Cite the article and the archived version of this repository on Zenodo. [CITATION.cff](CITATION.cff) contains the citation data.

> P. Dechent, E. Barbers, S. Clark, S. Lehner, B. Planden, M. Adachi, D. U. Sauer, D. A. Howey, S. Paarmann: Demonstrating Linked Battery Data to Accelerate Knowledge Flow in Battery Science. Electrochimica Acta (2026) 150404. [doi:10.1016/j.electacta.2026.150404](https://doi.org/10.1016/j.electacta.2026.150404)

## License

BSD 3-Clause License, see [LICENSE](LICENSE).
