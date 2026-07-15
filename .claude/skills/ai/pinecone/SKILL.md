---
name: pinecone
description: "Manages vector embeddings with Pinecone for semantic search, recommendation, and RAG pipelines."
category: ai
tags: [pinecone, vector-database, embeddings, search, rag]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Pinecone
> Managed vector database for semantic search and RAG.
## Quick Start
```python
from pinecone import Pinecone, ServerlessSpec
pc = Pinecone(api_key="YOUR_API_KEY")
pc.create_index(name="my-index", dimension=384, metric="cosine", spec=ServerlessSpec(cloud="aws", region="us-east-1"))
```
## Indexing & Query
```python
index = pc.Index("my-index")
index.upsert(vectors=[{"id": "doc1", "values": [0.1, 0.2], "metadata": {"text": "Document 1"}}])
results = index.query(vector=query_embedding, top_k=5, include_metadata=True)
```
## When to Use
- Semantic search; RAG vector storage; Recommendation systems
## Validation
1. Index creation succeeds; 2. Upsert operations complete; 3. Query returns relevant results
