---
name: haystack
description: Builds NLP pipelines with Haystack for document search, QA, and LLM-powered applications.
category: ai
tags: [haystack, nlp, search, qa, pipelines]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Haystack
> NLP framework for building search and QA systems.
## Quick Start
```python
from haystack import Pipeline
from haystack.components.retrievers import InMemoryBM25Retriever
from haystack_integrations.components.generators import OpenAIGenerator
pipeline = Pipeline()
pipeline.add_component("retriever", InMemoryBM25Retriever(top_k=3))
pipeline.add_component("llm", OpenAIGenerator())
pipeline.connect("retriever.documents", "llm.documents")
result = pipeline.run({"retriever": {"query": "What is Haystack?"}})
```
## When to Use
- Document retrieval; QA over custom data; Hybrid search; NLP pipelines
## Validation
1. Pipeline compiles; 2. Retrieval returns relevant docs; 3. LLM generates context-based answers
