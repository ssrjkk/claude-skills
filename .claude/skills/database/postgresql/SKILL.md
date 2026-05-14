---
name: postgresql
description: Models relational data, writes optimized queries, and manages PostgreSQL databases with indexes, views, and CTEs. Use for robust data storage.
category: database
tags: [postgresql, sql, database, relational, queries]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# PostgreSQL

> Advanced relational database with powerful querying and indexing.

## Quick Start
```sql
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_users_email ON users(email);
```

## When to Use
- Structured relational data
- Complex queries and joins
- Transactional workloads
- Analytics with window functions

## Step-by-Step
1. Install PostgreSQL
2. Create database: `CREATE DATABASE mydb;`
3. Design schema with migrations
4. Optimize with EXPLAIN ANALYZE

## Dependencies
```bash
# psql client
psql -h localhost -U postgres -d mydb
```

## Examples
```sql
SELECT u.name, COUNT(o.id) as order_count
FROM users u
LEFT JOIN orders o ON o.user_id = u.id
GROUP BY u.id
HAVING COUNT(o.id) > 5
ORDER BY order_count DESC;
```

## Resources
- [PostgreSQL Docs](https://www.postgresql.org/docs)

## Validation
1. Connection succeeds
2. Queries return correct results
3. Indexes improve query performance
