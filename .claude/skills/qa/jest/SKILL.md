---
name: jest
description: Writes unit and integration tests with Jest, including mocks, snapshots, and code coverage. Use for JavaScript/TypeScript testing.
category: qa
tags: [jest, testing, javascript, typescript, unit-test]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Jest

> Delightful JavaScript testing with built-in mocking and assertions.

## Quick Start
```javascript
// sum.test.js
const sum = (a, b) => a + b;

test('adds 1 + 2 to equal 3', () => {
  expect(sum(1, 2)).toBe(3);
});
```

## When to Use
- Unit and integration tests
- React component testing
- API endpoint testing
- Snapshot testing

## Step-by-Step
1. Install: `npm install --save-dev jest`
2. Add `"test": "jest"` to package.json
3. Write tests in `*.test.js` files
4. Run: `npm test`

## Dependencies
```bash
npm install --save-dev jest @types/jest ts-jest
```

## Examples
```javascript
import axios from 'axios';
jest.mock('axios');

test('fetches users', async () => {
  axios.get.mockResolvedValue({ data: [{ id: 1 }] });
  const users = await fetchUsers();
  expect(users).toHaveLength(1);
});
```

## Resources
- [Jest Docs](https://jestjs.io/docs/getting-started)

## Validation
1. Tests pass with `npm test`
2. Coverage report generates
3. Mocks work correctly
