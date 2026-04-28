# Database Migration Reference

## Alembic Commands
- `alembic revision -m "message"` — создать новую ревизию
- `alembic upgrade head` — применить все миграции
- `alembic downgrade -1` — откатить последнюю миграцию

## PostgreSQL Operations
- `CREATE TABLE` — создание таблицы
- `ALTER TABLE` — изменение таблицы
