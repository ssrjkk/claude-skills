---
name: langchain-rag
description: Builds advanced RAG (Retrieval-Augmented Generation) pipelines with LangChain, multiple retrievers, and document chains.
category: ai
tags: [langchain, rag, llm, retrieval, embeddings]
models: [opus]
version: 1.0.0
created: 2026-05-14
---
# LangChain RAG

> Production RAG pipelines with LangChain — retrieval, generation, and evaluation.

## Quick Start
```python
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

# Vector store
db = Chroma(persist_directory="./chroma_db", embedding_function=OpenAIEmbeddings())

# RAG chain
llm = ChatOpenAI(model="gpt-4o")
prompt = ChatPromptTemplate.from_template("Answer based on context: {context}\nQuestion: {input}")
doc_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(db.as_retriever(search_kwargs={"k": 4}), doc_chain)

result = rag_chain.invoke({"input": "What is RAG?"})
print(result["answer"])
```

## When to Use
- ✅ Question answering over documents
- ✅ Chat with your data (PDFs, wikis, databases)
- ❌ Not for simple Q&A without external knowledge

## Step-by-Step Instructions
1. Load and chunk documents
2. Create embeddings and vector store
3. Set up retriever with relevant parameters
4. Create RAG chain with custom prompt

## Dependencies
```bash
pip install langchain langchain-openai langchain-chroma
```

## Examples
Input: "Summarize the key findings" → Output: Answer grounded in retrieved documents

## Resources
- [LangChain RAG](https://python.langchain.com/docs/use_cases/question_answering/)
- [Examples](./examples/)

## Validation
1. Retriever returns relevant documents
2. LLM generates grounded answers
3. Citations are accurate
