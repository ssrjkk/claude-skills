---
name: etl-pipeline
description: Строит ETL пайплайны на Python с Pandas и SQLAlchemy. Используется для извлечения, трансформации и загрузки данных между системами.
category: data
tags: [etl, python, pandas, sqlalchemy, data-pipeline]
models: [sonnet, opus]
version: 1.0.0
created: 2026-04-29
---
# ETL Pipeline

> Построение ETL процессов для обработки и миграции данных.

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

## 📋 Когда использовать
- ✅ Миграция данных между БД
- ✅ Трансформация данных перед загрузкой
- ❌ Не использовать для потоковой обработки (лучше Kafka)

## 🔧 Пошаговая инструкция
1. Установи зависимости: `pip install pandas sqlalchemy`
2. Определи источник и приемник данных
3. Напиши функции extract, transform, load
4. Запусти: `python etl.py`

## 📦 Зависимости
```bash
pip install pandas sqlalchemy psycopg2-binary
```

## 🧪 Примеры
Input: CSV файл с данными → Output: Данные в PostgreSQL таблице

## 🔗 Ресурсы
- [Pandas Docs](https://pandas.pydata.org/)
- [Примеры кода](./examples/)

## ✅ Валидация
1. Данные успешно извлекаются из источника
2. Трансформации применяются корректно
3. Данные загружаются в целевую систему
