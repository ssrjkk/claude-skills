---
name: contract-testing-pact
description: Реализует контрактное тестирование API с Pact. Используется для проверки совместимости между сервисами.
category: qa
tags: [contract-testing, pact, api, testing]
models: [sonnet, opus]
version: 1.0.0
created: 2026-04-29
---
# Contract Testing Pact

> Контрактное тестирование API между микросервисами с Pact.

## 🚀 Quick Start
```python
from pact import Consumer, Provider

pact = Consumer('ConsumerService').has_pact_with(
    Provider('ProviderService')
)

def test_user_api():
    pact.given('User exists') \
        .upon_receiving('a request for user') \
        .with_request('GET', '/users/1') \
        .will_respond_with(200, body={'id': 1, 'name': 'John'})
```

## 📋 Когда использовать
- ✅ Микросервисная архитектура
- ✅ Проверка контрактов API
- ❌ Не использовать для монолитов

## 🔧 Пошаговая инструкция
1. Установи: `pip install pact-python`
2. Определи ожидания потребителя
3. Создай мок провайдера
4. Верифицируй контракт

## 📦 Зависимости
```bash
pip install pact-python pytest
```

## 🧪 Примеры
Input: Тест контракта → Output: Pact файл соглашения

## 🔗 Ресурсы
- [Pact Docs](https://docs.pact.io/)
- [Примеры кода](./examples/)

## ✅ Валидация
1. Контракты генерируются корректно
2. Верификация проходит успешно
3. Несовместимость контрактов обнаруживается
