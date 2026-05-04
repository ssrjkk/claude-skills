---
name: api-testing
description: Tests REST and GraphQL APIs using pytest and requests library. Use for endpoint validation, HTTP response verification, and automated API test writing.
category: qa
tags: [api, testing, rest, graphql, pytest, requests]
models: [haiku, sonnet, opus]
version: 1.0.0
created: 2026-04-29
---
# API Testing

> Automated API testing with pytest and requests for REST/GraphQL endpoints.

## 🚀 Quick Start
```python
import pytest
import requests

def test_get_user():
    response = requests.get("https://api.example.com/users/1")
    assert response.status_code == 200
    assert "id" in response.json()
```

## 📋 When to Use
- ✅ Testing REST or GraphQL APIs
- ✅ Validating HTTP responses and headers
- ❌ Not for UI testing (use E2E tools instead)

## 🔧 Step-by-Step Instructions
1. Install: `pip install pytest requests`
2. Create test file `test_api.py`
3. Write tests with status code and response validation
4. Run: `pytest test_api.py -v`

## 📦 Dependencies
```bash
pip install pytest requests
```

## 🧪 Examples
Input: `GET /users/1` with valid API
Output: Response 200, JSON contains user data

## 🔗 Resources
- [requests docs](https://docs.python-requests.org/)
- [pytest docs](https://docs.pytest.org/)

## ✅ Validation
1. All tests pass: `pytest --tb=short`
2. Endpoints covered as required
3. No false positives
