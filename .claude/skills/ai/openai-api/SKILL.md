---
name: openai-api
description: "Integrates OpenAI API for chat completions, embeddings, and function calling in applications. Use for adding LLM capabilities."
category: ai
tags: [openai, gpt, api, llm, embeddings]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# OpenAI API

> Integrate GPT models and embeddings into your applications.

## Quick Start
```python
from openai import OpenAI

client = OpenAI()
response = client.chat.completions.create(
  model="gpt-4o",
  messages=[{"role": "user", "content": "Hello!"}]
)
print(response.choices[0].message.content)
```

## When to Use
- Chat applications and assistants
- Content generation
- Embeddings for search
- Function calling and tool use

## Step-by-Step
1. Install: `pip install openai`
2. Set `OPENAI_API_KEY` environment variable
3. Use chat completions or embeddings
4. Handle streaming responses

## Dependencies
```bash
pip install openai
export OPENAI_API_KEY=sk-...
```

## Examples
```python
stream = client.chat.completions.create(
  model="gpt-4o",
  messages=[{"role": "user", "content": "Tell me a story"}],
  stream=True
)
for chunk in stream:
  print(chunk.choices[0].delta.content or "", end="")
```

## Resources
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference)

## Validation
1. API key authenticates
2. Chat completion returns response
3. Streaming works correctly
