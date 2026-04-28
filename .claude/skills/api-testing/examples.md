# API Testing Examples

## REST Example
```python
def test_create_user():
    client = APIClient("https://api.example.com")
    response = client.post("users", json={"name": "Test"})
    assert_status_code(response, 201)
```

## GraphQL Example
```python
def test_graphql_query():
    response = requests.post("https://api.example.com/graphql", json={"query": "{ users { id } }"})
    assert response.status_code == 200
```
