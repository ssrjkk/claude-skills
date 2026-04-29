---
name: ml-model-training
description: Создает пайплайны обучения ML моделей с scikit-learn и трекингом экспериментов. Используется для обучения и оценки моделей машинного обучения.
category: data
tags: [ml, scikit-learn, training, model, pandas]
models: [opus]
version: 1.0.0
created: 2026-04-29
---
# ML Model Training

> Обучение и оценка ML моделей с трекингом экспериментов.

## 🚀 Quick Start
```python
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Загрузка данных
X, y = load_data()
X_train, X_test, y_train, y_test = train_test_split(X, y)

# Обучение
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Оценка
predictions = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, predictions)}")
```

## 📋 Когда использовать
- ✅ Обучение классических ML моделей
- ✅ Нужен трекинг экспериментов
- ❌ Не использовать для глубокого обучения (лучше PyTorch/TensorFlow)

## 🔧 Пошаговая инструкция
1. Подготовь данные и раздели на train/test
2. Выбери алгоритм и гиперпараметры
3. Обучи модель и оцени качество
4. Сохрани модель: `joblib.dump(model, 'model.pkl')`

## 📦 Зависимости
```bash
pip install scikit-learn pandas numpy
```

## 🧪 Примеры
Input: Данные клиентов → Output: Модель предсказания оттока с accuracy 0.85

## 🔗 Ресурсы
- [Scikit-learn Docs](https://scikit-learn.org/)
- [Примеры кода](./examples/)

## ✅ Валидация
1. Модель обучается без ошибок
2. Метрики качества в ожидаемом диапазоне
3. Модель сохраняется и загружается корректно
