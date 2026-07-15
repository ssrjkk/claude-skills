---
name: prompt-compression
description: "Reduces prompt token usage through compression techniques, summarization, and selective context inclusion while maintaining output quality. Use for cost optimization."
category: ai
tags: [prompt, compression, tokens, optimization, cost]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Prompt Compression

> Reduce token usage while preserving prompt effectiveness.

## Quick Start
```
Before (150 tokens):
"Please analyze the following customer feedback and provide
a detailed summary of the main complaints, positive points,
and suggestions for improvement. The feedback is from our
quarterly survey of 500 users across North America and Europe."

After (40 tokens):
"Analyze this customer feedback. Summarize complaints,
positive points, and improvement suggestions."
```

## When to Use
- Cost-sensitive production systems
- Long context window limits
- Batch processing with many requests
- Mobile or edge deployments

## Techniques

### Instruction Compression
Remove unnecessary words (please, could you, let's).

### Few-Shot Deduplication
Use one example per pattern type instead of multiple.

### Context Summarization
Pre-summarize retrieved documents before including.

### Selective Inclusion
Only include the most relevant context chunks.

### Abbreviation Mapping
Define short codes for repeated concepts.

## Dependencies
```bash
pip install llmlingua  # specialized prompt compression
```

## Examples
```
Instead of:
"For each of the following three customer reviews, classify
the sentiment as either positive, negative, or neutral.
Provide your reasoning for each classification."

Use:
"Classify sentiment (positive/negative/neutral) for each review.
Show reasoning."
Reduction: ~40% tokens
```

## Resources
- [LLMLingua Paper](https://arxiv.org/abs/2310.05736)
- [Anthropic Prompt Optimization](https://docs.anthropic.com/claude/docs/prompt-optimization)

## Validation
1. Output quality maintained after compression
2. Compression ratio measurable (>20% reduction)
3. Critical instructions not lost
4. Compare before/after on test suite
