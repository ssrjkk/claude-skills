---
name: agent-design
description: Проектирует LLM-агентов с памятью, инструментами и циклом reasoning. Используется для создания автономных AI-ассистентов.
category: ai
tags: [agent, llm, tools, memory, reasoning]
models: [opus]
version: 1.0.0
created: 2026-04-29
---
# Agent Design

> Проектирование LLM-агентов с памятью и инструментами.

## 🚀 Quick Start
```python
from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI

tools = [
    Tool(name="Search", func=search_func, description="Поиск в web"),
]

agent = initialize_agent(
    tools, 
    OpenAI(temperature=0), 
    agent="zero-shot-react-description",
    verbose=True
)
agent.run("Найди информацию о Python")
```

## 📋 Когда использовать
- ✅ Автономные AI-ассистенты
- ✅ Нужен reasoning и использование инструментов
- ❌ Не использовать для простых Q&A задач

## 🔧 Пошаговая инструкция
1. Определи инструменты (search, calculator, API)
2. Настрой системный промпт с ролью агента
3. Добавь память (buffer, summary)
4. Тестируй цикл reasoning

## 📦 Зависимости
```bash
pip install langchain openai
```

## 🧪 Примеры
Input: "Какая погода в Москве?" → Output: Агент вызывает weather API, возвращает ответ

## 🔗 Ресурсы
- [LangChain Agents](https://python.langchain.com/docs/modules/agents/)
- [Примеры кода](./examples/)

## ✅ Валидация
1. Агент выбирает правильные инструменты
2. Память сохраняет контекст диалога
3. Reasoning цепочка логична и завершена
