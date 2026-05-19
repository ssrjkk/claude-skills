---
name: kubernetes
description: Deploys and manages containerized applications on Kubernetes with pods, deployments, services, and ingress.
category: devops
tags: [kubernetes, k8s, containers, orchestration, deployment]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Kubernetes

> Container orchestration platform for deploying and scaling applications.

## Quick Start
```yaml
apiVersion: apps/v1; kind: Deployment; metadata: { name: nginx-deployment }
spec:
  replicas: 3; selector: { matchLabels: { app: nginx } }
  template:
    metadata: { labels: { app: nginx } }
    spec: { containers: [{ name: nginx, image: nginx:latest, ports: [{ containerPort: 80 }] }] }
```
```bash
kubectl apply -f deployment.yaml
```

## Services & Ingress
```yaml
apiVersion: v1; kind: Service; metadata: { name: nginx-service }
spec:
  type: LoadBalancer; selector: { app: nginx }
  ports: [{ port: 80, targetPort: 80 }]
```

## kubectl Essentials
```bash
kubectl get pods                    # List pods
kubectl logs -f deployment/nginx    # Follow logs
kubectl exec -it pod-name -- bash   # Shell into pod
kubectl port-forward svc/nginx 8080:80  # Port forward
kubectl delete all -l app=nginx     # Delete by label
```

## When to Use
- Container orchestration at scale
- Microservices deployments
- CI/CD pipelines
- Hybrid/multi-cloud apps

## Validation
1. kubectl get pods shows all pods running
2. Services are accessible
3. Rolling updates work without downtime
