# Database Migration Reference

## Alembic Commands
- `alembic revision -m "message"` — create a new revision
- `alembic upgrade head` — apply all migrations
- `alembic downgrade -1` — rollback last migration
- `alembic current` — show current revision
- `alembic history` — show migration history

## PostgreSQL Operations
- `CREATE TABLE` — create a table
- `ALTER TABLE` — modify a table
- `DROP TABLE` — delete a table
- `CREATE INDEX` — create an index
