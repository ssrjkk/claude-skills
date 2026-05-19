---
name: mysql
description: Designs and manages MySQL databases with schemas, indexes, queries, and replication. Use for relational data storage.
category: database
tags: [mysql, sql, database, relational, queries]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# MySQL

> Popular open-source relational database management system.

## Quick Start
```sql
CREATE DATABASE myapp; USE myapp;
CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100) NOT NULL, email VARCHAR(255) UNIQUE NOT NULL, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
```

## Indexes & Optimization
```sql
CREATE INDEX idx_email ON users(email);
CREATE FULLTEXT INDEX idx_search ON posts(title, body);
EXPLAIN SELECT * FROM users WHERE email = 'test@example.com';
```

## When to Use
- Web application backends
- Content management systems
- E-commerce platforms
- Relational data with joins

## Validation
1. Connection to MySQL succeeds
2. Queries return correct results
3. EXPLAIN shows index usage
