---
name: prompt-engineering
description: Optimizes prompts for LLMs with few-shot, chain-of-thought, and structured output techniques. Use for improving response quality.
category: ai
tags: [prompt, llm, engineering, few-shot, chain-of-thought]
models: [opus]
version: 1.0.0
created: 2026-04-29
---
# Prompt Engineering

> Techniques for writing effective LLM prompts.

## Quick Start
```
# Few-shot prompting
Examples:
Q: 2+2=? A: 4
Q: 3+5=? A: 8
Q: 10+7=? A:

# Chain-of-Thought
Solve step by step:
1. Analyze input data
2. Extract key facts
3. Formulate answer
```

## When to Use
- ✅ Improving LLM response quality
- ✅ Need structured generation
- ❌ Not for simple one-step tasks

## Step-by-Step Instructions
1. Define task and desired output format
2. Add examples (few-shot) if needed
3. Use CoT for complex reasoning
4. Test with different models

## Dependencies
```bash
pip install openai anthropic
```

## Examples
Input: "Classify: Great service!" with sentiment prompt
Output: `{"sentiment": "positive", "confidence": 0.95}`

## Resources
- [OpenAI Prompt Engineering](https://platform.openai.com/docs/guides/prompt-engineering)
- [Examples](./examples/)

## Validation
1. Responses match specified format
2. Quality higher than baseline prompt
3. Model follows instructions consistently
