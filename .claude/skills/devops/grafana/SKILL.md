---
name: grafana
description: Creates dashboards and visualizations with Grafana, including Prometheus data sources, alerting, and annotations.
category: devops
tags: [grafana, monitoring, dashboards, visualization, alerting]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Grafana

> Open-source monitoring and observability platform.

## Quick Start
```bash
docker run -d -p 3000:3000 --name grafana grafana/grafana
# UI at http://localhost:3000 (admin/admin)
```

## Dashboard JSON
```json
{
  "title": "System Overview",
  "panels": [{
    "title": "CPU Usage",
    "type": "timeseries",
    "datasource": "Prometheus",
    "targets": [{ "expr": "100 - (avg by(instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)" }]
  }]
}
```

## Alert Rules
```yaml
groups:
  - name: instance_down
    rules:
      - alert: InstanceDown
        expr: up == 0
        for: 5m
        labels: { severity: critical }
        annotations: { summary: "Instance {{ $labels.instance }} down" }
```

## When to Use
- Infrastructure dashboards
- Application performance monitoring
- Multi-source observability
- Team alerting

## Validation
1. Data source connects successfully
2. Panels display real-time data
3. Alerts fire correctly
