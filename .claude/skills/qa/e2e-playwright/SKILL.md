---
name: e2e-playwright
description: "Creates E2E tests with Playwright and Allure report generation. Use for automated user scenario testing."
category: qa
tags: [e2e, playwright, testing, allure]
models: [sonnet, opus]
version: 1.0.0
created: 2026-04-29
---
# E2E Playwright

> Automated E2E testing with Playwright and Allure.

## Quick Start
```typescript
import { test, expect } from '@playwright/test';

test('basic test', async ({ page }) => {
    await page.goto('https://example.com');
    await expect(page.locator('h1')).toHaveText('Example Domain');
});
```

## When to Use
- ✅ E2E testing of web applications
- ✅ Need screenshots and videos on failures
- ❌ Not for unit tests

## Step-by-Step Instructions
1. Install: `npm init playwright@latest`
2. Create tests in `tests/` folder
3. Run: `npx playwright test`
4. Generate Allure report

## Dependencies
```bash
npm init playwright@latest
npm install allure-playwright
```

## Examples
Input: Test run → Output: Success, screenshot saved

## Resources
- [Playwright Docs](https://playwright.dev/)
- [Examples](./examples/)

## Validation
1. Tests pass without errors
2. Allure reports generated correctly
3. Screenshots/videos saved on failures
