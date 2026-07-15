---
name: elasticsearch
description: "Indexes, searches, and analyzes data with Elasticsearch, using full-text search, aggregations, and Kibana visualization. Use for search and log analytics."
category: database
tags: [elasticsearch, search, kibana, analytics, nosql]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Elasticsearch

> Distributed search and analytics engine for all types of data.

## Quick Start
```json
PUT /products/_doc/1
{
  "name": "Wireless Mouse",
  "price": 29.99,
  "tags": ["electronics", "accessories"]
}
```

## When to Use
- Full-text search
- Log and event analytics
- Product catalogs
- Metrics and monitoring

## Step-by-Step
1. Start Elasticsearch + Kibana
2. Create index with mapping
3. Index documents
4. Search with query DSL

## Dependencies
```bash
# Docker
docker run -p 9200:9200 -e "discovery.type=single-node" elasticsearch:8.x
```

## Examples
```json
GET /products/_search
{
  "query": { "match": { "name": "wireless mouse" } },
  "aggs": { "avg_price": { "avg": { "field": "price" } } }
}
```

## Resources
- [Elasticsearch Guide](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html)

## Validation
1. Cluster health is green
2. Documents indexed and searchable
3. Aggregations return correct results
