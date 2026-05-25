---
name: github-models
description: GitHub Models playground and API
category: devops
tags: [github, models, ai, playground, api, copilot]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# GitHub Models

> Explore and integrate AI models through GitHub Models marketplace and playground.

## Quick Start
```python
# GitHub Models API — free tier with GitHub token
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=os.environ["GITHUB_TOKEN"]
)

# Available models: gpt-4o, gpt-4o-mini, mistral-large, llama-3.2-90b, cohere-command, etc.
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain GitHub Models in 2 sentences."}
    ],
    temperature=0.7,
    max_tokens=500
)
print(response.choices[0].message.content)

# List available models
models = client.models.list()
for model in models:
    print(f"- {model.id}")
```

```bash
# Direct API call with curl
curl -s -X POST "https://models.inference.ai.azure.com/chat/completions" \
  -H "Authorization: Bearer $GITHUB_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4o",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

## Key Concepts
GitHub Models provides free API access to multiple AI models using your GitHub token. Rate-limited but generous for development. Accessible through OpenAI-compatible API. Great for prototyping and comparison.

## When to Use
- Prototyping with multiple model providers without separate accounts
- Comparing model outputs for different use cases
- CI/CD pipelines that need AI integration
- Learning and experimentation (free tier)

## Validation
1. API responds with 200 and valid completion
2. Multiple models are accessible through the same endpoint
3. Token usage and rate limits are respected
