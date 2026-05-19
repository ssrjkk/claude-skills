---
name: artillery
description: Load tests APIs and applications with Artillery, supporting HTTP, WebSocket, and Socket.io.
category: qa
tags: [artillery, load-testing, performance, http, websocket]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Artillery
> Cloud-scale load testing with YAML configuration.
## Quick Start
```yaml
config:
  target: "https://api.example.com"
  phases: [{ duration: 60, arrivalRate: 5, rampTo: 20, name: "Warm up" }]
scenarios:
  - flow:
      - get: { url: "/api/users" }
      - post: { url: "/api/users", json: { name: "Alice" } }
```
```bash
artillery run config.yaml
```
## WebSocket Testing
```yaml
scenarios:
  - engine: "ws"
    flow: [{ connect: "ws://localhost:8080" }, { send: '{"event": "join", "room": "general"}' }]
```
## When to Use
- API load testing; WebSocket perf testing; CI/CD performance gates
## Validation
1. Artillery runs and produces metrics; 2. Response times tracked; 3. p50/p95/p99 shown
