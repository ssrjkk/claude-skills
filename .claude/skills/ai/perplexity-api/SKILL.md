---
name: perplexity-api
description: Integrates Perplexity AI's online LLM API for web-connected search and generation with real-time information.
category: ai
tags: [perplexity, api, search, llm, online]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Perplexity API
> Online LLM API with real-time web search capabilities.
## Quick Start
```python
import requests
response = requests.post("https://api.perplexity.ai/chat/completions", json={
  "model": "sonar-pro",
  "messages": [{"role": "user", "content": "What is the latest news about AI?"}]
}, headers={"Authorization": "Bearer YOUR_API_KEY", "Content-Type": "application/json"})
print(response.json()["choices"][0]["message"]["content"])
```
## When to Use
- Real-time web-connected Q&A; Research assistance; Current events; Factual queries
## Validation
1. API key authenticates; 2. Responses include citations; 3. Web search returns current info
