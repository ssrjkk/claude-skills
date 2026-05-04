---
name: data-validation
description: Validates data quality with Great Expectations and Pandera. Use for data pipeline quality checks.
category: data
tags: [validation, data-quality, great-expectations, pandera]
models: [sonnet, opus]
version: 1.0.0
created: 2026-04-29
---
# Data Validation#

> Check data quality and schema compliance.

## 🚀 Quick Start
```python
import pandera as pa
from pandera import Column, Check

schema = pa.DataFrameSchema({
    "name": Column(str, Check(lambda s: s.str.len() > 0)),
    "age": Column(int, Check.in_range(0, 120))
})

df = pd.read_csv("data.csv")
validated_df = schema.validate(df)
```

## 📋 When to Use
- ✅ Data validation at pipeline entry
- ✅ Schema compliance checks
- ❌ Not for code validation

## 🔧 Step-by-Step Instructions
1. Define expectations for data (schemas, ranges)
2. Setup validators with Great Expectations or Pandera
3. Run checks before processing
4. Analyze quality reports

## 📦 Dependencies
```bash
pip install pandera great-expectations pandas
```

## 🧪 Examples
Input: DataFrame with invalid age → Output: Validation error

## 🔗 Resources
- [Pandera Docs](https://pandera.readthedocs.io/)
- [Great Expectations](https://docs.greatexpectations.io/)
- [Examples](./examples/)

## ✅ Validation
1. Invalid data caught by validators
2. Reports generated correctly
3. Validation doesn't miss anomalies
