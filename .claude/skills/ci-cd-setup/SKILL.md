---
name: ci-cd-setup
description: Sets up CI/CD pipelines for testing using GitHub Actions. Use for automating test runs, builds, and deployments to QA environments.
category: qa
tags: [ci-cd, github-actions, automation, testing, pytest, qa]
models: [haiku, sonnet, opus]
version: 1.0.0
created: 2026-04-29
---
# CI/CD Setup

> Automated testing pipelines with GitHub Actions.

## 🚀 Quick Start
```yaml
# .github/workflows/qa-tests.yml
name: QA Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
      - run: pip install pytest
      - run: pytest
```

## 📋 When to Use
- ✅ Automating test execution
- ✅ Building and deploying to QA environments
- ❌ Not for production deployments (use dedicated CD)

## 🔧 Step-by-Step Instructions
1. Create `.github/workflows/` folder in repo root
2. Write YAML pipeline with setup and test steps
3. Add PostgreSQL, Allure setup if needed
4. Commit and push - pipeline runs automatically

## 📦 Dependencies
```bash
# GitHub Actions (built-in)
# No installation needed
```

## 🧪 Examples
Input: Push to main branch
Output: Tests run automatically, results in GitHub UI

## 🔗 Resources
- [GitHub Actions Docs](https://docs.github.com/en/actions)
- [Examples](./examples/)

## ✅ Validation
1. Pipeline passes on push to branch
2. Tests run correctly, results visible
3. No YAML configuration errors
