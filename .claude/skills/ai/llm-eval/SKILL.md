---
name: llm-eval
description: Оценивает качество работы LLM с использованием метрик BLEU, ROUGE и LLM-as-judge. Используется для тестирования моделей.
category: ai
tags: [llm, evaluation, metrics, bleu, rouge]
models: [opus]
version: 1.0.0
created: 2026-04-29
---
# LLM Evaluation

> Оценка качества LLM ответов с автоматическими метриками и LLM-as-judge.

## 🚀 Quick Start
```python
from rouge import Rouge

def evaluate_summary(reference, candidate):
    rouge = Rouge()
    scores = rouge.get_scores(candidate, reference)
    return scores[0]['rouge-l']['f']
```

## 📋 Когда использовать
- ✅ Тестирование качества LLM
- ✅ Сравнение разных моделей
- ❌ Не использовать для оценки точности классификаторов

## 🔧 Пошаговая инструкция
1. Подготовь тестовый датасет с эталонными ответами
2. Сгенерируй ответы тестируемой моделью
3. Посчитай метрики (BLEU, ROUGE, BERTScore)
4. Проведи LLM-as-judge оценку

## 📦 Зависимости
```bash
pip install rouge-score bert-score openai
```

## 🧪 Примеры
Input: reference="Привет", candidate="Привет!" → Output: ROUGE-L F1 = 0.95

## 🔗 Ресурсы
- [BLEU Score](https://en.wikipedia.org/wiki/BLEU)
- [Примеры кода](./examples/)

## ✅ Валидация
1. Метрики считаются корректно
2. Высокая корреляция с человеческой оценкой
3. Отчеты генерируются автоматически
