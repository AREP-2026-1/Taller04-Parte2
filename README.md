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