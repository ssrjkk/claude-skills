---
name: cloud-native-ai
description: Cloud-native AI deployment patterns
category: devops
tags: [cloud-native, ai, kubernetes, inference, deployment]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Cloud-Native AI

> Deploy and scale AI workloads using cloud-native patterns with Kubernetes and containerization.

## Quick Start
```yaml
# model-serving.yaml — vLLM inference server
apiVersion: apps/v1
kind: Deployment
metadata:
  name: vllm-server
spec:
  replicas: 1
  selector:
    matchLabels:
      app: vllm
  template:
    metadata:
      labels:
        app: vllm
    spec:
      containers:
      - name: vllm
        image: vllm/vllm-openai:latest
        args: ["--model", "mistralai/Mistral-7B-v0.1"]
        env:
        - name: HUGGING_FACE_HUB_TOKEN
          valueFrom:
            secretKeyRef:
              name: hf-token
              key: token
        ports:
        - containerPort: 8000
        resources:
          limits:
            nvidia.com/gpu: 1
            memory: "32Gi"
            cpu: "8"
        readinessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 60
---
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: vllm-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: vllm-server
  minReplicas: 1
  maxReplicas: 10
  metrics:
  - type: Pods
    pods:
      metric:
        name: vllm:gpu_cache_usage_perc
      target:
        type: AverageValue
        averageValue: 80
  behavior:
    scaleDown:
      stabilizationWindowSeconds: 300
```

```bash
# Model inference with batching
curl -X POST http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "mistralai/Mistral-7B-v0.1",
    "messages": [{"role": "user", "content": "Hello"}],
    "max_tokens": 100
  }'
```

## Key Concepts
Cloud-native AI uses containers, orchestration, service mesh, and GitOps for ML deployment. Key patterns: model serving with vLLM/TGI, batch inference with Kueue/Volcano, model registries, and A/B testing with traffic splitting.

## When to Use
- Production AI services requiring high availability
- Multi-model serving infrastructure
- CI/CD for ML models with canary deployments
- GPU cluster management and scheduling

## Validation
1. Model deployment completes with health check passing
2. HPA scales based on GPU utilization
3. Rolling update deploys new model version without downtime
4. Batch inference jobs complete with correct results
