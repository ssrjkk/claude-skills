---
name: vitest
description: Runs fast unit and integration tests with Vitest, featuring Vite-native speed and Jest-compatible API. Use for modern Vite projects.
category: qa
tags: [vitest, testing, vite, javascript, typescript]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Vitest

> Blazing-fast unit test framework powered by Vite.

## Quick Start
```javascript
// sum.test.js
import { describe, it, expect } from 'vitest'

function sum(a, b) { return a + b }

describe('sum', () => {
  it('adds numbers', () => {
    expect(sum(1, 2)).toBe(3)
  })
})
```

## When to Use
- Vite-based projects
- Vue/React/Svelte component testing
- TypeScript-native testing
- Fast feedback development

## Step-by-Step
1. Install: `npm install --save-dev vitest`
2. Add `"test": "vitest"` to package.json
3. Write tests with Jest-compatible API
4. Run: `npm test`

## Dependencies
```bash
npm install --save-dev vitest @vue/test-utils jsdom
```

## Examples
```javascript
import { mount } from '@vue/test-utils'
import Counter from './Counter.vue'

it('increments on click', async () => {
  const wrapper = mount(Counter)
  await wrapper.find('button').trigger('click')
  expect(wrapper.text()).toContain('1')
})
```

## Resources
- [Vitest Guide](https://vitest.dev/guide)

## Validation
1. Tests pass with `vitest run`
2. Watch mode works: `vitest`
3. Coverage generates: `vitest --coverage`
