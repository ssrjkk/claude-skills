---
name: llm-eval
description: "Evaluates LLM performance using BLEU, ROUGE metrics and LLM-as-judge. Use for model testing."
category: ai
tags: [llm, evaluation, metrics, bleu, rouge]
models: [opus]
version: 1.0.0
created: 2026-04-29
---
# LLM Evaluation

> Evaluate LLM response quality with automatic metrics and LLM-as-judge.

## Quick Start
```python
from rouge import Rouge

def evaluate_summary(reference, candidate):
    rouge = Rouge()
    scores = rouge.get_scores(candidate, reference)
    return scores[0]['rouge-l']['f']
```

## When to Use
- ✅ Testing LLM quality
- ✅ Comparing different models
- ❌ Not for evaluating classifier accuracy

## Step-by-Step Instructions
1. Prepare test dataset with reference answers
2. Generate responses with model under test
3. Calculate metrics (BLEU, ROUGE, BERTScore)
4. Conduct LLM-as-judge evaluation

## Dependencies
```bash
pip install rouge-score bert-score openai
```

## Examples
Input: reference="Hello", candidate="Hello!" → Output: ROUGE-L F1 = 0.95

## Resources
- [BLEU Score](https://en.wikipedia.org/wiki/BLEU)
- [Examples](./examples/)

## Validation
1. Metrics calculated correctly
2. High correlation with human judgment
3. Reports generated automatically
