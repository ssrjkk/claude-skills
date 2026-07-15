---
name: python-fastapi
description: "Creates REST API templates with FastAPI, Pydantic validation, and auto-generated documentation. Use for building new microservices or API endpoints."
category: backend
tags: [python, fastapi, rest, pydantic, async]
models: [sonnet, opus]
version: 1.0.0
created: 2026-04-29
---
# Python FastAPI

> FastAPI with auto-generated docs and type validation.

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

## 📋 When to Use
- ✅ Building new REST APIs on Python
- ✅ Need auto-generated OpenAPI docs
- ❌ Not for monoliths without API layer

## 🔧 Step-by-Step Instructions
1. Install: `pip install fastapi uvicorn`
2. Create `main.py` with FastAPI code
3. Define data models with Pydantic
4. Run: `uvicorn main:app --reload`

## 📦 Dependencies
```bash
pip install fastapi uvicorn pydantic
```

## 🧪 Examples
Input: `POST /users/` with `{"name": "John", "email": "john@example.com"}`
Output: `{"message": "User created", "user": {...}}`

## 🔗 Resources
- [FastAPI Docs](https://fastapi.tiangolo.com)
- [Examples](./examples/)

## ✅ Validation
1. Server starts without errors: `uvicorn main:app --reload`
2. Docs available at `http://localhost:8000/docs`
3. Requests validated correctly
