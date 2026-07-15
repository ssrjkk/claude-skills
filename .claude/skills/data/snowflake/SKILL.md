---
name: snowflake
description: "Manages data warehousing with Snowflake, including virtual warehouses, clustering, and semi-structured data support. Use for cloud analytics at scale."
category: data
tags: [snowflake, data-warehouse, cloud, analytics, sql]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Snowflake

> Cloud data warehouse with separate storage and compute.

## Quick Start
```sql
CREATE WAREHOUSE my_wh WITH WAREHOUSE_SIZE = 'XSMALL';
CREATE DATABASE analytics;
CREATE TABLE users (
  id INTEGER,
  name VARCHAR(100),
  email VARCHAR(255),
  created_at TIMESTAMP_NTZ
);
```

## When to Use
- Cloud data warehousing
- Analytics and reporting
- Semi-structured data (JSON, Parquet)
- Data sharing across organizations

## Step-by-Step
1. Create warehouse and database
2. Load data from stage
3. Query with standard SQL
4. Set up cloning and time travel

## Dependencies
```sql
ALTER WAREHOUSE my_wh RESUME;
USE DATABASE analytics;
```

## Examples
```sql
SELECT
  DATE_TRUNC('MONTH', created_at) AS month,
  COUNT(*) AS signups
FROM users
WHERE created_at >= DATEADD(YEAR, -1, CURRENT_DATE())
GROUP BY month
ORDER BY month;
```

## Resources
- [Snowflake Docs](https://docs.snowflake.com)

## Validation
1. Warehouse starts and runs queries
2. Data loads from stage successfully
3. Time travel queries return historical data
