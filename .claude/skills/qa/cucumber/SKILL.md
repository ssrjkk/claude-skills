---
name: cucumber
description: Implements Behavior-Driven Development with Cucumber, Gherkin scenarios, and step definitions.
category: qa
tags: [cucumber, bdd, gherkin, testing, acceptance]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Cucumber
> BDD testing with Gherkin scenarios and step definitions.
## Quick Start
```gherkin
Feature: User Login
  Scenario: Successful login
    Given I am on the login page
    When I enter "user@example.com" as email
    And I enter "password123" as password
    And I click "Sign In"
    Then I should see the dashboard
```
## Step Definitions
```javascript
const { Given, When, Then } = require('@cucumber/cucumber')
Given('I am on the login page', async function () { await this.page.goto('https://example.com/login') })
Then('I should see the dashboard', async function () { await expect(this.page.locator('#dashboard')).toBeVisible() })
```
## When to Use
- Business-readable tests; ATDD; Cross-team communication; Living documentation
## Validation
1. Features parse without errors; 2. All scenarios pass; 3. Reports with pass/fail status
