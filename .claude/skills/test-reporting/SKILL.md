---
name: test-reporting
description: Generates test reports using Allure and pytest. Use for visualizing test results, tracking bugs, and team collaboration.
category: qa
tags: [testing, reporting, allure, pytest, qa, metrics]
models: [sonnet, opus]
version: 1.0.0
created: 2026-04-29
---
# Test Reporting

> Generate comprehensive test reports with Allure and pytest.

## 🚀 Quick Start
```bash
pip install pytest allure-pytest
pytest --alluredir=allure-results
allure serve allure-results
```

## 📋 When to Use
- ✅ Need visual test reports
- ✅ Tracking test failures and trends
- ❌ Not for simple test output (use pytest -v)

## 🔧 Step-by-Step Instructions
1. Install Allure CLI and pytest-allure
2. Run tests with `--alluredir` flag
3. Generate and open report: `allure serve allure-results`
4. Integrate with CI/CD for automated reporting

## 📦 Dependencies
```bash
pip install pytest allure-pytest
# Install Allure CLI: https://docs.qameta.io/allure/#install
```

## 🧪 Examples
Input: `pytest --alluredir=allure-results`
Output: Allure report with test results, trends, and categories

## 🔗 Resources
- [Allure Docs](https://docs.qameta.io/allure/)
- [Examples](./examples/)

## ✅ Validation
1. Allure report opens without errors
2. All test results displayed correctly
3. Metrics collected and saved
