def assert_status_code(response, expected_code):
    assert response.status_code == expected_code, f"Expected {expected_code}, got {response.status_code}"

def assert_json_contains(response, key):
    assert key in response.json(), f"Response JSON missing key: {key}"
