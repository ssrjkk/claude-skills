---
name: cassandra
description: "Models and queries data with Apache Cassandra for high-availability, partition-tolerant NoSQL workloads."
category: database
tags: [cassandra, nosql, wide-column, distributed, database]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Apache Cassandra

> Highly-scalable, partition-tolerant NoSQL database.

## Quick Start
```sql
CREATE KEYSPACE myapp WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};
USE myapp;
CREATE TABLE users (user_id UUID PRIMARY KEY, name TEXT, email TEXT, created_at TIMESTAMP);
CREATE TABLE orders_by_user (user_id UUID, order_id UUID, total DECIMAL, created_at TIMESTAMP, PRIMARY KEY (user_id, created_at, order_id)) WITH CLUSTERING ORDER BY (created_at DESC);
```

## When to Use
- High-write-throughput applications
- Time-series data
- IoT sensor data
- Multi-region deployments

## Validation
1. Node joins the cluster
2. CQL queries return correct data
3. Replication works across nodes
