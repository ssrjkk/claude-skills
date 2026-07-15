---
name: cypress-e2e
description: "Creates E2E tests with Cypress for modern web applications. Use for fast testing with debugging."
category: qa
tags: [cypress, e2e, testing, javascript, typescript]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-01
---
# Cypress E2E

> E2E testing with Cypress for modern web applications.

## Quick Start
```javascript
describe('My First Test', () => {
  it('Does not do much!', () => {
    cy.visit('https://example.com')
    cy.contains('Example Domain').should('be.visible')
  })
})
```

## When to Use
- ✅ E2E testing of modern web apps
- ✅ Need real-time debugging
- ❌ Not for mobile applications

## Step-by-Step Instructions
1. Install: `npm install cypress --save-dev`
2. Open Cypress: `npx cypress open`
3. Create tests in `cypress/e2e/`
4. Run: `npx cypress run`

## Dependencies
```bash
npm install cypress --save-dev
```

## Examples
Input: Test run → Output: Test passes, screenshots saved

## Resources
- [Cypress Docs](https://docs.cypress.io/)
- [Examples](./examples/)

## Validation
1. Tests pass without errors
2. Screenshots/videos saved
3. Real-time debugging works
