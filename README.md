# Cell Info Repository

Information about battery cells as structured, semantic, and linked data. This repository allows usage in knowledge graphs, websites, or Retrieval Augmented Generation.

## Installation

To install the required dependencies, use the `requirements.txt` file:

```sh
pip install -r requirements.txt
```

For using the GraphRAG notebook, either an OpenAI API key needs to be installed or a local Ollama server should be set up.

## Usage

Usage examples are provided in the following Jupyter notebooks:

- `CreateBatteryTypeJson.ipynb`: Instructions and examples on how to create battery type JSON files.
- `DemoKnowledgeGraph.ipynb`: Demonstrates how to build and query a knowledge graph using the provided battery cell data.
- `GraphRAG.ipynb`: Example of using Retrieval Augmented Generation with the battery cell data. Requires OpenAI API key or a local Ollama server.
- `VisualizeBatteryTypes.ipynb`: Instructions and examples for visualizing battery types using the provided data.

## File Descriptions

- **BatteryTypeJson/**: Contains various JSON files with detailed information about different battery cells.
    - Examples: `-_E78.json`, `A123_A123_20AH.json`, `CATL_100Ah_CATL_LiFePO4.json`, etc.

- **Sources/**: Contains source data files used in the notebooks.
    - `CellComparison.csv`
    - `TumDataBattINFO.csv`
    - `cell_product_list.csv`
    - `pg_doi.csv`
    - `pg_s2.csv`
    - `valid_hits.json`

- **VegaPlotsJson/**: Contains JSON files for Vega plots.
    - `RagoneLiterature.json`

- **CreateBatteryTypeJson.ipynb**: Notebook for creating battery type JSON files.

- **DemoKnowledgeGraph.ipynb**: Notebook demonstrating how to create and query a knowledge graph.

- **GraphRAG.ipynb**: Notebook demonstrating Retrieval Augmented Generation with battery cell data.

- **VisualizeBatteryTypes.ipynb**: Notebook for visualizing battery types.

- **requirements.txt**: List of required Python packages for the project.