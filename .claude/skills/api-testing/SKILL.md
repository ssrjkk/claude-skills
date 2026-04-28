---
name: api-testing
description: Тестирует REST и GraphQL API с использованием pytest и библиотеки requests. Используется для проверки эндпоинтов, валидации HTTP-ответов и написания автоматизированных API тестов.
---
# API Testing

## 🚀 Quick Start
```python
import pytest
import requests

def test_get_user():
    response = requests.get("https://api.example.com/users/1")
    assert response.status_code == 200
    assert "id" in response.json()
```

## 📋 Инструкция
1. Установи зависимости: `pip install pytest requests`
2. Создай тестовый файл `test_api.py`
3. Напиши тесты с проверкой статус-кодов, тела ответа, заголовков
4. Запусти тесты: `pytest test_api.py -v`

## 🔧 Скрипты/Инструменты
- `scripts/api_client.py` — обертка над requests для повторного использования
- `scripts/assertions.py` — кастомные проверки для API ответов

## 📚 Ресурсы
- `reference.md` — полный список HTTP-статусов и методов проверки
- `examples.md` — примеры тестов для REST и GraphQL

## ✅ Валидация
1. Все тесты проходят без ошибок: `pytest --tb=short`
2. Покрытие эндпоинтов соответствует требованиям
3. Нет ложноположительных результатов
