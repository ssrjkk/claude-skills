---
name: model-evaluation
description: LLM evaluation and benchmarking
category: ai
tags: [evaluation, benchmarking, llm, testing, metrics]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Model Evaluation

> Systematically evaluate LLM performance with benchmarks, metrics, and continuous testing.

## Quick Start
```python
from datasets import load_dataset
from anthropic import Anthropic
import json

client = Anthropic()

def evaluate_model(dataset_name: str = "mmlu/abstract_algebra") -> dict:
    dataset = load_dataset(dataset_name, split="test")
    results = {"correct": 0, "total": 0, "by_category": {}}

    for item in dataset.select(range(100)):
        prompt = f"""Question: {item['question']}

Options:
{chr(10).join(f'{k}: {v}' for k, v in item['choices'].items())}

Answer with the letter only."""
        
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=10
        )
        
        predicted = response.content[0].text.strip()
        correct = predicted == item['answer']
        results["total"] += 1
        if correct:
            results["correct"] += 1

    results["accuracy"] = round(results["correct"] / results["total"], 4)
    return results

# Run evaluation
scores = evaluate_model()
print(f"Accuracy: {scores['accuracy']:.2%}")
```

## Key Concepts
Track accuracy, F1, BLEU, ROUGE, and task-specific metrics. Use standardized benchmarks (MMLU, HumanEval, GSM8K). Implement regression testing — compare against baselines when changing prompts or models.

## When to Use
- Comparing model providers or versions for your use case
- Validating prompt changes with quantitative metrics
- Monitoring production LLM performance over time
- Building test suites for LLM-powered features

## Validation
1. Evaluation runs on a representative test set
2. Results are statistically significant (adequate sample size)
3. Scoring is reproducible across runs
4. Performance regression alerts trigger on degradation
