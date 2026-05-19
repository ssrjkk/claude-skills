---
name: puppeteer
description: Automates browser testing with Puppeteer, headless Chrome, and page interaction APIs.
category: qa
tags: [puppeteer, browser, automation, testing, headless]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Puppeteer
> Browser automation library for Node.js with headless Chrome.
## Quick Start
```javascript
import puppeteer from 'puppeteer'
const browser = await puppeteer.launch(); const page = await browser.newPage()
await page.goto('https://example.com'); await page.screenshot({ path: 'screenshot.png' })
await browser.close()
```
## Page Interaction
```javascript
await page.goto('https://example.com/login')
await page.type('#email', 'user@example.com'); await page.click('#submit')
await page.waitForNavigation(); const title = await page.title()
```
## When to Use
- Automated screenshots; PDF generation; E2E testing; Web scraping
## Validation
1. Browser launches headless; 2. Page interactions work; 3. Screenshots capture correctly
