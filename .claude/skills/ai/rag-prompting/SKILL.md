---
name: rag-prompting
description: Designs prompts optimized for Retrieval-Augmented Generation systems, including context integration, citation handling, and hallucination reduction. Use for RAG applications.
category: ai
tags: [prompt, rag, retrieval, context, citations]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# RAG Prompting

> Prompt strategies for retrieval-augmented generation systems.

## Quick Start
```
Answer based ONLY on the provided context.
If the answer is not in the context, say "I cannot answer from the available information."
Cite the source paragraph numbers in your answer.

Context:
[1] Climate change is caused by greenhouse gas emissions.
[2] Carbon dioxide levels have risen 50% since the Industrial Revolution.
[3] The Paris Agreement aims to limit warming to 1.5°C.

Question: What causes climate change?
Answer: Climate change is caused by greenhouse gas emissions [1].
```

## When to Use
- Document Q&A systems
- Knowledge base assistants
- Customer support chatbots
- Research paper analysis

## Techniques

### Context Window Management
Place most relevant documents at the top/bottom of context.

### Citation Format
Define clear citation style (brackets, source IDs, page numbers).

### Hallucination Guard
Explicitly instruct to only use provided context.

### Source Quality
Tag sources by reliability level in the prompt.

## Dependencies
```bash
pip install langchain openai chromadb
```

## Examples
```
You have access to the following product documentation.
Only answer using information from these documents.
If documents don't contain the answer, say so.

Documents:
<doc id="1">The API rate limit is 100 requests per minute.</doc>
<doc id="2">Authentication requires a Bearer token in the header.</doc>
```

## Resources
- [LangChain RAG](https://python.langchain.com/docs/use_cases/question_answering)

## Validation
1. Answers are grounded in retrieved context
2. Citations correctly reference sources
3. Model refuses to answer outside context
4. Multiple documents synthesized correctly
