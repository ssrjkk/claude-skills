---
name: embedding-chunking
description: Splits documents into chunks and creates embeddings for semantic search. Use in RAG pipelines.
category: ai
tags: [embeddings, chunking, rag, semantic-search]
models: [sonnet, opus]
version: 1.0.0
created: 2026-04-29
---
# Embedding & Chunking

> Optimal text splitting and vector representation creation.

## Quick Start
```python
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = text_splitter.split_text(long_document)

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
vectors = [embeddings.embed_query(chunk) for chunk in chunks]
```

## When to Use
- ✅ Preparing documents for RAG
- ✅ Semantic search over text
- ❌ Not for short queries

## Step-by-Step Instructions
1. Choose chunking strategy (fixed, semantic, recursive)
2. Configure chunk size and overlap
3. Generate embeddings via API
4. Store in vector database

## Dependencies
```bash
pip install langchain-text-splitters langchain-openai tiktoken
```

## Examples
Input: 10000 character document → Output: 20 chunks of 500 chars with embeddings

## Resources
- [OpenAI Embeddings](https://platform.openai.com/docs/guides/embeddings)
- [Examples](./examples/)

## Validation
1. Chunks don't lose context at boundaries
2. Embeddings have expected dimensionality
3. Search returns relevant chunks
