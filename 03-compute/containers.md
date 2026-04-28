# containers

**What it is**  
Упакованное приложение + зависимости. Изолировано, использует общий kernel. 

**Why it matters**  
Consistent dev/prod. Быстрый старт. Высокая плотность. 

**Must know**  
Docker: образы, слои, registry (ECR, GCR, ACR). ECS vs EKS vs GKE. 

**Must be able to do**  
Собрать Docker image. Push в registry. Деплоить в ECS/EKS. 

**Where it is used**  
Microservices, CI/CD pipelines, любой modern stack. 

**Trade-offs**  
+Consistency, +speed. -Complexity (K8s), -security overhead (daemon). 

**Common mistakes**  
Latest tag в продакшене. Образы по 2GB. Запуск как root. 

**Interview check**  
Q: ECS vs EKS? A: ECS проще (AWS-only). EKS = K8s standard (portable). 

**Mini example**  
Dockerfile: multi-stage build. Image 45MB вместо 800MB. Startup 0.3с.