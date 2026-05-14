---
name: ollama
description: Runs large language models locally with Ollama, including model management, custom Modelfiles, and API integration. Use for private, offline LLM inference.
category: ai
tags: [ollama, llm, local, offline, llama]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Ollama

> Run LLMs locally with simple commands and a REST API.

## Quick Start
```bash
ollama pull llama3.2
ollama run llama3.2 "What is the capital of France?"
```

## When to Use
- Private/local LLM inference
- Offline AI applications
- Testing models without API costs
- Custom fine-tuned models

## Step-by-Step
1. Install Ollama from ollama.com
2. Pull a model: `ollama pull llama3.2`
3. Run interactively or via API
4. Create custom Modelfiles

## Dependencies
```bash
# Install from https://ollama.com
ollama pull llama3.2:3b
```

## Examples
```python
import requests
response = requests.post("http://localhost:11434/api/generate", json={
  "model": "llama3.2",
  "prompt": "Why is the sky blue?",
  "stream": False
})
print(response.json()["response"])
```

## Resources
- [Ollama GitHub](https://github.com/ollama/ollama)

## Validation
1. Ollama service is running
2. Model pulls and runs successfully
3. API returns responses at localhost:11434
