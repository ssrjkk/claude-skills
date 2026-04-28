# CI/CD Examples

## With Allure Reporting
```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
      - run: pip install pytest allure-pytest
      - run: pytest --alluredir=allure-results
      - uses: simple-elf/allure-report-action@master
```
