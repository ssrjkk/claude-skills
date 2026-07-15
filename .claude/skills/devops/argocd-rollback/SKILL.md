---
name: argocd-rollback
description: "Performs automatic and manual rollback of deployments in Kubernetes via ArgoCD. Use for quick recovery from failures."
category: devops
tags: [argocd, rollback, kubernetes, gitops, recovery]
models: [opus]
version: 1.0.0
created: 2026-05-01
---
# ArgoCD Rollback

> Quick rollback of deployments in Kubernetes via ArgoCD.

## 🚀 Quick Start
```bash
# View deployment history
argocd app history myapp

# Manual rollback to previous version
argocd app rollback myapp

# Rollback to specific revision
argocd app rollback myapp 3
```

## 📋 When to Use
- ✅ Deployment failure in production
- ✅ Need quick rollback to stable version
- ❌ Not without ArgoCD and Kubernetes

## 🔧 Step-by-Step Instructions
1. Check app status: `argocd app get myapp`
2. View history: `argocd app history myapp`
3. Perform rollback: `argocd app rollback myapp [REV]`
4. Verify recovery: `argocd app sync myapp`

## 📦 Dependencies
```bash
# Install ArgoCD CLI
# https://argo-cd.readthedocs.io/en/stable/user-guide/commands/argocd_app_rollback/
```

## 🧪 Examples
Input: `argocd app rollback myapp`
Output: Application rolled back to previous version

## 🔗 Resources
- [ArgoCD Rollback](https://argo-cd.readthedocs.io/en/stable/user-guide/commands/argocd_app_rollback/)
- [Examples](./examples/)

## ✅ Validation
1. Rollback executes without errors
2. Application working stably
3. Git history synchronized
