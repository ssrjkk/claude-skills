---
name: gitops-argocd
description: "Implements GitOps approach for Kubernetes with ArgoCD, automatically syncing cluster state with Git."
category: devops
tags: [argocd, gitops, kubernetes, continuous-delivery]
models: [opus]
version: 1.0.0
created: 2026-04-29
---
# GitOps ArgoCD

> Automatic deployment to Kubernetes via GitOps with ArgoCD.

## 🚀 Quick Start
```bash
# Install ArgoCD in K8s
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

# Access UI
kubectl port-forward svc/argocd-server -n argocd 8080:443
```

## 📋 When to Use
- ✅ GitOps workflow for K8s
- ✅ Automatic deployment on Git changes
- ❌ Not without Kubernetes

## 🔧 Step-by-Step Instructions
1. Install ArgoCD in cluster
2. Create Application manifest pointing to Git repo
3. Configure sync (automatic or manual)
4. Monitor status in ArgoCD UI

## 📦 Dependencies
```bash
# Install ArgoCD CLI
# https://argo-cd.readthedocs.io/en/stable/cli_installation/
```

## 🧪 Examples
Input: Push changes to Git repo with manifests
Output: ArgoCD automatically updates deployment in K8s

## 🔗 Resources
- [ArgoCD Docs](https://argo-cd.readthedocs.io/)
- [Examples](./examples/)

## ✅ Validation
1. ArgoCD syncs with Git repository
2. Applications deployed to cluster
3. Rollback works correctly
