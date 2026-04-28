# Test Reporting Examples

## Allure Annotation Example
```python
import allure

@allure.feature("User Management")
@allure.story("Create User")
def test_create_user():
    pass
```

## Custom Metrics
```python
def test_with_metrics():
    metrics = collect_metrics("allure-results")
    assert metrics["failed"] == 0
```
