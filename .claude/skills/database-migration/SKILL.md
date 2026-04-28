---
name: database-migration
description: Управляет миграциями баз данных PostgreSQL с помощью Alembic. Используется для создания, применения и отката миграций схемы БД в QA-окружениях.
---
# Database Migration

## 🚀 Quick Start
```bash
pip install alembic psycopg2-binary
alembic init migrations
alembic revision -m "create users table"
alembic upgrade head
```

## 📋 Инструкция
1. Настрой `alembic.ini` с параметрами подключения к PostgreSQL
2. Создай новую ревизию: `alembic revision -m "описание изменений"`
3. Напиши код миграции в `migrations/versions/`
4. Применяй миграции: `alembic upgrade head`
5. Откатывай при необходимости: `alembic downgrade -1`

## 🔧 Скрипты/Инструменты
- `scripts/migration_helper.py` — утилиты для проверки состояния БД
- `scripts/seed_data.py` — заполнение тестовыми данными

## 📚 Ресурсы
- `reference.md` — синтаксис Alembic и операции с PostgreSQL
- `examples.md` — примеры миграций для типичных схем

## ✅ Валидация
1. Миграция применяется без ошибок: `alembic upgrade head`
2. Схема БД соответствует ожидаемой структуре
3. Откат миграции восстанавливает предыдущее состояние
