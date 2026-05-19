---
name: clickhouse
description: Analyzes large datasets with ClickHouse, column-oriented DBMS for real-time analytical queries.
category: database
tags: [clickhouse, olap, analytics, columnar, sql]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# ClickHouse

> Column-oriented DBMS for real-time analytical queries.

## Quick Start
```sql
CREATE TABLE orders (order_id UInt64, user_id UInt32, amount Decimal(10,2), created_at DateTime)
ENGINE = MergeTree() ORDER BY created_at;
```

## Partitioning & Optimization
```sql
CREATE TABLE events (event_date Date, event_type String, user_id UInt32, value Float64)
ENGINE = MergeTree() PARTITION BY toYYYYMM(event_date) ORDER BY (event_type, event_date);
```

## Analytics
```sql
SELECT toStartOfMonth(created_at) AS month, user_id, COUNT(*) AS order_count, SUM(amount) AS total_spent
FROM orders GROUP BY month, user_id ORDER BY total_spent DESC LIMIT 10;
```

## When to Use
- Real-time analytics dashboards
- Clickstream analysis
- Log analytics
- OLAP workloads

## Validation
1. ClickHouse accepts connections
2. Tables created and data inserted
3. Aggregation queries complete quickly
