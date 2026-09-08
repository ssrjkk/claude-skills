---
name: few-shot-learning
description: "Designs and curates few-shot examples to guide LLM behavior, including example selection, formatting, and ordering. Use for task specification without fine-tuning."
category: ai
tags: [few-shot-learning, ai, russian]
models: [sonnet, opus]
version: "1.0"
language: ru
original: few-shot-learning
---
# Few-Shot Learning (Few-Shot обучение)

> Управление поведением LLM через тщательно подобранные примеры.

## Быстрый старт
```
Classify the sentiment of each review:

Review: "This product is amazing!"
Sentiment: Positive

Review: "Terrible experience, would not recommend."
Sentiment: Negative

Review: "It's okay, nothing special."
Sentiment: Neutral

Review: "Best purchase I've made all year!"
Sentiment:
```

## Когда использовать
- Обучение новым задачам без дообучения
- Задание формата вывода на примерах
- Обработка пограничных случаев
- Задание тона и стиля ответа

## Лучшие практики

### Выбор примеров
- Покрывайте edge cases и граничные условия
- Используйте 3-5 разнообразных примеров
- Показывайте и положительные, и отрицательные кейсы
- Располагайте от простого к сложному

### Форматирование
- Используйте одинаковый разделитель между примерами
- Явно разделяйте вход и выход
- Формат должен совпадать с реальным использованием

### Динамический выбор
- Для больших датасетов: извлекайте наиболее похожие примеры
- Используйте similarity эмбеддингов для выбора примеров
- Учитывайте лимиты контекстного окна

## Зависимости
```bash
pip install openai
# Для динамического выбора: pip install sentence-transformers
```

## Пошаговое руководство
1. Декомпозируйте задачу: определите форму входа/выхода и граничные кейсы.
2. Подберите 3-5 примеров: разнообразные пары, от простого к сложному, с edge cases и контрпримерами.
3. Единый формат: одинаковый разделитель между примерами, явные границы входа и выхода.
4. Уложитесь в контекст: держите примеры компактными; для больших корпусов берите топ-k по эмбеддингам.
5. Передайте примеры inline (few-shot) или в system message; формат цели — в последнем ходе.
6. Оцените: прогоните на отложенной выборке, сравните форматы и итерируйте, добавляя неудачные кейсы.

## Примеры
```python
# Динамический few-shot выбор через similarity эмбеддингов
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def select_examples(query: str, pool: list[tuple[str, str]], k: int = 3) -> list[tuple[str, str]]:
    # pool: список (prompt_example, answer_example) с эмбеддингами, посчитанными офлайн
    emb_q = model.encode(query)
    emb_pool = model.encode([p for p, _ in pool])
    idx = np.argsort([np.dot(emb_q, e) for e in emb_pool])[-k:][::-1]
    return [pool[i] for i in idx]
```
```txt
# Единый формат с явными маркерами
## Example 1
Input: "The movie was brilliant and moving."
Output: Positive

## Example 2
Input: "Waste of money, don't buy."
Output: Negative

## Example 3 (edge case)
Input: "Not bad at all."
Output: Positive
```

## Ресурсы
- [OpenAI Few-Shot Guide](https://platform.openai.com/docs/guides/prompt-engineering)

## Валидация
1. Модель стабильно следует паттернам примеров
2. Edge cases обрабатываются корректно
3. Добавление примеров повышает точность
4. Формат совпадает с примерами
