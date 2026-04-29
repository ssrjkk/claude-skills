---
name: secrets-management
description: Управляет секретами приложений с HashiCorp Vault или AWS Secrets Manager. Используется для безопасного хранения учетных данных.
category: security
tags: [secrets, vault, security, credentials]
models: [sonnet, opus]
version: 1.0.0
created: 2026-04-29
---
# Secrets Management

> Безопасное хранение и ротация секретов приложений.

## 🚀 Quick Start
```bash
# Vault: запись секрета
vault kv put secret/myapp api_key=12345

# Vault: чтение секрета
vault kv get secret/myapp
```

## 📋 Когда использовать
- ✅ Хранение API ключей, паролей БД
- ✅ Ротация секретов
- ❌ Не использовать для хранения пользовательских файлов

## 🔧 Пошаговая инструкция
1. Разверни Vault или настрой AWS Secrets Manager
2. Определи политики доступа
3. Интегрируй чтение секретов в приложение
4. Настрой ротацию

## 📦 Зависимости
```bash
# Vault
brew install vault
# AWS CLI
pip install awscli
```

## 🧪 Примеры
Input: `vault kv get secret/myapp` → Output: `api_key=12345`

## 🔗 Ресурсы
- [Vault Docs](https://www.vaultproject.io/docs)
- [Примеры кода](./examples/)

## ✅ Валидация
1. Секреты читаются приложением без ошибок
2. Доступ ограничен политиками
3. Ротация проходит без downtime
