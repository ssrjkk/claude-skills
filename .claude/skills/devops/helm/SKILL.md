---
name: helm
description: "Packages and deploys Kubernetes applications with Helm, including charts, templates, and releases."
category: devops
tags: [helm, kubernetes, charts, packaging, deployment]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Helm

> Kubernetes package manager with charts, templates, and release management.

## Quick Start
```bash
helm create my-app
helm install my-release ./my-app
helm list
```

## Chart Structure
```
my-app/
  Chart.yaml          # Metadata
  values.yaml         # Default configuration
  templates/          # K8s manifests with Go templates
    deployment.yaml
    service.yaml
    _helpers.tpl
```

## Go Templates
```yaml
apiVersion: apps/v1
kind: Deployment
spec:
  replicas: {{ .Values.replicaCount }}
  template:
    spec:
      containers:
        - name: {{ .Chart.Name }}
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
```

## When to Use
- Standardized Kubernetes deployments
- Multi-environment configurations
- Application package distribution
- CI/CD for Kubernetes

## Validation
1. helm lint passes without errors
2. helm template renders correct manifests
3. helm install creates resources successfully
