---
name: data-validation
description: Валидирует качество данных с Great Expectations и Pandera. Используется для проверки данных в пайплайнах и обеспечения качества.
category: data
tags: [validation, data-quality, great-expectations, pandera]
models: [sonnet, opus]
version: 1.0.0
created: 2026-04-29
---
# Data Validation

> Проверка качества и соответствия данных схемам и ожиданиям.

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

## 📋 Когда использовать
- ✅ Валидация данных на входе пайплайна
- ✅ Проверка соответствия схеме БД
- ❌ Не использовать для валидации кода

## 🔧 Пошаговая инструкция
1. Определи ожидания от данных (схемы, диапазоны)
2. Настрой валидаторы с Great Expectations или Pandera
3. Запускай проверки перед обработкой
4. Анализируй отчеты о качестве

## 📦 Зависимости
```bash
pip install pandera great-expectations pandas
```

## 🧪 Примеры
Input: DataFrame с некорректным возрастом → Output: Ошибка валидации

## 🔗 Ресурсы
- [Pandera Docs](https://pandera.readthedocs.io/)
- [Great Expectations](https://docs.greatexpectations.io/)
- [Примеры кода](./examples/)

## ✅ Валидация
1. Некорректные данные отлавливаются
2. Отчеты генерируются корректно
3. Валидация не пропускает аномалии
