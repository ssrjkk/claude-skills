---
name: ml-model-training
description: Creates ML model training pipelines with scikit-learn and experiment tracking. Use for training and evaluating machine learning models.
category: data
tags: [ml, scikit-learn, training, model, pandas]
models: [opus]
version: 1.0.0
created: 2026-04-29
---
# ML Model Training#

> Train and evaluate ML models with experiment tracking.

## 🚀 Quick Start
```python
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load data
X, y = load_data()
X_train, X_test, y_train, y_test = train_test_split(X, y)

# Train
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluate
predictions = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, predictions)}")
```

## 📋 When to Use
- ✅ Training classical ML models
- ✅ Need experiment tracking
- ❌ Not for deep learning (better PyTorch/TensorFlow)

## 🔧 Step-by-Step Instructions
1. Prepare data and split train/test
2. Choose algorithm and hyperparameters
3. Train model and evaluate quality
4. Save model: `joblib.dump(model, 'model.pkl')`

## 📦 Dependencies
```bash
pip install scikit-learn pandas numpy
```

## 🧪 Examples
Input: Customer data → Output: Churn prediction model with 0.85 accuracy

## 🔗 Resources
- [Scikit-learn Docs](https://scikit-learn.org/)
- [Examples](./examples/)

## ✅ Validation
1. Model trains without errors
2. Quality metrics in expected range
3. Model saves and loads correctly
