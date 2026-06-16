---
name: playwright-e2e-testing
description: Build robust automated E2E test suites using Playwright with cross-browser support and visual regression testing
category: qa
tags: [playwright, e2e, testing, automation, cross-browser]
models: [sonnet, opus]
version: "1.0"
language: en
---

# Playwright End-to-End Testing

## Overview
Build robust automated E2E test suites using Playwright with cross-browser support, visual regression testing, and CI/CD integration.

## Context
You are a QA engineer designing comprehensive test automation. You understand test design patterns, async operations, and reliability.

## Key Principles
- **Cross-Browser**: Test on Chrome, Firefox, Safari
- **Reliability**: Tests pass consistently
- **Speed**: Run in parallel
- **Maintenance**: Easy to update
- **Visibility**: Clear failure reporting

## Step-by-Step Instructions

### 1. Project Setup
```bash
npm init -y
npm install -D @playwright/test @testing-library/playwright
npx playwright install

# Directory structure
project/
  tests/
    auth.spec.ts
    dashboard.spec.ts
  tests/fixtures/
    auth.fixture.ts
  playwright.config.ts
```

### 2. Playwright Configuration
```typescript
// playwright.config.ts
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './tests',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 1 : undefined,
  reporter: 'html',
  use: {
    baseURL: 'http://localhost:3000',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
  },
  
  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
    {
      name: 'firefox',
      use: { ...devices['Desktop Firefox'] },
    },
    {
      name: 'webkit',
      use: { ...devices['Desktop Safari'] },
    },
  ],

  webServer: {
    command: 'npm run dev',
    url: 'http://localhost:3000',
    reuseExistingServer: !process.env.CI,
  },
});
```

### 3. Writing Tests
```typescript
import { test, expect, Page } from '@playwright/test';

test('login and view dashboard', async ({ page }) => {
  // Navigate
  await page.goto('/login');

  // Fill form
  await page.fill('input[name="email"]', 'user@example.com');
  await page.fill('input[name="password"]', 'password123');

  // Submit
  await page.click('button:has-text("Login")');

  // Wait for navigation
  await page.waitForURL('/dashboard');

  // Assert
  await expect(page).toHaveTitle('Dashboard');
  await expect(page.locator('h1')).toContainText('Welcome');
});

test('add item to cart', async ({ page }) => {
  await page.goto('/products');

  // Click and wait
  await page.click('[data-testid="product-1"]');
  await page.click('button:has-text("Add to Cart")');

  // Check cart badge
  const cartBadge = page.locator('[data-testid="cart-badge"]');
  await expect(cartBadge).toHaveText('1');
});
```

### 4. Advanced Selectors
```typescript
// Data attributes (best practice)
await page.click('[data-testid="submit-button"]');

// Text matching
await page.click('button:has-text("Click me")');

// Combining selectors
await page.click('form >> button >> text=Login');

// XPath (last resort)
await page.click('//button[@id="submit"]');

// CSS combinator
await page.click('nav > ul > li >> a');
```

### 5. Handling Async Operations
```typescript
test('wait for async data', async ({ page }) => {
  await page.goto('/data');

  // Wait for request and response
  const responsePromise = page.waitForResponse(
    response => response.url().includes('/api/data')
  );
  
  await page.click('button:has-text("Load Data")');
  const response = await responsePromise;
  
  expect(response.status()).toBe(200);

  // Wait for element
  await page.waitForSelector('[data-testid="data-loaded"]');
  
  // Wait for function
  await page.waitForFunction(() => {
    return document.querySelectorAll('[data-testid="item"]').length > 0;
  });
});
```

## Real-World Examples

### Example 1: Complete E2E Flow
```typescript
import { test, expect } from '@playwright/test';

test.describe('E-commerce Checkout', () => {
  test.beforeEach(async ({ page }) => {
    // Login before each test
    await page.goto('/');
    await page.click('[data-testid="login"]');
    await page.fill('input[name="email"]', 'test@example.com');
    await page.fill('input[name="password"]', 'password');
    await page.click('button:has-text("Login")');
    await page.waitForURL('/');
  });

  test('complete purchase', async ({ page }) => {
    // Add product
    await page.goto('/products');
    await page.click('[data-testid="product-1"]');
    await page.click('button:has-text("Add to Cart")');

    // Checkout
    await page.goto('/cart');
    await page.click('button:has-text("Checkout")');

    // Fill address
    await page.fill('input[name="address"]', '123 Main St');
    await page.fill('input[name="city"]', 'New York');

    // Payment
    await page.frame({ name: 'iframe' }).fill('input[name="cardnumber"]', '4242424242424242');
    await page.click('button:has-text("Pay")');

    // Confirm
    await page.waitForURL('/order-confirmation');
    await expect(page.locator('h1')).toContainText('Thank you');
  });
});
```

### Example 2: Visual Regression Testing
```typescript
test('button appearance', async ({ page }) => {
  await page.goto('/');
  
  // Screenshot entire page
  await expect(page).toHaveScreenshot('homepage.png');
  
  // Screenshot component
  await expect(page.locator('button')).toHaveScreenshot('button.png');
});

// Update baseline
// npx playwright test --update-snapshots
```

### Example 3: API Response Mocking
```typescript
test('handle API error gracefully', async ({ page }) => {
  // Intercept API call
  await page.route('**/api/data', route => {
    route.abort('failed');  // Simulate failure
  });

  await page.goto('/data');
  
  // Should show error message
  await expect(page.locator('.error-message')).toContainText('Failed to load data');
});

test('mock API response', async ({ page }) => {
  await page.route('**/api/users', route => {
    route.fulfill({
      status: 200,
      body: JSON.stringify([
        { id: 1, name: 'John' },
        { id: 2, name: 'Jane' }
      ])
    });
  });

  await page.goto('/users');
  
  // Should display mocked data
  await expect(page.locator('text=John')).toBeVisible();
});
```

## Best Practices
- ✅ Use data attributes for selectors
- ✅ Wait for elements explicitly
- ✅ Use meaningful test names
- ✅ Keep tests independent
- ✅ Run in parallel
- ✅ Mock external APIs
- ✅ Use fixtures for setup
- ❌ Don't use timeouts instead of waits
- ❌ Don't test implementation details
- ❌ Don't make tests interdependent

## Advanced Patterns

### Fixtures and Page Objects
```typescript
// fixtures/auth.fixture.ts
import { test as base } from '@playwright/test';

export const test = base.extend({
  authenticatedPage: async ({ page }, use) => {
    // Login
    await page.goto('/login');
    await page.fill('input[name="email"]', 'test@example.com');
    await page.fill('input[name="password"]', 'password');
    await page.click('button:has-text("Login")');
    
    // Use authenticated page
    await use(page);
  },
});

// Usage
test('view dashboard', async ({ authenticatedPage }) => {
  await authenticatedPage.goto('/dashboard');
  // Already authenticated
});
```

### Performance Testing
```typescript
test('page loads quickly', async ({ page }) => {
  const startTime = Date.now();
  
  await page.goto('/');
  
  const loadTime = Date.now() - startTime;
  expect(loadTime).toBeLessThan(3000);  // 3 second limit
});
```

## Metrics to Track
- Test pass rate
- Execution time (should be < 30 min)
- Code coverage
- Failure reasons
- Flaky test rate

## Common Pitfalls
1. **Hard timeouts**: Use explicit waits
2. **Over-mocking**: Too much mocking = unrealistic
3. **Slow tests**: Too many tests in sequence
4. **Brittle selectors**: Change with UI
5. **No retries**: Flaky tests fail CI

## Running Tests
```bash
# Run all tests
npx playwright test

# Run specific file
npx playwright test tests/auth.spec.ts

# Run with browser UI
npx playwright test --ui

# Debug mode
npx playwright test --debug

# Generate report
npx playwright show-report
```

## CI/CD Integration
```yaml
# GitHub Actions
name: Playwright Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '18'
      - run: npm ci
      - run: npx playwright install --with-deps
      - run: npm run test:e2e
      - uses: actions/upload-artifact@v4
        if: always()
        with:
          name: playwright-report
          path: playwright-report/
```

## Related Skills
- qa-testing-jest-unit-tests
- frontend-react-core-concepts
- devops-github-actions-ci-cd
