---
name: pytest
description: Writes Python tests with pytest, including fixtures, parameterization, and plugins for coverage.
category: qa
tags: [pytest, python, testing, fixtures, unit-test]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Pytest
> Python testing framework with fixtures and parameterized tests.
## Quick Start
```python
def test_add(): assert 1 + 1 == 2
def test_subtract(): assert 3 - 1 == 2
```
```bash
pytest test_calc.py -v
```
## Fixtures & Parameterization
```python
import pytest
@pytest.fixture
def db_connection(): conn = create_database(); yield conn; conn.close()
@pytest.mark.parametrize("input,expected", [(1, 2), (2, 4), (3, 6)])
def test_double(input, expected): assert input * 2 == expected
```
## When to Use
- Python unit tests; API testing; Data pipeline validation; TDD
## Validation
1. pytest discovers all tests; 2. Fixtures setup/teardown correctly; 3. Coverage reports
