---
name: logging-elk
description: Sets up centralized log collection and analysis with ELK stack. Use for debugging and log monitoring.
category: devops
tags: [elk, elasticsearch, logstash, kibana, logging]
models: [opus]
version: 1.0.0
created: 2026-04-29
---
# Logging ELK

> Centralized logging with ELK stack.

## 🚀 Quick Start
```yaml
# docker-compose.yml
version: '3'
services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:8.x
    ports:
      - "9200:9200"
  kibana:
    image: docker.elastic.co/kibana/kibana:8.x
    ports:
      - "5601:5601"
```

## 📋 When to Use
- ✅ Centralized logging from multiple services
- ✅ Need log search and analysis
- ❌ Not for simple single log file apps

## 🔧 Step-by-Step Instructions
1. Start ELK via docker-compose
2. Configure application logging in JSON format
3. Set up Logstash pipeline for parsing
4. Create dashboards in Kibana

## 📦 Dependencies
```bash
docker-compose up -d
```

## 🧪 Examples
Input: App logs sent to Logstash
Output: Logs indexed in Elasticsearch, visible in Kibana

## 🔗 Resources
- [ELK Stack Docs](https://www.elastic.co/guide/index.html)
- [Examples](./examples/)

## ✅ Validation
1. Elasticsearch responds to queries
2. Logs appear in Kibana
3. Log search works correctly
