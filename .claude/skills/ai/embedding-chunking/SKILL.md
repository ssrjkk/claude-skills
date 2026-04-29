---
name: embedding-chunking
description: Разбивает документы на чанки и создает embeddings для семантического поиска. Используется в RAG пайплайнах.
category: ai
tags: [embeddings, chunking, rag, semantic-search]
models: [sonnet, opus]
version: 1.0.0
created: 2026-04-29
---
# Embedding & Chunking

> Оптимальное разбиение текста и создание векторных представлений.

## 🚀 Quick Start
```python
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = text_splitter.split_text(long_document)

embeddings = OpenAIEmbeddings()
vectors = [embeddings.embed_query(chunk) for chunk in chunks]
```

## 📋 Когда использовать
- ✅ Подготовка документов для RAG
- ✅ Семантический поиск по тексту
- ❌ Не использовать для коротких запросов

## 🔧 Пошаговая инструкция
1. Выберите стратегию чанкинга (fixed, semantic, recursive)
2. Настройте размер и перекрытие чанков
3. Сгенерируйте embeddings через API
4. Сохраните в векторную БД

## 📦 Зависимости
```bash
pip install langchain openai tiktoken
```

## 🧪 Примеры
Input: Документ 10000 символов → Output: 20 чанков по 500 символов с embeddings

## 🔗 Ресурсы
- [OpenAI Embeddings](https://platform.openai.com/docs/guides/embeddings)
- [Примеры кода](./examples/)

## ✅ Валидация
1. Чанки не теряют контекста на границах
2. Embeddings имеют ожидаемую размерность
3. Поиск возвращает релевантные чанки
