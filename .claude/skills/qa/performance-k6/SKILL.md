---
name: performance-k6
description: "Conducts load testing of APIs and web applications with k6. Use for performance validation under load."
category: qa
tags: [performance, k6, load-testing, qa]
models: [sonnet, opus]
version: 1.0.0
created: 2026-04-29
---
# Performance k6

> Load testing with k6 and performance metrics analysis.

## Quick Start
```javascript
import http from 'k6/http';
import { check, sleep } from 'k6';

export default function() {
    let res = http.get('https://example.com');
    check(res, { 'status was 200': (r) => r.status == 200 });
    sleep(1);
}
```

## When to Use
- ✅ Load testing APIs
- ✅ Performance validation under load
- ❌ Not for functional testing

## Step-by-Step Instructions
1. Install k6: `brew install k6`
2. Write load scenario
3. Run: `k6 run script.js`
4. Analyze metrics in report

## Dependencies
```bash
# Windows: https://k6.io/docs/getting-started/installation/
# Mac: brew install k6
# Linux: sudo apt-get install k6
```

## Examples
Input: `k6 run load-test.js` → Output: Metrics: avg response time, p95, error rate

## Resources
- [k6 Docs](https://k6.io/docs/)
- [Examples](./examples/)

## Validation
1. Test runs without errors
2. Metrics collected correctly
3. Thresholds trigger when limits exceeded
