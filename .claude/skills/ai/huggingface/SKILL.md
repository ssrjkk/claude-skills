---
name: huggingface
description: Loads, fine-tunes, and deploys models from HuggingFace Hub for NLP, CV, and audio tasks.
category: ai
tags: [huggingface, transformers, nlp, fine-tuning, llm]
models: [opus]
version: 1.0.0
created: 2026-05-14
---
# HuggingFace

> Load, fine-tune, and deploy models from HuggingFace Hub.

## Quick Start
```python
from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer
from datasets import load_dataset

# Use pre-trained pipeline
classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
result = classifier("I love HuggingFace!")
print(result)

# Fine-tune
model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=2)
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
dataset = load_dataset("imdb")
```

## When to Use
- ✅ NLP tasks (classification, summarization, translation)
- ✅ Fine-tuning open-source LLMs
- ❌ Not for production GPU inference (better use dedicated infra)

## Step-by-Step Instructions
1. Install: `pip install transformers datasets accelerate`
2. Load pre-trained model from Hub
3. Prepare dataset with tokenizer
4. Fine-tune with Trainer API

## Dependencies
```bash
pip install transformers datasets torch accelerate
```

## Examples
Input: "This product is amazing!" → Output: `[{"label": "POSITIVE", "score": 0.99}]`

## Resources
- [HuggingFace Docs](https://huggingface.co/docs)
- [Examples](./examples/)

## Validation
1. Model loads without errors
2. Inference returns expected output
3. Training loss decreases over epochs
