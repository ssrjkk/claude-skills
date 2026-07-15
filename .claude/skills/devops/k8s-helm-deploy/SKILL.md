---
name: k8s-helm-deploy
description: "Deploys applications to Kubernetes using Helm charts and values overrides. Use for managing releases in K8s."
category: devops
tags: [kubernetes, helm, deploy, devops]
models: [opus]
version: 1.0.0
created: 2026-04-29
---
# K8s Helm Deploy

> Manage Kubernetes deployments via Helm charts.

## 🚀 Quick Start
```bash
# Add repo
helm repo add bitnami https://charts.bitnami.com/bitnami

# Install release with overrides
helm install my-release bitnami/nginx \
  --set service.type=ClusterIP \
  --set replicaCount=3

# Check status
helm status my-release
```

## 📋 When to Use
- ✅ Deploying to Kubernetes
- ✅ Managing configuration via values.yaml
- ❌ Not without K8s cluster

## 🔧 Step-by-Step Instructions
1. Create Helm chart: `helm create mychart`
2. Configure templates/ and values.yaml
3. Install: `helm install myapp ./mychart`
4. Upgrade: `helm upgrade myapp ./mychart --set image.tag=v2`

## 📦 Dependencies
```bash
# Install Helm
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash

# Install kubectl
# https://kubernetes.io/docs/tasks/tools/
```

## 🧪 Examples
Input: `helm install myapp ./chart --set replicaCount=3`
Output: 3 replicas of application running in K8s

## 🔗 Resources
- [Helm Docs](https://helm.sh/docs/)
- [Examples](./examples/)

## ✅ Validation
1. Release installed successfully: `helm list`
2. Pods running: `kubectl get pods`
3. Service accessible as intended
