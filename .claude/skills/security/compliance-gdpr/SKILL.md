---
name: compliance-gdpr
description: Проверяет соответствие приложений требованиям GDPR (General Data Protection Regulation). Используется для compliance аудита.
category: security
tags: [gdpr, compliance, privacy, legal]
models: [opus]
version: 1.0.0
created: 2026-04-29
---
# Compliance GDPR

> Проверка соответствия GDPR требованиям для обработки персональных данных.

## 🚀 Quick Start
```
GDPR Compliance Checklist:

Data Collection:
  [ ] Есть согласие пользователя (consent)
  [ ] Данные собираются законно и справедливо
  [ ] Указана цель сбора данных

User Rights:
  [ ] Право на доступ к данным
  [ ] Право на удаление (right to be forgotten)
  [ ] Право на перенос данных
```

## 📋 Когда использовать
- ✅ Обработка персональных данных EU граждан
- ✅ Compliance аудит
- ❌ Не использовать для анонимных данных без PII

## 🔧 Пошаговая инструкция
1. Проведи Data Protection Impact Assessment (DPIA)
2. Проверь наличие cookie banner и privacy policy
3. Убедись в реализации user rights
4. Настрой breach notification процесс

## 📦 Зависимости
```bash
# Инструменты: OneTrust, TrustArc
```

## 🧪 Примеры
Input: Аудит веб-сайта → Output: 3 нарушения GDPR найдено

## 🔗 Ресурсы
- [GDPR Official Text](https://gdpr-info.eu/)
- [Примеры кода](./examples/)

## ✅ Валидация
1. Приложение соблюдает принципы GDPR
2. Пользователь может реализовать свои права
3. DPIA документирован корректно
