---
name: opentelemetry
description: "Implements observability with OpenTelemetry for distributed tracing, metrics, and logs collection."
category: devops
tags: [opentelemetry, observability, tracing, metrics, monitoring]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# OpenTelemetry

> Unified observability framework for traces, metrics, and logs.

## Quick Start (Node.js)
```javascript
const { NodeSDK } = require('@opentelemetry/sdk-node')
const { ConsoleSpanExporter } = require('@opentelemetry/sdk-trace-base')
const sdk = new NodeSDK({ traceExporter: new ConsoleSpanExporter() })
sdk.start()
```

## Distributed Tracing
```javascript
const { trace } = require('@opentelemetry/api')
const tracer = trace.getTracer('my-service')
const span = tracer.startSpan('process-order')
span.setAttribute('order.id', orderId)
span.end()
```

## Metrics
```javascript
const meter = metrics.getMeter('my-service')
const requestCounter = meter.createCounter('requests.total', { description: 'Total requests' })
requestCounter.add(1, { route: '/api/users' })
```

## When to Use
- Microservices observability
- Distributed tracing
- Multi-vendor telemetry
- Standardized instrumentation

## Validation
1. Traces appear in collector
2. Metrics export correctly
3. Context propagation works across services
