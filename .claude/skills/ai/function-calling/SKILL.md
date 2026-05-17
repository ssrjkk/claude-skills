---
name: function-calling
description: Designs prompts and schemas for LLM function calling and tool use, enabling structured interactions with external APIs and services.
category: ai
tags: [prompt, function-calling, tools, api, structured]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Function Calling

> Prompt patterns for LLM tool use and external API integration.

## Quick Start
```
Available functions:
- get_weather(city: string, unit: "celsius"|"fahrenheit"): object
- get_timezone(city: string): string
- send_email(to: string, subject: string, body: string): boolean

Determine which function to call based on the user request.
Respond with: {"function": "name", "args": {...}}
```

## When to Use
- Building AI assistants with tool access
- API orchestration through LLM
- Database query generation
- Multi-step agent workflows

## Techniques

### Function Declaration
Describe each function with name, parameters, types and descriptions.

### Parameter Extraction
Guide the model to extract arguments from user input.

### Chaining
Chain multiple function calls for complex workflows.

### Error Recovery
Handle cases where arguments are missing or invalid.

## Dependencies
```python
# OpenAI-style function calling
response = client.chat.completions.create(
  model="gpt-4o",
  messages=messages,
  tools=tool_definitions
)
```

## Examples
```json
{
  "name": "search_flights",
  "description": "Search for available flights",
  "parameters": {
    "origin": {"type": "string"},
    "destination": {"type": "string"},
    "date": {"type": "string", "format": "date"}
  }
}
```

## Resources
- [OpenAI Function Calling](https://platform.openai.com/docs/guides/function-calling)
- [Anthropic Tool Use](https://docs.anthropic.com/claude/docs/tool-use)

## Validation
1. Correct function selected for each request
2. All required parameters are extracted
3. Invalid requests are handled gracefully
4. Multi-turn tool use maintains context
