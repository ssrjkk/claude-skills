---
name: vector-db-rag
description: "Builds RAG pipelines with vector databases (Chroma, Pinecone) and embedding models. Use for semantic search and LLM applications."
category: data
tags: [rag, vector-db, embeddings, llm, semantic-search]
models: [opus]
version: 1.0.0
created: 2026-04-29
---
# Vector DB RAG

> RAG pipelines with vector databases and LLMs for semantic search.

## Quick Start
```python
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

# Create vector DB
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
db = Chroma.from_documents(documents, embeddings)

# Semantic search
docs = db.similarity_search("query about documents")
```

## When to Use
- ✅ Semantic search over documents
- ✅ RAG architecture for LLM
- ❌ Not for exact ID lookup

## Step-by-Step Instructions
1. Prepare documents and split into chunks
2. Create embeddings via OpenAI/Cohere
3. Store in vector DB (Chroma/Pinecone)
4. Setup retrieval for LLM

## Dependencies
```bash
pip install langchain langchain-chroma langchain-openai
```

## Examples
Input: "How to use FastAPI?" → Output: Relevant document fragments

## Resources
- [LangChain Docs](https://python.langchain.com/)
- [Examples](./examples/)

## Validation
1. Vectors created correctly
2. Search returns relevant results
3. RAG pipeline works end-to-end
