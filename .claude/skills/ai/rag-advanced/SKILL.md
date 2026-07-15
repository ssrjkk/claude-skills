---
name: rag-advanced
description: "Advanced RAG patterns (HyDE, multi-hop, agentic RAG)"
category: ai
tags: [rag, retrieval, hyde, multi-hop, agentic]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Advanced RAG

> Implement cutting-edge RAG patterns including HyDE, multi-hop retrieval, and agentic RAG.

## Quick Start
```python
from openai import OpenAI
import numpy as np

class HyDERetrieval:
    """Hypothetical Document Embeddings — generate then retrieve"""
    
    def __init__(self, embedding_model="text-embedding-3-small"):
        self.client = OpenAI()
    
    def hyde_query(self, question: str) -> str:
        """Generate a hypothetical document that would answer the question"""
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": f"""Write a detailed paragraph that would answer this question. Include specific facts and figures:
Question: {question}
Hypothetical answer:"""}],
            max_tokens=300
        )
        return response.choices[0].message.content
    
    def search(self, question: str, top_k: int = 5):
        # Generate hypothetical document
        hypothetical = self.hyde_query(question)
        
        # Embed the hypothetical document instead of the question
        response = self.client.embeddings.create(
            model=self.embedding_model,
            input=[hypothetical]
        )
        query_embedding = response.data[0].embedding
        
        # Search vector DB with this embedding
        # (pseudo-code — adapt to your vector DB)
        results = vector_db.similarity_search(query_embedding, k=top_k)
        return results

# Multi-hop RAG: break complex queries into sub-questions
def multi_hop_rag(question: str, depth: int = 2):
    """Break complex question into sub-questions, retrieve for each"""
    sub_questions = decompose_question(question)
    contexts = []
    
    for i in range(min(depth, len(sub_questions))):
        docs = retrieve(sub_questions[i])
        contexts.extend(docs)
    
    return generate_answer(question, contexts)
```

## Key Concepts
**HyDE**: Generate a hypothetical perfect document, then use it for similarity search — bridges query-document gap. **Multi-hop**: Decompose complex queries, retrieve for each sub-question. **Agentic RAG**: Let an agent decide when and what to retrieve.

## When to Use
- Complex questions requiring multiple facts
- Domain-specific retrieval where query-document vocabulary mismatch exists
- Questions needing synthesis across multiple sources

## Validation
1. HyDE improves recall over direct query embedding on test set
2. Multi-hop retrieval correctly decomposes and answers complex queries
3. Agentic RAG only retrieves when necessary (reduces cost)
