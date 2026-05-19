---
name: detox
description: Tests React Native applications E2E with Detox, gray box testing, and device synchronization.
category: qa
tags: [detox, react-native, e2e, mobile-testing, automation]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Detox
> Gray-box E2E testing for React Native apps.
## Quick Start
```javascript
describe('Login', () => {
  beforeAll(async () => { await device.launchApp() })
  it('should login successfully', async () => {
    await element(by.id('email-input')).typeText('user@example.com')
    await element(by.id('password-input')).typeText('password123')
    await element(by.id('login-button')).tap()
    await expect(element(by.id('welcome-screen'))).toBeVisible()
  })
})
```
## When to Use
- React Native E2E testing; CI/CD mobile testing; Cross-platform tests
## Validation
1. Detox builds the app correctly; 2. Tests run on simulator; 3. Element matching works
