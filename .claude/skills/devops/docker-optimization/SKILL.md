---
name: docker-optimization
description: Оптимизирует Docker образы с multi-stage сборкой, кэшированием слоев и уменьшением размера. Используется для ускорения CI/CD и экономии диска.
category: devops
tags: [docker, optimization, multi-stage, caching]
models: [sonnet, opus]
version: 1.0.0
created: 2026-04-29
---
# Docker Optimization

> Создание минимальных, безопасных и быстрых Docker образов.

## 🚀 Quick Start
```dockerfile
# Multi-stage build
FROM node:alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
EXPOSE 80
```

## 📋 Когда использовать
- ✅ Нужно уменьшить размер образа
- ✅ Ускорение сборки через кэширование
- ❌ Не использовать для простых однофайловых скриптов

## 🔧 Пошаговая инструкция
1. Используй multi-stage сборку (builder + runtime)
2. Правильно расставляй COPY/RUN для кэширования слоев
3. Используй .dockerignore для исключения лишнего
4. Собери: `docker build -t myapp:optimized .`

## 📦 Зависимости
```bash
# Установить Docker
# Windows: https://docs.docker.com/desktop/install/windows-install/
# Mac: https://docs.docker.com/desktop/install/mac-install/
# Linux: https://docs.docker.com/engine/install/
```

## 🧪 Примеры
Input: `docker build -t myapp .` с оптимизированным Dockerfile
Output: Образ размером < 50MB вместо > 500MB

## 🔗 Ресурсы
- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)
- [Примеры кода](./examples/)

## ✅ Валидация
1. Размер образа уменьшился минимум на 50%
2. Контейнер запускается и работает корректно
3. В образе нет исходного кода или dev-зависимостей
