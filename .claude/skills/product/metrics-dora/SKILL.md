---
name: metrics-dora
description: "Calculates DORA metrics (Deployment Frequency, Lead Time, MTTR, CFR) for teams. Use for evaluating DevOps effectiveness."
category: product
tags: [dora, metrics, devops, performance]
models: [sonnet, opus]
version: 1.0.0
created: 2026-04-29
---
# Metrics DORA

> Calculate and analyze DORA metrics for team performance evaluation.

## Quick Start
```python
# Calculate DORA metrics
deployments_per_day = 5
lead_time_hours = 24
mttr_hours = 2
change_failure_rate = 0.05

print(f"Deployment Frequency: {deployments_per_day}/day")
print(f"Lead Time: {lead_time_hours}h")
print(f"MTTR: {mttr_hours}h")
print(f"CFR: {change_failure_rate*100}%")
```

## When to Use
- ✅ Evaluate DevOps maturity
- ✅ Track team improvements
- ❌ Not for evaluating individual developers

## Step-by-Step Instructions
1. Collect data from CI/CD and incident management
2. Calculate 4 DORA metrics
3. Compare with industry benchmarks
4. Create improvement plan

## Dependencies
```bash
pip install pandas matplotlib
```

## Examples
Input: Quarterly data → Output: "Elite" level on DORA

## Resources
- [DORA Research](https://cloud.google.com/devops/state-of-devops/)
- [Examples](./examples/)

## Validation
1. Metrics calculated correctly
2. Data collected from reliable sources
3. Comparison with benchmarks done
