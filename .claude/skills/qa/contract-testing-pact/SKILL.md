---
name: contract-testing-pact
description: Implements contract testing for APIs with Pact. Use for checking compatibility between services.
category: qa
tags: [contract-testing, pact, api, testing]
models: [sonnet, opus]
version: 1.0.0
created: 2026-04-29
---
# Contract Testing Pact

> Contract testing between microservices with Pact.

## Quick Start
```python
from pact import Consumer, Provider

pact = Consumer('ConsumerService').has_pact_with(
    Provider('ProviderService')
)

def test_user_api():
    pact.given('User exists') \
        .upon_receiving('a request for user') \
        .with_request('GET', '/users/1') \
        .will_respond_with(200, body={'id': 1, 'name': 'John'})
```

## When to Use
- ✅ Microservice architecture
- ✅ API contract verification
- ❌ Not for monoliths

## Step-by-Step Instructions
1. Install: `pip install pact`
2. Define consumer expectations
3. Create provider mock
4. Verify contract

## Dependencies
```bash
pip install pact pytest
```

## Examples
Input: Contract test → Output: Pact agreement file

## Resources
- [Pact Docs](https://docs.pact.io/)
- [Examples](./examples/)

## Validation
1. Contracts generated correctly
2. Verification passes successfully
3. Contract incompatibilities detected
