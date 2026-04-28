# cloud-skills

[![GitHub Stars](https://img.shields.io/github/stars/ssrjkk/claude-skills?style=social)](https://github.com/ssrjkk/claude-skills)
[![GitHub Last Commit](https://img.shields.io/github/last-commit/ssrjkk/claude-skills)](https://github.com/ssrjkk/claude-skills)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

**Внутренняя инженерная база знаний для Cloud-инженеров, SRE, DevOps и архитекторов.**  
Практический справочник без воды. Только use-cases, trade-offs и готовые решения.

---

## Оглавление

- [Для кого этот репозиторий](#для-кого-этот-репозиторий)
- [Структура репозитория](#структура-репозитория)
- [Быстрый старт](#быстрый-старт)
- [Стек технологий](#стек-технологий)
- [Как внести вклад](#как-внести-вклад)
- [Контакты](#контакты)

---

## Для кого этот репозиторий

| Роль | Зачем здесь |
| :--- | :--- |
| **Junior** | База знаний для старта, подготовка к собеседованиям. |
| **Middle** | Шпаргалка по сервисам, паттернам и IaC. |
| **Senior** | Архитектурные развилки, SRE-практики, Disaster Recovery. |
| **Staff/Principal** | Стратегии миграции, Governance, мульти-клауд. |

---

## Структура репозитория

### 1. Core Fundamentals (`01-core-fundamentals`)
Фундаментальные понятия облачных вычислений.
- `iaas-paas-saas.md` — уровни абстракции и когда что использовать.
- `public-private-hybrid.md` — типы облаков, регуляции и цена.
- `regions-az-edge.md` — география, HA и латентность.
- `scalability-elasticity.md` — вертикальное и горизонтальное масштабирование.
- `ha-ft-dr.md` — High Availability, Fault Tolerance и Disaster Recovery.
- `shared-responsibility.md` — модель разделения ответственности.
- `cap-theorem.md` — CAP теорема на практике.
- `consistency-models.md` — Strong vs Eventual Consistency.
- `latency-throughput-availability.md` — метрики производительности.
- `stateless-vs-stateful.md` — проектирование отказоустойчивых систем.

### 2. Cloud Providers (`02-cloud-providers`)
Сравнение ведущих провайдеров.
- `aws.md` — глубокое погружение в экосистему Amazon.
- `gcp.md` — Kubernetes, BigQuery и глобальная сеть Google.
- `azure.md` — Enterprise интеграция и гибридное облако.
- `service-mapping.md` — таблица соответствия сервисов (AWS <-> GCP <-> Azure).
- `vendor-lockin.md` — уровни зависимости и способы митигации.
- `multi-cloud.md` — реальность мульти-облачных архитектур.

### 3. Compute (`03-compute`)
Ресурсы для вычислений.
- `virtual-machines.md` — EC2, Compute Engine, оптимизация стоимости.
- `autoscaling.md` — группы автомасштабирования и политики.
- `load-balancing.md` — ALB vs NLB, распределение трафика.
- `serverless-functions.md` — Lambda, Cloud Functions, cold starts.
- `containers.md` — Docker, образы, плотность размещения.

### 4. Networking (`04-networking`)
Сетевая инфраструктура.
- `vpc-subnets.md` — изоляция, CIDR, публичные и приватные подсети.
- `security-groups.md` — Stateful/Stateless фаерволы.
- `vpc-peering.md` — соединение сетей и Transit Gateway.
- `dns.md` — Route 53, Cloud DNS, маршрутизация.
- `cdn.md` — CloudFront, кеширование и защита от DDoS.

### 5. Security (`05-security`)
Безопасность облака.
- `iam.md` — управление доступом, роли и политики.
- `least-privilege.md` — принцип минимальных привилегий.
- `secrets.md` — Secrets Manager, Parameter Store.
- `compliance.md` — GDPR, HIPAA, PCI-DSS.
- `zero-trust.md` — архитектура Zero Trust.

### 6. Storage (`06-storage`)
Хранение данных.
- `object-storage.md` — S3, жизненный цикл, durability.
- `block-storage.md` — EBS, SSD vs HDD, IOPS.
- `file-storage.md` — EFS, shared filesystems.
- `lifecycle-glacier.md` — холодное хранение и архив.

### 7. Databases (`07-databases`)
Базы данных.
- `databases.md` — SQL vs NoSQL, DynamoDB, RDS, Aurora, Backups.

### 8. Containers & K8s (`08-containers-k8s`)
Оркестрация контейнеров.
- `containers-k8s.md` — Docker, ECS, EKS, GKE, Pods, Services.

### 9. CI/CD (`09-cicd`)
Развертывание и доставка.
- `cicd.md` — Pipelines, GitHub Actions, ArgoCD, Blue/Green.

### 10. IaC (`10-iac`)
Инфраструктура как код.
- `iac.md` — Terraform, CloudFormation, State Management, Modules.

### 11. Observability (`11-observability`)
Наблюдаемость.
- `observability.md` — CloudWatch, Prometheus, Grafana, Tracing, Alerts.

### 12. Reliability (`12-reliability`)
Надежность.
- `reliability.md` — SLA/SLO/SLI, Error Budgets, Chaos Engineering.

### 13. Cost (`13-cost`)
Оптимизация затрат.
- `cost.md` — Strategies, Budgets, Reserved, Spot, Tagging.

### 14. Architecture (`14-architecture`)
Архитектура.
- `architecture.md` — Well-Architected Framework, Patterns, Anti-Patterns.

### 15. Scenarios (`15-scenarios`)
Реальные кейсы.
- `scenarios.md` — Решения для высокой латентности, перерасхода и ботов.

### 16. Interview (`16-interview`)
Собеседования.
- `interview.md` — Вопросы и ответы для Junior, Middle, Senior, Staff.

### 17. Skill Matrix (`17-skill-matrix`)
Матрица компетенций.
- `skill-matrix.md` — Требования к уровням инженеров.

### 18. Checklist (`18-checklist`)
Чек-листы.
- `checklist.md` — Pre-flight проверки перед деплоем.

### 19. Roadmap (`19-roadmap`)
Путь развития.
- `roadmap.md` — План роста от Junior до Staff.

---

## Быстрый старт

1. **Клонируй репозиторий:**
   ```bash
   git clone https://github.com/ssrjkk/claude-skills.git
   ```
2. **Начни с основ:** Открой папку `01-core-fundamentals`.
3. **Выбери провайдера:** Изучи `02-cloud-providers`.
4. **Проверь себя:** Пройди чеклист в `18-checklist`.

---

## Стек технологий

![AWS](https://img.shields.io/badge/AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)
![GCP](https://img.shields.io/badge/GCP-4285F4?style=for-the-badge&logo=googlecloud&logoColor=white)
![Azure](https://img.shields.io/badge/Azure-0089D6?style=for-the-badge&logo=microsoftazure&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=for-the-badge&logo=terraform&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)

---

## Как внести вклад

1. Fork репозитория.
2. Создай ветку (`git checkout -b feature/amazing-skill`).
3. Commit изменения (`git commit -m 'Add some amazing skill'`).
4. Push в ветку (`git push origin feature/amazing-skill`).
5. Открой Pull Request.

---

## Контакты

[![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/ssrjkk)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ssrjkk)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:ssrjkk@example.com)

---

> **Помни:** Хорошая архитектура — это не когда больше нечего добавить, а когда уже ничего нельзя убрать.
