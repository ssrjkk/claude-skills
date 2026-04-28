# containers & Kubernetes

## Docker

**What it is**  
Платформа для контейнеризации. 

**Why it matters**  
Consistent dev/prod, быстрый деплой. 

**Must know**  
Images, containers, Dockerfile, registry. 

**Must be able to do**  
Написать Dockerfile. Собрать и push image. 

**Where it is used**  
Все modern apps. 

**Trade-offs**  
+Consistency. -Learning curve. 

**Common mistakes**  
Latest tag. root user. 

**Interview check**  
Q: Dockerfile CMD vs ENTRYPOINT? A: CMD может быть переопределен, ENTRYPOINT нет. 

**Mini example**  
Multi-stage build: image 50MB.

## ECS

**What it is**  
AWS container orchestration. 

**Why it matters**  
Простой способ запуска контейнеров на AWS. 

**Must know**  
Tasks, services, clusters. Fargate vs EC2 launch type. 

**Must be able to do**  
Деплоить service в ECS. 

**Where it is used**  
AWS-only environments. 

**Trade-offs**  
+Просто. -AWS lock-in. 

**Common mistakes**  
EC2 launch type без autoscaling. 

**Interview check**  
Q: Fargate vs EC2? A: Fargate serverless, EC2 вы управляете instances. 

**Mini example**  
Fargate: $0.04/vCPU-hour + $0.004/GB-hour.

## EKS

**What it is**  
AWS managed Kubernetes. 

**Why it matters**  
Standard K8s, portable. 

**Must know**  
Control plane (AWS), worker nodes (ваши). 

**Must be able to do**  
Создать EKS cluster. Деплоить pod. 

**Where it is used**  
Multi-cloud или K8s-native. 

**Trade-offs**  
+Portable. -Сложнее ECS. 

**Common mistakes**  
Нет node groups. 

**Interview check**  
Q: EKS vs ECS? A: EKS = K8s standard, ECS = AWS proprietary. 

**Mini example**  
EKS control plane: $0.10/час. Workers: EC2 costs.

## K8s basics

**What it is**  
Pods, services, deployments. 

**Why it matters**  
Основы работы с K8s. 

**Must know**  
Pod = 1+ containers. Service = stable endpoint. 

**Must be able to do**  
Написать deployment.yaml. 

**Where it is used**  
Все K8s clusters. 

**Trade-offs**  
+Standard. -Complex. 

**Common mistakes**  
Один pod на сервис (нет HA). 

**Interview check**  
Q: Pod vs Container? A: Pod может иметь несколько containers. 

**Mini example**  
Deployment: 3 replicas, rolling update.