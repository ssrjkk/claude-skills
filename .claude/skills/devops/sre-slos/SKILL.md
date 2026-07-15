---
name: sre-slos
description: "SRE SLI/SLO/SLA implementation"
category: devops
tags: [sre, sli, slo, sla, reliability, monitoring]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# SRE SLOs

> Implement Service Level Indicators, Objectives, and Agreements following SRE best practices.

## Quick Start
```yaml
# slo-config.yaml — Service level configuration
apiVersion: sre.google.com/v1
kind: SLO
metadata:
  name: api-availability
  service: payment-api
spec:
  description: "Payment API availability SLO"
  target: 99.9  # percentage
  window: 28d   # rolling window
  
  indicator:
    type: availability
    definition: |
      # SLI: Ratio of successful requests
      good_events = count(status_code < 500)
      valid_events = count(status_code != 0)
      sli = good_events / valid_events
  
  burnRateAlerts:
    - severity: page
      threshold: 0.01  # minutes of error budget consumed per minute
      lookback: 1h
    - severity: ticket
      threshold: 0.001
      lookback: 6h
---
# Error budget policy
apiVersion: sre.google.com/v1
kind: ErrorBudget
metadata:
  name: api-error-budget
spec:
  sloRef: api-availability
  policy:
    # Stop deployments when error budget is depleted
    deployFreeze:
      enabled: true
      remainingBudgetPercent: 20
```

```python
# SLO Monitoring with Prometheus
from prometheus_client import Histogram, Counter
import time

REQUEST_LATENCY = Histogram(
    'http_request_duration_seconds',
    'HTTP request latency',
    ['method', 'endpoint'],
    buckets=[0.01, 0.05, 0.1, 0.25, 0.5, 1.0, 2.5, 5.0]
)

REQUEST_COUNT = Counter(
    'http_requests_total',
    'Total HTTP requests',
    ['method', 'endpoint', 'status']
)

def track_request(method: str, endpoint: str):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            try:
                result = func(*args, **kwargs)
                REQUEST_COUNT.labels(method=method, endpoint=endpoint, status="200").inc()
                return result
            except Exception:
                REQUEST_COUNT.labels(method=method, endpoint=endpoint, status="500").inc()
                raise
            finally:
                REQUEST_LATENCY.labels(method=method, endpoint=endpoint).observe(time.time() - start)
        return wrapper
    return decorator
```

## Key Concepts
SLIs measure service reliability (latency, availability, durability). SLOs set targets (e.g., 99.9% availability over 28 days). Error budget = (1 - SLO) × total events. Use burn rate alerts for early detection.

## When to Use
- Defining reliability expectations for services
- Making data-driven decisions about deployment velocity
- Balancing feature development with reliability investment

## Validation
1. SLIs are accurately measured and reported
2. SLO compliance dashboard shows current and historical status
3. Error budget alerts fire correctly during degradation
4. Deployment gates respect error budget policy
