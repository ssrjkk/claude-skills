---
name: prompt-engineering
description: Advanced prompt engineering patterns
category: ai
tags: [prompt-engineering, llm, patterns, techniques]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Prompt Engineering

> Master advanced prompt engineering patterns for reliable, structured LLM outputs.

## Quick Start
```markdown
# Advanced Prompt Patterns

## Chain-of-Thought (CoT)
```
Solve this step by step:
1. First, identify what we know
2. Break down the problem
3. Work through each part
4. Verify the answer

Question: {question}
```

## Few-Shot with Format Control
```
Extract structured data from text.
Examples:
Input: "Order #1234: 2x Widget A ($9.99 each) shipped to NYC"
Output: {"order_id": "1234", "items": [{"name": "Widget A", "qty": 2, "price": 9.99}], "shipping": "NYC"}

Input: "{input}"
Output:
```

## Role-Persona-Format (RPF)
```
Act as a senior {role} at {company}.
{context}
Format your response as:
## Summary
## Analysis
## Recommendations
## Risk Assessment
```

## Reflexion — Self-Correction
```
Generate a solution. Then review your solution for errors.
If you find issues, produce a corrected version.
Label each attempt as [ATTEMPT 1], [ATTEMPT 2], etc.
```
```

## Key Concepts
Structure, specificity, and iteration are key. Use delimiters, format constraints, and role assignments. Chain-of-thought improves reasoning. Self-correction loops catch errors. Structured outputs enable reliable parsing.

## When to Use
- Generating structured data for programmatic consumption
- Complex reasoning tasks requiring step-by-step thought
- Tasks where output format consistency is critical

## Validation
1. Prompt produces consistent, parseable outputs
2. CoT prompts show correct reasoning before answers
3. Edge cases (empty input, extreme values) handled gracefully
