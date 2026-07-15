---
name: embedding-models
description: "Working with embedding models (OpenAI, Cohere, Voyage)"
category: ai
tags: [embeddings, vector, semantic-search, openai, cohere, voyage]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Embedding Models

> Generate and use embeddings from major providers for semantic search, clustering, and classification.

## Quick Start
```python
import numpy as np
from openai import OpenAI
from typing import List

class EmbeddingService:
    def __init__(self, provider: str = "openai"):
        self.provider = provider
        if provider == "openai":
            self.client = OpenAI()
            self.model = "text-embedding-3-small"
            self.dimensions = 1536
        elif provider == "cohere":
            import cohere
            self.client = cohere.Client()
            self.model = "embed-english-v3.0"
            self.dimensions = 1024
        elif provider == "voyage":
            import voyageai
            self.client = voyageai.Client()
            self.model = "voyage-3-lite"
            self.dimensions = 1024

    def embed(self, texts: List[str]) -> np.ndarray:
        if self.provider == "openai":
            response = self.client.embeddings.create(
                model=self.model, input=texts
            )
            return np.array([d.embedding for d in response.data])
        elif self.provider == "cohere":
            response = self.client.embed(
                texts=texts, model=self.model,
                input_type="search_document"
            )
            return np.array(response.embeddings)
        elif self.provider == "voyage":
            response = self.client.embed(
                texts=texts, model=self.model
            )
            return np.array(response.embeddings)

    def similarity(self, a: np.ndarray, b: np.ndarray) -> float:
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

svc = EmbeddingService("openai")
embeddings = svc.embed(["Paris is the capital of France", "London is the capital of UK"])
print(f"Similarity: {svc.similarity(embeddings[0], embeddings[1]):.3f}")
```

## Key Concepts
Embeddings map text to dense vector space. Different providers optimize for different tasks: OpenAI for general use, Cohere for search/classification, Voyage for multilingual. Consider dimensions, cost, latency, and language support.

## When to Use
- Semantic search over document collections
- Clustering similar documents or customer queries
- Classification with embedding + classifier
- Recommendation systems (item similarity)

## Validation
1. Embeddings from same provider produce consistent results
2. Cosine similarity correctly ranks related vs unrelated text
3. Batch processing doesn't hit rate limits
4. Embedding dimension and model match your vector DB requirements
