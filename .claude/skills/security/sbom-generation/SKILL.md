---
name: sbom-generation
description: Генерирует Software Bill of Materials (SBOM) для отслеживания зависимостей и уязвимостей. Используется для supply chain безопасности.
category: security
tags: [sbom, supply-chain, security, dependencies]
models: [sonnet, opus]
version: 1.0.0
created: 2026-04-29
---
# SBOM Generation

> Генерация Software Bill of Materials для отслеживания компонентов.

## 🚀 Quick Start
```bash
# Генерация SBOM с Syft
syft dir:. -o cyclonedx-json=sbom.json

# Проверка SBOM
cat sbom.json | jq '.components[] | .name'
```

## 📋 Когда использовать
- ✅ Supply chain безопасность
- ✅ Комплаенс требования (US Executive Order)
- ❌ Не использовать как замену dependency scanning

## 🔧 Пошаговая инструкция
1. Установи Syft или Anchore
2. Сгенерируй SBOM для проекта/образа
3. Проверь структуру (CycloneDX, SPDX)
4. Интегрируй в CI/CD

## 📦 Зависимости
```bash
brew install syft
# или
curl -sSfL https://raw.githubusercontent.com/anchore/syft/main/install.sh | sh -s -- -b /usr/local/bin
```

## 🧪 Примеры
Input: `syft dir:.` → Output: JSON с списком всех зависимостей

## 🔗 Ресурсы
- [SBOM Guide](https://www.cisa.gov/sbom)
- [Примеры кода](./examples/)

## ✅ Валидация
1. SBOM содержит все прямые и транзитивные зависимости
2. Формат соответствует CycloneDX/SPDX
3. SBOM успешно парсится инструментами
