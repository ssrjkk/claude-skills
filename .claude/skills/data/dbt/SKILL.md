---
name: dbt
description: Transforms data in warehouses using dbt with SQL models, tests, and documentation. Use for analytics engineering and data transformation.
category: data
tags: [dbt, sql, data-warehouse, analytics, etl]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# dbt

> Data transformation tool that enables analytics engineers to transform data in their warehouses.

## Quick Start
```sql
-- models/staging/stg_orders.sql
WITH source AS (
  SELECT * FROM {{ source('shopify', 'orders') }}
)
SELECT
  id AS order_id,
  customer_id,
  total_price,
  created_at
FROM source
```

## When to Use
- Data warehouse transformations
- Analytics engineering
- Data quality testing
- Documentation generation

## Step-by-Step
1. Init: `dbt init my_project`
2. Write SQL models in `models/`
3. Define sources and tests
4. Run: `dbt run`

## Dependencies
```bash
pip install dbt-core dbt-postgres
dbt init my_project
```

## Examples
```sql
{{ config(materialized='table') }}
SELECT
  customer_id,
  COUNT(*) as order_count,
  SUM(total_price) as total_spent
FROM {{ ref('stg_orders') }}
GROUP BY customer_id
```

## Resources
- [dbt Docs](https://docs.getdbt.com)

## Validation
1. `dbt run` completes successfully
2. `dbt test` passes all tests
3. Documentation generates: `dbt docs generate`
