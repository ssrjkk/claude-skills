---
name: prompt-chaining
description: "Multi-step prompt chaining strategies"
category: ai
tags: [prompt-chaining, workflow, llm, multi-step]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Prompt Chaining

> Decompose complex tasks into sequential LLM calls for more reliable and auditable results.

## Quick Start
```python
from anthropic import Anthropic

client = Anthropic()

def analyze_document(text: str) -> dict:
    # Step 1: Extract key information
    step1 = client.messages.create(
        model="claude-sonnet-4-20250514",
        messages=[{"role": "user", "content": f"""Extract structured data from this document:
Document: {text}

Output format:
- title: str
- date: str  
- key_points: list[str]
- entities: list[{{name: str, type: str}}]"""}],
        max_tokens=1000
    )
    extracted = parse_json(step1.content[0].text)

    # Step 2: Generate summary
    step2 = client.messages.create(
        model="claude-sonnet-4-20250514",
        messages=[{"role": "user", "content": f"""Summarize this document in 3 sentences:

Title: {extracted['title']}
Key points: {', '.join(extracted['key_points'])}"""}],
        max_tokens=500
    )
    extracted["summary"] = step2.content[0].text

    # Step 3: Classify and tag
    step3 = client.messages.create(
        model="claude-sonnet-4-20250514",
        messages=[{"role": "user", "content": f"""Classify this document:
Title: {extracted['title']}
Summary: {extracted['summary']}

Categories: [technical, business, legal, personal]
Tone: [positive, negative, neutral]
Urgency: [high, medium, low]

Output JSON only."""}],
        max_tokens=200
    )
    extracted.update(parse_json(step3.content[0].text))
    return extracted
```

## Key Concepts
Chaining splits complex tasks into focused steps. Each step has a clear input/output contract. Benefits: better accuracy per step, easier debugging, intermediate results are auditable, and each step can use different prompts/models.

## When to Use
- Document processing pipelines (extract → summarize → classify)
- Multi-stage content generation (outline → draft → polish → format)
- Complex analysis (gather data → analyze → recommend → summarize)

## Validation
1. Each step's output is valid input for the next step
2. Error recovery at each step (retry, skip, default)
3. Final output quality exceeds single-prompt approach
