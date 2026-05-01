---
name: argocd-rollback
description: Выполняет автоматический и ручной откат (rollback) деплоев в Kubernetes через ArgoCD. Используется для быстрого восстановления при сбоях.
category: devops
tags: [argocd, rollback, kubernetes, gitops, recovery]
models: [opus]
version: 1.0.0
created: 2026-05-01
---
# ArgoCD Rollback

> Быстрый откат деплоев в Kubernetes через ArgoCD.

## 🚀 Quick Start
```bash
# Просмотр истории деплоев
argocd app history myapp

# Ручной откат к предыдущей версии
argocd app rollback myapp

# Откат к конкретной ревизии
argocd app rollback myapp 3
```

## 📋 Когда использовать
- ✅ Сбой деплоя в production
- ✅ Нужен быстрый откат к стабильной версии
- ❌ Не использовать без ArgoCD и Kubernetes

## 🔧 Пошаговая инструкция
1. Проверь статус приложения: `argocd app get myapp`
2. Посмотри историю: `argocd app history myapp`
3. Выполни откат: `argocd app rollback myapp [REV]`
4. Убедись в восстановлении: `argocd app sync myapp`

## 📦 Зависимости
```bash
# Установить ArgoCD CLI
# https://argo-cd.readthedocs.io/en/stable/cli_installation/
```

## 🧪 Примеры
Input: `argocd app rollback myapp` → Output: Приложение откачено к предыдущей версии

## 🔗 Ресурсы
- [ArgoCD Rollback](https://argo-cd.readthedocs.io/en/stable/user-guide/commands/argocd_app_rollback/)
- [Примеры кода](./examples/)

## ✅ Валидация
1. Откат выполняется без ошибок
2. Приложение работает стабильно
3. Git история синхронизирована
