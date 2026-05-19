---
name: llama-index
description: Builds data-augmented LLM applications with LlamaIndex, including indexing, retrieval, and query engines.
category: ai
tags: [llamaindex, rag, llm, indexing, retrieval]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# LlamaIndex
> Data framework for building LLM applications with custom data.
## Quick Start
```python
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
documents = SimpleDirectoryReader('data').load_data()
index = VectorStoreIndex.from_documents(documents)
response = index.as_query_engine().query("What is the main topic?")
```
## Index Types
```python
from llama_index.core import VectorStoreIndex, SummaryIndex, KeywordTableIndex
vector_index = VectorStoreIndex.from_documents(docs)
summary_index = SummaryIndex.from_documents(docs)
keyword_index = KeywordTableIndex.from_documents(docs)
```
## When to Use
- Document Q&A; Custom knowledge bases; RAG pipelines
## Validation
1. Documents index successfully; 2. Query engines return relevant results; 3. Retrieval returns top-k nodes
