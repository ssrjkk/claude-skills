---
name: structured-output
description: Guides LLMs to produce structured, schema-validated JSON output with type safety and format constraints. Use for programmatic LLM integration.
category: ai
tags: [prompt, json, structured-output, schema, parsing]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Structured Output

> Getting reliable, schema-validated JSON from LLMs.

## Quick Start
```
Extract the following information as JSON:
"John Doe, 28 years old, john@example.com, lives in New York"

Respond ONLY with valid JSON:
{
  "name": "John Doe",
  "age": 28,
  "email": "john@example.com",
  "city": "New York",
  "is_adult": true
}
```

## When to Use
- API integrations requiring typed data
- Database record generation
- Form filling and data extraction
- Function calling / tool use

## Techniques

### Schema Definition
Define the exact JSON schema in the prompt with types and constraints.

### Format Enforcement
Use "Respond ONLY with valid JSON" to prevent extra text.

### Type Coercion
Specify exact types (string, number, boolean, array, null) for each field.

### Error Handling
Request JSON wrapped in JSON code blocks for safe parsing.

## Dependencies
```python
import json
# Use json.loads() with try/except for safety
```

## Examples
Input: "Extract product info: Apple MacBook Pro 2023, $2499, in stock"
```json
{
  "product": "MacBook Pro",
  "brand": "Apple",
  "year": 2023,
  "price": 2499.99,
  "currency": "USD",
  "in_stock": true
}
```

## Resources
- [JSON Schema](https://json-schema.org)

## Validation
1. Output is always valid JSON
2. All required keys are present
3. Values match specified types
4. JSON.parse() succeeds without errors
