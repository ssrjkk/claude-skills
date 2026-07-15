---
name: great-expectations
description: "Validates data quality with Great Expectations, creating expectations, suites, and data docs."
category: data
tags: [great-expectations, data-quality, validation, testing, data-pipeline]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Great Expectations
> Data quality validation and documentation framework.
## Quick Start
```python
import great_expectations as gx
context = gx.get_context()
datasource = context.sources.add_pandas("my_data")
data_asset = datasource.add_dataframe_asset("my_asset")
batch_request = data_asset.build_batch_request(dataframe=df)
expectation_suite = context.add_expectation_suite("my_suite")
validator = context.get_validator(batch_request=batch_request, expectation_suite_name="my_suite")
validator.expect_column_values_to_not_be_null("user_id")
validator.expect_column_values_to_be_between("age", min_value=0, max_value=120)
validator.save_expectation_suite()
checkpoint = context.add_or_update_checkpoint(name="my_checkpoint", validator=validator)
checkpoint.run()
```
## When to Use
- Data pipeline quality gates; Data warehouse validation; ML data validation
## Validation
1. Expectations created; 2. Validation runs pass/fail; 3. Data docs generated
