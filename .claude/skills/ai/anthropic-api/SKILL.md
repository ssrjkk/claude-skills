---
name: anthropic-api
description: Integrates Anthropic's Claude API for chat completions, messages, and tool use in applications.
category: ai
tags: [anthropic, claude, api, llm, messages]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Anthropic API
> Build applications with Claude's Messages API and tool use.
## Quick Start
```python
from anthropic import Anthropic
client = Anthropic()
response = client.messages.create(model="claude-sonnet-4-20250514", max_tokens=1024, messages=[{"role": "user", "content": "Hello!"}])
print(response.content[0].text)
```
## Messages with System Prompt
```python
response = client.messages.create(model="claude-sonnet-4-20250514", max_tokens=1024, system="You are a helpful coding assistant.", messages=[{"role": "user", "content": "Write a Python function to sort a list"}])
```
## Tool Use
```python
tools = [{"name": "get_weather", "description": "Get current weather", "input_schema": {"type": "object", "properties": {"location": {"type": "string"}, "unit": {"type": "string", "enum": ["c", "f"]}}, "required": ["location"]}}]
response = client.messages.create(model="claude-sonnet-4-20250514", max_tokens=1024, messages=[...], tools=tools)
```
## When to Use
- Building with Claude models; Tool-use agents; Multi-turn conversations
## Validation
1. API key authenticates; 2. Messages API returns completions; 3. Tool use requests are properly formatted
