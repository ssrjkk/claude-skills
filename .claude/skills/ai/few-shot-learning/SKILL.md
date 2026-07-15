---
name: few-shot-learning
description: "Designs and curates few-shot examples to guide LLM behavior, including example selection, formatting, and ordering. Use for task specification without fine-tuning."
category: ai
tags: [prompt, few-shot, examples, in-context-learning, llm]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Few-Shot Learning

> Guiding LLM behavior through carefully curated examples.

## Quick Start
```
Classify the sentiment of each review:

Review: "This product is amazing!"
Sentiment: Positive

Review: "Terrible experience, would not recommend."
Sentiment: Negative

Review: "It's okay, nothing special."
Sentiment: Neutral

Review: "Best purchase I've made all year!"
Sentiment:
```

## When to Use
- Teaching new tasks without fine-tuning
- Specifying output format by example
- Handling edge cases
- Setting response tone and style

## Best Practices

### Example Selection
- Cover edge cases and boundary conditions
- Include 3-5 diverse examples
- Show both positive and negative cases
- Order from simple to complex

### Formatting
- Use consistent separator between examples
- Clearly mark input vs output boundaries
- Keep format identical to expected real use

### Dynamic Selection
- For large datasets: retrieve most similar examples
- Use embedding similarity for example selection
- Limit to context window constraints

## Dependencies
```bash
pip install openai
# For dynamic selection: pip install sentence-transformers
```

## Examples
```
Translate English to French:

English: "Hello"
French: "Bonjour"

English: "Good morning"
French: "Bonjour"

English: "Thank you"
French: "Merci"

English: "How are you?"
French:
```

## Resources
- [OpenAI Few-Shot Guide](https://platform.openai.com/docs/guides/prompt-engineering)

## Validation
1. Model follows example patterns consistently
2. Edge cases handled correctly
3. Adding more examples improves accuracy
4. Format matches examples exactly
