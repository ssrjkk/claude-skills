---
name: security-owasp
description: Проводит проверку веб-приложений на соответствие OWASP Top 10. Используется для security-тестирования.
category: qa
tags: [security, owasp, testing, vulnerability]
models: [opus]
version: 1.0.0
created: 2026-04-29
---
# Security OWASP

> Проверка безопасности веб-приложений по OWASP Top 10.

## 🚀 Quick Start
```bash
# Сканирование с OWASP ZAP
docker run -t owasp/zap2docker zap-baseline.py \
  -t https://example.com
```

## 📋 Когда использовать
- ✅ Security-аудит веб-приложений
- ✅ Проверка на OWASP Top 10 уязвимости
- ❌ Не использовать для нагрузочного тестирования

## 🔧 Пошаговая инструкция
1. Запусти ZAP baseline scan
2. Проанализируй отчет на уязвимости
3. Исправь найденные проблемы
4. Проведи повторное сканирование

## 📦 Зависимости
```bash
docker pull owasp/zap2docker
```

## 🧪 Примеры
Input: `zap-baseline.py -t https://myapp.com` → Output: Отчет с найденными уязвимостями

## 🔗 Ресурсы
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Примеры кода](./examples/)

## ✅ Валидация
1. Сканер находит известные уязвимости
2. Отчеты генерируются в машиночитаемом формате
3. Повторный скан показывает исправления
