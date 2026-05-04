---
name: selenium-grid
description: Sets up Selenium Grid for distributed web application testing. Use for parallel test execution.
category: qa
tags: [selenium, grid, testing, parallel, webdriver]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-01
---
# Selenium Grid

> Parallel test execution with Selenium Grid.

## Quick Start
```bash
# Start Selenium Grid
docker run -d -p 4444:4444 --name selenium-hub selenium/hub:4

# Register Chrome node
docker run -d --link selenium-hub:hub selenium/node-chrome:4
```

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    options=options
)
```

## When to Use
- ✅ Parallel test execution
- ✅ Cross-browser testing
- ❌ Not for simple E2E tests (better use Playwright)

## Step-by-Step Instructions
1. Download Selenium Server
2. Start Hub and nodes
3. Configure tests for Remote WebDriver
4. Run tests in parallel

## Dependencies
```bash
pip install selenium
# Download selenium-server.jar or use Docker
```

## Examples
Input: Running 10 tests → Output: Executed in parallel on nodes

## Resources
- [Selenium Grid Docs](https://www.selenium.dev/documentation/grid/)
- [Examples](./examples/)

## Validation
1. Grid accessible via HTTP
2. Nodes register successfully
3. Tests execute in parallel
