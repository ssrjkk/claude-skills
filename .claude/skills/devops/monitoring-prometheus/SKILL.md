---
name: monitoring-prometheus
description: Sets up application and infrastructure monitoring with Prometheus and Grafana. Use for metrics collection and alerting.
category: devops
tags: [prometheus, grafana, monitoring, metrics]
models: [sonnet, opus]
version: 1.0.0
created: 2026-04-29
---
# Monitoring Prometheus

> Metrics, alerting, and visualization with Prometheus + Grafana.

## 🚀 Quick Start
```yaml
# prometheus.yml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'myapp'
    static_configs:
      - targets: ['localhost:8080']
```

```bash
# Start Prometheus
docker run -p 9090:9090 -v prometheus.yml:/etc/prometheus/prometheus.yml prom/prometheus
```

## 📋 When to Use
- ✅ Need application monitoring
- ✅ Collecting time-series metrics
- ❌ Not for logging (better use ELK)

## 🔧 Step-by-Step Instructions
1. Set up metrics exporters in your app
2. Create prometheus.yml with scrape configs
3. Start Prometheus and Grafana containers
4. Configure dashboards in Grafana

## 📦 Dependencies
```bash
docker run -p 9090:9090 prom/prometheus
docker run -p 3000:3000 grafana/grafana
```

## 🧪 Examples
Input: HTTP request to `/metrics` endpoint
Output: Metrics in Prometheus format

## 🔗 Resources
- [Prometheus Docs](https://prometheus.io/docs/)
- [Examples](./examples/)

## ✅ Validation
1. Prometheus scrapes targets successfully
2. Alerts trigger on conditions
3. Grafana dashboards show data
