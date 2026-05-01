---
name: airflow-dags
description: Создает DAGs для Apache Airflow с задачами и расписанием. Используется для оркестрации ETL пайплайнов.
category: data
tags: [airflow, dags, orchestration, etl, python]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-01
---
# Airflow DAGs

> Оркестрация рабочих процессов с Apache Airflow.

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

## 📋 Когда использовать
- ✅ Оркестрация сложных ETL процессов
- ✅ Расписание задач с зависимостями
- ❌ Не использовать для простых скриптов

## 🔧 Пошаговая инструкция
1. Установи Airflow: `pip install apache-airflow`
2. Инициализируй БД: `airflow db init`
3. Создай DAG файл в `dags/`
4. Запусти веб-сервер: `airflow webserver`

## 📦 Зависимости
```bash
pip install apache-airflow
```

## 🧪 Примеры
Input: Запуск DAG → Output: Задачи выполняются по расписанию

## 🔗 Ресурсы
- [Airflow Docs](https://airflow.apache.org/docs/)
- [Примеры кода](./examples/)

## ✅ Валидация
1. DAG валидируется без ошибок
2. Задачи выполняются в правильном порядке
3. Расписание работает корректно
