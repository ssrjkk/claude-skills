---
name: k8s-helm-deploy
description: Разворачивает приложения в Kubernetes с использованием Helm чартов и values оверрайдов. Используется для управления релизами в K8s.
category: devops
tags: [kubernetes, helm, deploy, devops]
models: [opus]
version: 1.0.0
created: 2026-04-29
---
# K8s Helm Deploy

> Управление деплоями в Kubernetes через Helm чарты.

## 🚀 Quick Start
```bash
# Добавить репозиторий
helm repo add bitnami https://charts.bitnami.com/bitnami

# Установить релиз с оверрайдом values
helm install my-release bitnami/nginx \
  --set service.type=ClusterIP \
  --set replicaCount=3

# Проверить статус
helm status my-release
```

## 📋 Когда использовать
- ✅ Деплой в Kubernetes
- ✅ Управление конфигурацией через values.yaml
- ❌ Не использовать без K8s кластера

## 🔧 Пошаговая инструкция
1. Создай Helm чарт: `helm create mychart`
2. Настрой templates/ и values.yaml
3. Установи: `helm install myapp ./mychart`
4. Обнови: `helm upgrade myapp ./mychart --set image.tag=v2`

## 📦 Зависимости
```bash
# Установить Helm
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash

# Установить kubectl
# https://kubernetes.io/docs/tasks/tools/
```

## 🧪 Примеры
Input: `helm install myapp ./chart --set replicaCount=3`
Output: 3 реплики приложения запущены в K8s

## 🔗 Ресурсы
- [Helm Docs](https://helm.sh/docs/)
- [Примеры кода](./examples/)

## ✅ Валидация
1. Релиз успешно установлен: `helm list`
2. Поды запущены: `kubectl get pods`
3. Сервис доступен по назначению
