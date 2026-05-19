---
name: sqlite
description: Embeds SQLite databases in applications with zero configuration and single-file storage. Use for local data persistence.
category: database
tags: [sqlite, sql, embedded, database, lightweight]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# SQLite

> Self-contained, serverless, zero-configuration SQL database engine.

## Quick Start
```bash
sqlite3 mydb.db
CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL);
INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');
SELECT * FROM users;
```

## CLI Commands
```bash
.tables          # List tables
.schema users    # Show schema
.mode json       # JSON output
.headers on      # Show column headers
```

## Python Integration
```python
import sqlite3
conn = sqlite3.connect('mydb.db')
cursor = conn.execute('SELECT * FROM users WHERE id = ?', (1,))
```

## When to Use
- Mobile app storage
- Desktop application data
- Prototypes and testing
- Embedded/IoT devices

## Validation
1. Database file creates correctly
2. SQL queries execute without error
3. Transactions commit and rollback
