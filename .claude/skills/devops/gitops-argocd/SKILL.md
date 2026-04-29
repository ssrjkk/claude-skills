---
name: gitops-argocd
description: Реализует GitOps подход для Kubernetes с ArgoCD, автоматически синхронизируя состояние кластера с Git репозиторием.
category: devops
tags: [argocd, gitops, kubernetes, continuous-delivery]
models: [opus]
version: 1.0.0
created: 2026-04-29
---
# GitOps ArgoCD

> Автоматический деплой в Kubernetes через GitOps с ArgoCD.

## 🚀 Quick Start
```bash
# Установка ArgoCD в K8s
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

# Доступ к UI
kubectl port-forward svc/argocd-server -n argocd 8080:443
```

## 📋 Когда использовать
- ✅ GitOps workflow для K8s
- ✅ Автоматический деплой при изменениях в Git
- ❌ Не использовать без Kubernetes

## 🔧 Пошаговая инструкция
1. Установи ArgoCD в кластер
2. Создай Application манифест с ссылкой на Git repo
3. Настрой синхронизацию (автоматическую или ручную)
4. Мониторь статус в ArgoCD UI

## 📦 Зависимости
```bash
# Установить ArgoCD CLI
# https://argo-cd.readthedocs.io/en/stable/cli_installation/
```

## 🧪 Примеры
Input: Пуш изменений в Git репозиторий с манифестами
Output: ArgoCD автоматически обновляет деплой в K8s

## 🔗 Ресурсы
- [ArgoCD Docs](https://argo-cd.readthedocs.io/)
- [Примеры кода](./examples/)

## ✅ Валидация
1. ArgoCD синхронизируется с Git репозиторием
2. Приложения задеплоены в кластер
3. Rollback работает корректно
