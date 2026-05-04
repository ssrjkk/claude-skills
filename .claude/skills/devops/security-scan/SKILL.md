---
name: security-scan
description: Integrates vulnerability scanning (Trivy, Snyk) into CI/CD pipelines. Use for checking Docker images and dependencies.
category: devops
tags: [security, scanning, trivy, snyk, devops]
models: [sonnet, opus]
version: 1.0.0
created: 2026-04-29
---
# Security Scan

> Vulnerability scanning for images and dependencies.

## 🚀 Quick Start
```bash
# Scan Docker image with Trivy
trivy image myapp:latest

# Scan dependencies with Snyk
snyk test
```

## 📋 When to Use
- ✅ Checking images before deployment
- ✅ Scanning dependencies for CVEs
- ❌ Not as sole security measure

## 🔧 Step-by-Step Instructions
1. Install scanners (Trivy, Snyk)
2. Add scanning steps to CI/CD
3. Configure policies (fail on critical)
4. Analyze reports and fix vulnerabilities

## 📦 Dependencies
```bash
# Trivy
brew install trivy

# Snyk
npm install -g snyk
```

## 🧪 Examples
Input: `trivy image myapp:latest`
Output: List of vulnerabilities with severity levels

## 🔗 Resources
- [Trivy Docs](https://trivy.dev/)
- [Snyk Docs](https://docs.snyk.io/)
- [Examples](./examples/)

## ✅ Validation
1. Scanners find known vulnerabilities
2. CI fails on critical vulnerabilities
3. Reports generated in machine-readable format
