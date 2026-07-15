---
name: locust
description: "Performs load testing with Locust, Python-based distributed testing, and real-time web UI."
category: qa
tags: [locust, load-testing, python, performance, stress-test]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Locust
> Distributed load testing framework in Python.
## Quick Start
```python
from locust import HttpUser, task, between
class WebsiteUser(HttpUser):
    wait_time = between(1, 3)
    @task(5)
    def browse(self): self.client.get("/products")
    @task(1)
    def checkout(self): self.client.post("/checkout", json={"item": "book"})
```
```bash
locust -f locustfile.py --web-host localhost
```
## When to Use
- API load testing; Performance regression; Capacity planning; Spike testing
## Validation
1. Locust UI shows metrics; 2. RPS displays correctly; 3. Test stops and reports
