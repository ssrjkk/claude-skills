---
name: kubernetes-ai
description: "Running AI workloads on Kubernetes"
category: devops
tags: [kubernetes, ai, ml, gpu, inference, training]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Kubernetes AI

> Deploy, scale, and manage AI/ML workloads on Kubernetes with GPU support.

## Quick Start
```yaml
# llm-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: llm-inference
spec:
  replicas: 2
  selector:
    matchLabels:
      app: llm-inference
  template:
    metadata:
      labels:
        app: llm-inference
    spec:
      containers:
      - name: ollama
        image: ollama/ollama:latest
        ports:
        - containerPort: 11434
        resources:
          requests:
            nvidia.com/gpu: 1
            memory: "16Gi"
            cpu: "4"
          limits:
            nvidia.com/gpu: 1
            memory: "32Gi"
            cpu: "8"
        volumeMounts:
        - name: models
          mountPath: /root/.ollama
      volumes:
      - name: models
        persistentVolumeClaim:
          claimName: ollama-models
---
apiVersion: v1
kind: Service
metadata:
  name: llm-service
spec:
  selector:
    app: llm-inference
  ports:
  - port: 11434
    targetPort: 11434
---
# GPU node pool configuration
apiVersion: karpenter.sh/v1beta1
kind: NodePool
metadata:
  name: gpu
spec:
  template:
    spec:
      requirements:
      - key: karpenter.k8s.aws/instance-family
        operator: In
        values: [g5, p4d, p5]
      - key: nvidia.com/gpu
        operator: Exists
  limits:
    cpu: 1000
    nvidia.com/gpu: 10
```

## Key Concepts
Use node pools with GPU instances, NVIDIA device plugin for GPU scheduling, PVCs for model storage, HPA for auto-scaling based on request latency/queue depth, and taints/tolerations for GPU-only pods.

## When to Use
- Production LLM inference at scale
- Multi-model serving with model versioning
- Batch inference jobs with GPU utilization optimization
- MLOps pipelines (training, evaluation, deployment)

## Validation
1. `kubectl describe pod` shows GPU allocated and NVIDIA drivers loaded
2. `kubectl logs` shows model loaded and API responding
3. HPA scales replicas based on load
4. Pods schedule on correct GPU node pool
