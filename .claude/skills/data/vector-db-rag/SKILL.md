---
name: vector-db-rag
description: Строит RAG пайплайны с векторными базами данных (Chroma, Pinecone) и embedding моделями. Используется для семантического поиска и LLM приложений.
category: data
tags: [rag, vector-db, embeddings, llm, semantic-search]
models: [opus]
version: 1.0.0
created: 2026-04-29
---
# Vector DB RAG

> RAG пайплайны с векторными базами и LLM для семантического поиска.

## 🚀 Quick Start
```python
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

# Создание векторной БД
embeddings = OpenAIEmbeddings()
db = Chroma.from_documents(documents, embeddings)

# Семантический поиск
docs = db.similarity_search("query about documents")
```

## 📋 Когда использовать
- ✅ Семантический поиск по документам
- ✅ RAG архитектура для LLM
- ❌ Не использовать для точного поиска по ID

## 🔧 Пошаговая инструкция
1. Подготовь документы и разбей на чанки
2. Создай embeddings через OpenAI/Cohere
3. Сохрани в векторную БД (Chroma/Pinecone)
4. Настрой retrieval для LLM

## 📦 Зависимости
```bash
pip install langchain chromadb openai
```

## 🧪 Примеры
Input: "How to use FastAPI?" → Output: Релевантные фрагменты документации

## 🔗 Ресурсы
- [LangChain Docs](https://python.langchain.com/)
- [Примеры кода](./examples/)

## ✅ Валидация
1. Векторы создаются корректно
2. Поиск возвращает релевантные результаты
3. RAG пайплайн работает end-to-end
