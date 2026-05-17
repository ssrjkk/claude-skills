---
name: prompt-testing
description: Tests and evaluates prompt quality using systematic methods, A/B testing, regression suites, and automated evaluation with LLM-as-judge. Use for prompt optimization.
category: ai
tags: [prompt, testing, evaluation, llm-as-judge, ab-testing]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Prompt Testing

> Systematic evaluation and iteration of prompts.

## Quick Start
1. Define ground truth for 10-20 test cases
2. Run prompt against all cases
3. Score each response (correct/partial/incorrect)
4. Iterate prompt based on failure patterns
5. Re-run to measure improvement

## When to Use
- Before deploying prompts to production
- Comparing prompt variants (A/B testing)
- Regression testing prompt changes
- Evaluating model upgrades

## Methods

### Manual Evaluation
Human review of a sample of outputs against criteria.

### LLM-as-Judge
Use a strong model (Opus, GPT-4) to rate outputs.

### Test Suite
Maintain a set of inputs with expected outputs.

### A/B Testing
Compare two prompt versions on the same inputs.

## Dependencies
```bash
pip install pytest
```

## Examples
```
Evaluation Criteria:
1. Correctness (0-5): Is the answer factually correct?
2. Format (0-3): Does output follow specified format?
3. Completeness (0-3): Are all requested elements present?

Prompt: "Extract date, amount, and vendor from invoice text"
```

## Resources
- [Anthropic Eval Tools](https://docs.anthropic.com/claude/docs/evaluation-tools)

## Validation
1. Test suite covers all major input types
2. Score improves with each prompt iteration
3. Edge cases are documented and tested
4. Regression prevents previously fixed issues
