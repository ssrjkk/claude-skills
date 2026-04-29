---
name: prompt-engineering
description: Оптимизирует промпты для LLM с техниками few-shot, chain-of-thought и структурированным выводом. Используется для улучшения качества ответов.
category: ai
tags: [prompt, llm, engineering, few-shot, chain-of-thought]
models: [opus]
version: 1.0.0
created: 2026-04-29
---
# Prompt Engineering

> Техники написания эффективных промптов для LLM.

## 🚀 Quick Start
```
# Few-shot prompting
Примеры:
Q: 2+2=? A: 4
Q: 3+5=? A: 8
Q: 10+7=? A:

# Chain-of-Thought
Реши пошагово:
1. Проанализируй входные данные
2. Выдели ключевые факты
3. Сформулируй ответ
```

## 📋 Когда использовать
- ✅ Улучшение качества ответов LLM
- ✅ Нужна структурированная генерация
- ❌ Не использовать для простых одношаговых задач

## 🔧 Пошаговая инструкция
1. Определи задачу и желаемый формат вывода
2. Добавь примеры (few-shot) если нужно
3. Используй CoT для сложных рассуждений
4. Тестируй с разными моделями

## 📦 Зависимости
```bash
pip install openai anthropic
```

## 🧪 Примеры
Input: "Классифицируй: Отличный сервис!" с промптом для sentiment
Output: `{"sentiment": "positive", "confidence": 0.95}`

## 🔗 Ресурсы
- [OpenAI Prompt Engineering](https://platform.openai.com/docs/guides/prompt-engineering)
- [Примеры кода](./examples/)

## ✅ Валидация
1. Ответы соответствуют заданному формату
2. Качество выше базового промпта
3. Модель следует инструкциям стабильно
