---
name: pandas
description: Manipulates and analyzes data with pandas, including DataFrames, group operations, and time series.
category: data
tags: [pandas, python, dataframe, data-analysis, csv]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Pandas

> Data manipulation and analysis library for Python.

## Quick Start
```python
import pandas as pd
df = pd.read_csv('data.csv')
df.info(); df.describe(); df['category'].value_counts()
```

## Selection & Grouping
```python
df[df['price'] > 100]                              # Filter
df.groupby('category').agg({'price': ['mean', 'std'], 'quantity': 'sum'})
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True).resample('M').mean()  # Time series
```

## When to Use
- CSV/Excel data analysis
- Data cleaning and transformation
- Time series analysis
- ETL pipeline development

## Validation
1. DataFrame operations execute correctly
2. GroupBy aggregations return expected values
3. Missing values handled properly
