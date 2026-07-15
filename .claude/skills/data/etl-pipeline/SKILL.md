---
name: etl-pipeline
description: "Builds ETL pipelines with Python, Pandas, and SQLAlchemy. Use for extracting, transforming, and loading data between systems."
category: data
tags: [etl, python, pandas, sqlalchemy, data-pipeline]
models: [sonnet, opus]
version: 1.0.0
created: 2026-04-29
---
# ETL Pipeline#

> Build ETL processes for data processing and migration.

## 🚀 Quick Start
```python
import pandas as pd
from sqlalchemy import create_engine

def etl_process():
    # Extract
    df = pd.read_csv('source_data.csv')
    
    # Transform
    df['processed'] = df['value'] * 2
    
    # Load
    engine = create_engine('postgresql://user:pass@localhost/db')
    df.to_sql('target_table', engine, if_exists='append')
```

## 📋 When to Use
- ✅ Data migration between databases
- ✅ Transforming data before loading
- ❌ Not for streaming processing (better Kafka)

## 🔧 Step-by-Step Instructions
1. Install: `pip install pandas sqlalchemy`
2. Define source and target systems
3. Write extract, transform, load functions
4. Run: `python etl.py`

## 📦 Dependencies
```bash
pip install pandas sqlalchemy psycopg2-binary
```

## 🧪 Examples
Input: CSV file with data → Output: Data in PostgreSQL table

## 🔗 Resources
- [Pandas Docs](https://pandas.pydata.org/)
- [Examples](./examples/)

## ✅ Validation
1. Data extracted successfully from source
2. Transformations applied correctly
3. Data loaded into target system
