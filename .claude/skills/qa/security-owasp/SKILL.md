---
name: security-owasp
description: Checks web applications for OWASP Top 10 compliance. Use for security testing.
category: qa
tags: [security, owasp, testing, vulnerability]
models: [opus]
version: 1.0.0
created: 2026-04-29
---
# Security OWASP

> Web application security testing with OWASP Top 10.

## Quick Start
```bash
# Scan with OWASP ZAP
docker run -t ghcr.io/zaproxy/zaproxy:stable zap-baseline.py \
  -t https://example.com
```

## When to Use
- ✅ Security audit of web applications
- ✅ Check for OWASP Top 10 vulnerabilities
- ❌ Not for load testing

## Step-by-Step Instructions
1. Run ZAP baseline scan
2. Analyze report for vulnerabilities
3. Fix identified issues
4. Run rescan

## Dependencies
```bash
docker pull ghcr.io/zaproxy/zaproxy:stable
```

## Examples
Input: `zap-baseline.py -t https://myapp.com` → Output: Report with found vulnerabilities

## Resources
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Examples](./examples/)

## Validation
1. Scanner finds known vulnerabilities
2. Reports generated in machine-readable format
3. Rescan shows fixes applied
