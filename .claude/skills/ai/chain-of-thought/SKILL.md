---
name: chain-of-thought
description: "Implements step-by-step reasoning with Chain-of-Thought, Tree-of-Thought, and self-consistency techniques. Use for complex multi-step problems."
category: ai
tags: [prompt, reasoning, chain-of-thought, step-by-step, llm]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Chain-of-Thought

> Step-by-step reasoning techniques for complex problem-solving.

## Quick Start
```
Solve step by step:
A store has 120 apples. They sell 1/3 of them in the morning,
then 1/4 of the remaining in the afternoon. How many are left?

Step 1: Morning sales = 120 * 1/3 = 40 apples
Step 2: Remaining after morning = 120 - 40 = 80 apples
Step 3: Afternoon sales = 80 * 1/4 = 20 apples
Step 4: Final remaining = 80 - 20 = 60 apples
Answer: 60
```

## When to Use
- Math and logic problems
- Multi-step reasoning tasks
- Decision trees and planning
- Complex analysis with verification

## Techniques

### Chain-of-Thought (CoT)
Ask the model to reason step by step before answering.

### Tree-of-Thought (ToT)
Explore multiple reasoning branches in parallel, then evaluate.

### Self-Consistency
Generate multiple CoT paths, take majority vote as final answer.

### Least-to-Most
Break a complex problem into simpler sub-problems, solve sequentially.

## Dependencies
No additional libraries needed — works with any LLM chat interface.

## Examples
```
Q: If 5 workers can build a wall in 12 days,
how many days would 8 workers take?

Step 1: Find worker-days needed: 5 * 12 = 60 worker-days
Step 2: Divide by new workers: 60 / 8 = 7.5 days
Answer: 7.5 days
```

## Resources
- [Chain-of-Thought Paper (Wei et al.)](https://arxiv.org/abs/2201.11903)
- [Tree-of-Thought Paper (Yao et al.)](https://arxiv.org/abs/2305.10601)

## Validation
1. Model shows intermediate reasoning steps
2. Final answer is correct given the steps
3. Self-consistency improves accuracy across runs
