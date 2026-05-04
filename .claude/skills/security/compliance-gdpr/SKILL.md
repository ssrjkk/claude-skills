---
name: compliance-gdpr
description: Checks application compliance with GDPR (General Data Protection Regulation) requirements. Use for compliance audit.
category: security
tags: [gdpr, compliance, privacy, legal]
models: [opus]
version: 1.0.0
created: 2026-04-29
---
# Compliance GDPR

> Check GDPR compliance for personal data processing.

## Quick Start
```
GDPR Compliance Checklist:

Data Collection:
  [ ] User consent obtained
  [ ] Data collected lawfully and fairly
  [ ] Purpose of data collection specified

User Rights:
  [ ] Right to access data
  [ ] Right to erasure (right to be forgotten)
  [ ] Right to data portability
```

## When to Use
- ✅ Processing personal data of EU citizens
- ✅ Compliance audit
- ❌ Not for anonymous data without PII

## Step-by-Step Instructions
1. Conduct Data Protection Impact Assessment (DPIA)
2. Check presence of cookie banner and privacy policy
3. Ensure implementation of user rights
4. Setup breach notification process

## Dependencies
```bash
# Tools: OneTrust, TrustArc
```

## Examples
Input: Website audit → Output: 3 GDPR violations found

## Resources
- [GDPR Official Text](https://gdpr-info.eu/)
- [Examples](./examples/)

## Validation
1. Application follows GDPR principles
2. Users can exercise their rights
3. DPIA documented correctly
