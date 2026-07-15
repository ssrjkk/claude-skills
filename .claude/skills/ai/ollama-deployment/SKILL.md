---
name: ollama-deployment
description: "Local LLM deployment with Ollama"
category: ai
tags: [ollama, local-llm, deployment, docker, inference]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Ollama Deployment

> Run and deploy open-source LLMs locally with Ollama for private, cost-effective inference.

## Quick Start
```bash
# Install Ollama (Linux/macOS)
curl -fsSL https://ollama.com/install.sh | sh

# Windows: download from ollama.com

# Pull and run a model
ollama pull llama3.2:3b
ollama run llama3.2:3b "What is the capital of France?"

# Run with custom parameters
ollama run llama3.2:3b --temperature 0.7 --top-p 0.9

# Server mode (API)
ollama serve

# API usage
curl http://localhost:11434/api/generate -d '{
  "model": "llama3.2:3b",
  "prompt": "Write a haiku about programming",
  "stream": false
}'
```

```python
# Python client
import requests

def query_ollama(prompt: str, model: str = "llama3.2:3b") -> str:
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": model, "prompt": prompt, "stream": False}
    )
    return response.json()["response"]

print(query_ollama("Explain quantum computing in 3 sentences"))
```

## Key Concepts
Ollama provides a local API-compatible endpoint for open-source models. Supports GGUF quantization, model customization with Modelfiles, concurrent requests, and GPU acceleration.

## When to Use
- Privacy-sensitive applications (no data leaves your machine)
- Offline/air-gapped environments
- Cost-sensitive deployments at scale
- Development and testing before deploying to cloud

## Validation
1. `ollama list` shows downloaded models
2. API endpoint responds on port 11434
3. Model generates coherent responses with reasonable latency
4. Multiple concurrent requests are handled correctly
