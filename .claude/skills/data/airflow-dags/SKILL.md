---
name: airflow-dags
description: Creates DAGs for Apache Airflow with tasks and scheduling. Use for ETL pipeline orchestration.
category: data
tags: [airflow, dags, orchestration, etl, python]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-01
---
# Airflow DAGs#

> Orchestrate workflows with Apache Airflow.

## 🚀 Quick Start
```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def print_hello():
    return 'Hello from Airflow!'

dag = DAG(
    'hello_world_dag',
    start_date=datetime(2026, 1, 1),
    schedule_interval='@daily'
)

task = PythonOperator(
    task_id='print_hello',
    python_callable=print_hello,
    dag=dag
)
```

## 📋 When to Use
- ✅ Orchestrating complex ETL processes
- ✅ Scheduling tasks with dependencies
- ❌ Not for simple scripts#

## 🔧 Step-by-Step Instructions
1. Install Airflow: `pip install apache-airflow`
2. Initialize DB: `airflow db init`
3. Create DAG file in `dags/`
4. Start webserver: `airflow webserver`

## 📦 Dependencies
```bash
pip install apache-airflow
```

## 🧪 Examples
Input: Trigger DAG → Output: Tasks execute on schedule

## 🔗 Resources
- [Airflow Docs](https://airflow.apache.org/docs/)
- [Examples](./examples/)

## ✅ Validation
1. DAG validates without errors
2. Tasks execute in correct order#
3. Schedule works correctly
