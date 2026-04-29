---
name: python-fastapi
description: Создает шаблоны для REST API на FastAPI с валидацией Pydantic и авто-документацией. Используется при создании новых микросервисов или API эндпоинтов.
category: backend
tags: [python, fastapi, rest, pydantic, async]
models: [sonnet, opus]
version: 1.0.0
created: 2026-04-29
---
# Python FastAPI

> Быстрый старт REST API с автоматической документацией и валидацией типов.

## 🚀 Quick Start
```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    email: str

@app.post("/users/")
async def create_user(user: User):
    return {"message": "User created", "user": user}
```

## 📋 Когда использовать
- ✅ Создание нового REST API на Python
- ✅ Нужна авто-документация (Swagger/OpenAPI)
- ❌ Не использовать для монолитных приложений без API

## 🔧 Пошаговая инструкция
1. Установи зависимости: `pip install fastapi uvicorn`
2. Создай файл `main.py` с кодом FastAPI
3. Определи модели данных через Pydantic
4. Запусти сервер: `uvicorn main:app --reload`

## 📦 Зависимости
```bash
pip install fastapi uvicorn pydantic
```

## 🧪 Примеры
Input: `POST /users/` с JSON `{"name": "John", "email": "john@example.com"}`
Output: `{"message": "User created", "user": {"name": "John", "email": "john@example.com"}}`

## 🔗 Ресурсы
- [Официальная документация FastAPI](https://fastapi.tiangolo.com)
- [Примеры кода](./examples/)

## ✅ Валидация
1. Сервер запускается без ошибок: `uvicorn main:app --reload`
2. Документация доступна по адресу `http://localhost:8000/docs`
3. Запросы валидируются корректно
