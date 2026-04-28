# CI/CD

## Pipelines

**What it is**  
Автоматизированный процесс сборки, тестов, деплоя. 

**Why it matters**  
Быстрый и надежный релиз. 

**Must know**  
Stages: build -> test -> deploy. Artifacts. 

**Must be able to do**  
Настроить pipeline. 

**Where it is used**  
Все команды разработки. 

**Trade-offs**  
+Speed, +reliability. -Setup time. 

**Common mistakes**  
Нет тестов в pipeline. 

**Interview check**  
Q: CI vs CD? A: CI = continuous integration, CD = continuous deployment. 

**Mini example**  
GitHub Actions: build -> test -> deploy to ECS.

## GitHub Actions

**What it is**  
CI/CD от GitHub. 

**Why it matters**  
Интегрировано с GitHub, просто настроить. 

**Must know**  
Workflows, jobs, steps. Runners (GitHub-hosted, self-hosted). 

**Must be able to do**  
Написать workflow.yml. 

**Where it is used**  
GitHub repos. 

**Trade-offs**  
+Просто. -Лимиты на minutes. 

**Common mistakes**  
Секреты в workflow файле. 

**Interview check**  
Q: GitHub Actions secrets? A: Хранятся в repo settings, доступны как env vars. 

**Mini example**  
Build Docker image, push to ECR, deploy to ECS.

## ArgoCD

**What it is**  
GitOps tool для K8s. 

**Why it matters**  
Декларативный деплой, sync с git. 

**Must know**  
Application, project, repo. Auto-sync. 

**Must be able to do**  
Настроить ArgoCD application. 

**Where it is used**  
K8s deployments. 

**Trade-offs**  
+GitOps. -Дополнительный инструмент. 

**Common mistakes**  
Manual changes в кластере. 

**Interview check**  
Q: GitOps? A: Декларативное описание инфры в git, auto-sync. 

**Mini example**  
ArgoCD следит за k8s manifests в git, auto-deploy.

## Blue/Green

**What it is**  
Стратегия деплоя: две среды, переключение трафика. 

**Why it matters**  
Zero-downtime деплой, easy rollback. 

**Must know**  
Blue (old), Green (new). ALB routing. 

**Must be able to do**  
Настроить blue/green в CodeDeploy. 

**Where it is used**  
Критичные продакшн системы. 

**Trade-offs**  
+Rollback мгновенный. -Удвоение ресурсов. 

**Common mistakes**  
Ручное переключение. 

**Interview check**  
Q: Blue/Green vs Rolling? A: Blue/Green две среды, Rolling поочередная замена pods. 

**Mini example**  
CodeDeploy: blue/green, 5 мин test, switch 100% traffic.