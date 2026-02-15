# LangChain Basic Agent (Taller04-Parte2)

## Overview

This project demonstrates a minimal LangChain agent that can call a simple tool (`get_weather`) and respond to a user message.

## Prerequisites

- Python 3.13+
- VS Code (recommended)

## Setup

### 1) Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2) Install dependencies

```bash
python -m pip install langchain langchain-anthropic
```

### 3) Run the script

```bash
python basic_agent.py
```

## Expected Output

- The agent should return a response to the user message.
- The `get_weather("Bogotá")` call should print:

```
It's always sunny in Bogotá!
```

## Notes

- The `get_weather` tool returns a fixed string, so it always returns the same response.
- To get real weather data, integrate a weather API and update `get_weather`.

## Troubleshooting

- If you see `externally-managed-environment`, use a virtual environment as shown above.
- If you see `ModuleNotFoundError: langchain_anthropic`, install it with:

```bash
python -m pip install langchain-anthropic
```

## RAG Process (Step-by-Step)

1) Documents: a small list of text snippets (`DOCS`) is the knowledge base.
2) Splitting: the text is chunked with `RecursiveCharacterTextSplitter`.
3) Embeddings: each chunk is turned into vectors using `HuggingFaceEmbeddings`.
4) Vector store: chunks are stored in FAISS for similarity search.
5) Retrieval: the retriever fetches the top-k relevant chunks for the question.
6) Prompting: retrieved chunks are injected into the prompt template.
7) Generation: the Anthropic model generates a grounded answer.

## RAG Output Explanation

When running `rag_agent.py`, you may see:

- A deprecation warning about `HuggingFaceEmbeddings`. The script still works, but the class has moved to `langchain-huggingface`.
- Model download logs the first time the embedding model is loaded (for example, `model.safetensors`, `tokenizer.json`).
- The final answer produced by the LLM, grounded in the retrieved context.
