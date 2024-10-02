# Cell Info Repository

Information about battery cells as structured, semantic, and linked data. This repository allows usage in knowledge graphs, websites, or Retrieval Augmented Generation.

## Installation

To install the required dependencies, use the `requirements.txt` file:

```sh
pip install -r requirements.txt
```

For using the GraphRAG notebook, either an OpenAI API key needs to be provided (see https://platform.openai.com/docs/quickstart) or a local Ollama server should be set up (see https://github.com/ollama/ollama/).

## Usage

Usage examples are provided in the following Jupyter notebooks:

- `CreateBatteryTypeJson.ipynb`: Instructions and examples on how to create battery type JSON files.
- `DemoKnowledgeGraph.ipynb`: Demonstrates how to build and query a knowledge graph using the provided battery cell data.
- `GraphRAG.ipynb`: Example of using Retrieval Augmented Generation with the battery cell data. Requires OpenAI API key or a local Ollama server.

## File Descriptions

- **BatteryTypeJson/**: Contains various JSON files with detailed information about different battery cells.
    - Examples: `A123_A123_20AH.json`, `CATL_100Ah_CATL_LiFePO4.json`, etc.

- **Sources/**: Contains source data files used in the notebooks.
    - `CellComparison.csv`
    - `TumDataBattINFO.csv`
    - `cell_product_list.csv`


- **CreateBatteryTypeJson.ipynb**: Notebook for creating battery type JSON files.

- **DemoKnowledgeGraph.ipynb**: Notebook demonstrating how to create and query a knowledge graph.

- **GraphRAG.ipynb**: Notebook demonstrating Retrieval Augmented Generation with battery cell data.

- **requirements.txt**: List of required Python packages for the project.