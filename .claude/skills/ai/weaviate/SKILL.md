---
name: weaviate
description: "Deploys Weaviate vector database with hybrid search, modules, and GraphQL API."
category: ai
tags: [weaviate, vector-database, search, graphql, ai]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Weaviate
> Open-source vector database with hybrid search and GraphQL API.
## Quick Start
```python
import weaviate
client = weaviate.connect_to_local()
client.collections.create("Document", vectorizer_config=weaviate.classes.config.Configure.Vectorizer.text2vec_openai())
```
## Hybrid Search
```python
collection = client.collections.get("Document")
response = collection.query.hybrid(query="machine learning basics", alpha=0.5, limit=5)
```
## When to Use
- Hybrid search applications; AI-native data management; Knowledge graphs
## Validation
1. Weaviate instance starts; 2. Vectorizer module loads; 3. Hybrid search returns combined results
