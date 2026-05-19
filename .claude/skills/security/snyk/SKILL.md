---
name: snyk
description: Scans dependencies, containers, and IaC for vulnerabilities with Snyk in CI/CD pipelines.
category: security
tags: [snyk, vulnerability, dependencies, security-scanning, ci-cd]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Snyk
> Developer security platform for vulnerability scanning.
## Quick Start
```bash
npm install -g snyk; snyk auth; snyk test; snyk monitor
```
## Scanning Types
```bash
snyk test --all-projects          # Node.js / npm
snyk container test node:20        # Docker images
snyk iac test main.tf              # Terraform IaC
snyk test --severity-threshold=high # Only high/critical
```
## CI/CD Integration
```yaml
- name: Snyk Scan
  uses: snyk/actions/node@master
  env: { SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }} }
  with: { args: --severity-threshold=high }
```
## When to Use
- Open source scanning; Container scanning; IaC validation; License compliance
## Validation
1. snyk test finds vulnerabilities; 2. Fix PRs generated; 3. IaC scanning detects misconfigs
