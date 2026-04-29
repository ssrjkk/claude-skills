---
name: metrics-dora
description: Рассчитывает DORA метрики (Deployment Frequency, Lead Time, MTTR, CFR) для команд. Используется для оценки эффективности DevOps.
category: product
tags: [dora, metrics, devops, performance]
models: [sonnet, opus]
version: 1.0.0
created: 2026-04-29
---
# Metrics DORA

> Расчет и анализ DORA метрик для оценки производительности команды.

## 🚀 Quick Start
```python
# Расчет DORA метрик
deployments_per_day = 5
lead_time_hours = 24
mttr_hours = 2
change_failure_rate = 0.05

print(f"Deployment Frequency: {deployments_per_day}/day")
print(f"Lead Time: {lead_time_hours}h")
print(f"MTTR: {mttr_hours}h")
print(f"CFR: {change_failure_rate*100}%")
```

## 📋 Когда использовать
- ✅ Оценка DevOps зрелости
- ✅ Трекинг улучшений команды
- ❌ Не использовать для оценки отдельных разработчиков

## 🔧 Пошаговая инструкция
1. Собери данные из CI/CD и incident management
2. Рассчитай 4 DORA метрики
3. Сравни с индустриальными бенчмарками
4. Создай план улучшений

## 📦 Зависимости
```bash
pip install pandas matplotlib
```

## 🧪 Примеры
Input: Данные за квартал → Output: "Elite" уровень по DORA

## 🔗 Ресурсы
- [DORA Research](https://cloud.google.com/devops/state-of-devops/)
- [Примеры кода](./examples/)

## ✅ Валидация
1. Метрики рассчитаны корректно
2. Данные собраны из надежных источников
3. Сравнение с бенчмарками проведено
