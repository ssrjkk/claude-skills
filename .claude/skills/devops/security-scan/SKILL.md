---
name: security-scan
description: Интегрирует сканирование уязвимостей (Trivy, Snyk) в CI/CD пайплайны. Используется для проверки Docker образов и зависимостей.
category: devops
tags: [security, scanning, trivy, snyk, devops]
models: [sonnet, opus]
version: 1.0.0
created: 2026-04-29
---
# Security Scan

> Сканирование уязвимостей в образах и зависимостях.

## 🚀 Quick Start
```bash
# Сканирование Docker образа с Trivy
trivy image myapp:latest

# Сканирование зависимостей с Snyk
snyk test
```

## 📋 Когда использовать
- ✅ Проверка образов перед деплоем
- ✅ Сканирование зависимостей на CVE
- ❌ Не использовать как единственный метод защиты

## 🔧 Пошаговая инструкция
1. Установи сканеры (Trivy, Snyk)
2. Добавь шаги сканирования в CI/CD
3. Настрой политики (fail on critical)
4. Анализируй отчеты и исправляй уязвимости

## 📦 Зависимости
```bash
# Trivy
brew install trivy

# Snyk
npm install -g snyk
```

## 🧪 Примеры
Input: `trivy image myapp:latest`
Output: Список уязвимостей с уровнями критичности

## 🔗 Ресурсы
- [Trivy Docs](https://trivy.dev/)
- [Snyk Docs](https://docs.snyk.io/)
- [Примеры кода](./examples/)

## ✅ Валидация
1. Сканеры находят известные уязвимости
2. CI падает при критических уязвимостях
3. Отчеты генерируются в машиночитаемом формате
