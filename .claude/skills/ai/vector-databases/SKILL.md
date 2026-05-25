---
name: vector-databases
description: Vector database integration (Pinecone, Weaviate, Qdrant)
category: ai
tags: [vector-db, pinecone, weaviate, qdrant, embeddings, search]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Vector Databases

> Integrate vector databases for scalable semantic search and RAG pipelines.

## Quick Start
```python
# Pinecone
from pinecone import Pinecone, ServerlessSpec

pc = Pinecone(api_key="your-api-key")
index = pc.Index("my-docs")

# Upsert vectors
index.upsert(vectors=[
    {"id": "doc1", "values": [0.1]*1536, "metadata": {"title": "Introduction to AI"}},
    {"id": "doc2", "values": [0.2]*1536, "metadata": {"title": "Machine Learning Basics"}},
])

# Query
results = index.query(
    vector=[0.15]*1536,
    top_k=5,
    include_metadata=True
)

# Qdrant
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams, Distance

client = QdrantClient("localhost", port=6333)
client.create_collection(
    collection_name="documents",
    vectors_config=VectorParams(size=1536, distance=Distance.COSINE)
)
client.upsert(collection_name="documents", points=[
    PointStruct(id=1, vector=[0.1]*1536, payload={"title": "AI Overview"}),
])

# Weaviate
import weaviate
client = weaviate.Client("http://localhost:8080")
client.query.get("Document", ["title"]).with_near_vector({
    "vector": [0.1]*1536
}).with_limit(5).do()
```

## Key Concepts
Vector DBs store embedding vectors and enable fast approximate nearest neighbor (ANN) search. Key features: hybrid search (vector + keyword), metadata filtering, multi-tenancy, and CRUD operations.

## When to Use
- Production RAG systems at scale
- Semantic product search and recommendations
- Duplicate detection and similarity matching
- Long-term memory for AI agents

## Validation
1. Index creation with correct dimensionality matches embedding model
2. Query returns semantically relevant results
3. Metadata filtering works alongside vector search
4. Index handles production-scale upserts and queries
