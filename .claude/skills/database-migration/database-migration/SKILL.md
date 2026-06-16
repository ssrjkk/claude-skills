---
name: database-migration
description: Manages PostgreSQL database migrations using Alembic. Use for creating, applying, and rolling back schema changes in QA environments.
category: database-migration
tags: [database, migration, postgresql, alembic, qa, schema]
models: [haiku, sonnet, opus]
version: 1.0.0
created: 2026-04-29
---
# Database Migration

> Manage PostgreSQL schema changes with Alembic migrations.

## 🚀 Quick Start
```bash
pip install alembic psycopg2-binary
alembic init migrations
alembic revision -m "create users table"
alembic upgrade head
```

## 📋 When to Use
- ✅ Managing PostgreSQL schema changes
- ✅ Version-controlled database migrations
- ❌ Not for NoSQL databases

## 🔧 Step-by-Step Instructions
1. Configure `alembic.ini` with PostgreSQL connection
2. Create new revision: `alembic revision -m "description"`
3. Write migration code in `migrations/versions/`
4. Apply migrations: `alembic upgrade head`
5. Rollback if needed: `alembic downgrade -1`

## 📦 Dependencies
```bash
pip install alembic psycopg2-binary
```

## 🧪 Examples
Input: `alembic upgrade head` with valid migration
Output: Database schema updated successfully

## 🔗 Resources
- [Alembic Docs](https://alembic.sqlalchemy.org/)
- [Examples](./examples/)

## ✅ Validation
1. Migration applies without errors: `alembic upgrade head`
2. Schema matches expected structure
3. Rollback restores previous state
