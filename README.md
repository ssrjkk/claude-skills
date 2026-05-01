# Claude Skills Library

> Готовые скиллы для Claude.ai — ускоряй разработку, тестирование и деплой

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Skills: 63+](https://img.shields.io/badge/Skills-63+-brightgreen)](.claude/skills/)
[![Domains: 11](https://img.shields.io/badge/Domains-11-purple)](#каталог-скиллов)
[![Last Update](https://img.shields.io/github/last-commit/ssrjkk/claude-skills)](../../commits)

---

##  Зачем это нужно

-  **Экономь токены**: не описывай контекст каждый раз — подключи скилл
-  **Точнее результаты**: специализированные инструкции для каждой задачи
-  **Переиспользование**: один скилл — сотни проектов
-  **Локально и бесплатно**: никаких API-ключей, всё в твоем репо

---

##  Каталог скиллов

| Домен | Скилл | Описание | Модели |
|-------|-------|----------|--------|
|  Backend | `python-fastapi` | REST API на FastAPI + Pydantic | sonnet, opus |
|  Backend | `nodejs-express` | Express + TypeScript boilerplate | haiku, sonnet |
|  Backend | `go-gin` | High-performance Go API | sonnet, opus |
|  Backend | `java-spring` | Spring Boot enterprise apps | opus |
|  Backend | `django-rest` | Django REST Framework API | sonnet, opus |
|  Backend | `laravel` | Laravel PHP web apps | sonnet, opus |
|  Frontend | `react-typescript` | Type-safe React components | sonnet, opus |
|  Frontend | `vue-composition` | Vue 3 Composition API | sonnet, opus |
|  Frontend | `nextjs-ssr` | SSR/SSG React framework | opus |
|  Frontend | `svelte-kit` | Lightweight Svelte framework | sonnet, opus |
|  Frontend | `angular-typescript` | Enterprise Angular apps | opus |
|  Frontend | `astro-ssg` | Static sites with Astro | sonnet, opus |
|  Mobile | `flutter-clean-arch` | Flutter с Clean Architecture | opus |
|  Mobile | `react-native-expo` | Cross-platform mobile | sonnet, opus |
|  Mobile | `ios-swiftui` | Native iOS SwiftUI | opus |
|  Mobile | `android-kotlin` | Native Android Kotlin | opus |
|  DevOps | `docker-optimization` | Multi-stage, caching, security | sonnet, opus |
|  DevOps | `k8s-helm-deploy` | Helm charts & K8s deploy | opus |
|  DevOps | `terraform-aws` | IaC for AWS | sonnet, opus |
|  DevOps | `ansible-automation` | Configuration management | sonnet, opus |
|  DevOps | `monitoring-prometheus` | Metrics & alerting | sonnet, opus |
|  DevOps | `logging-elk` | Centralized logging | opus |
|  DevOps | `gitops-argocd` | GitOps for K8s | opus |
|  DevOps | `jenkins-pipeline` | CI/CD automation | sonnet, opus |
|  DevOps | `argocd-rollback` | Quick rollback for K8s | opus |
|  DevOps | `security-scan` | Vulnerability scanning | sonnet, opus |
|  Data | `etl-pipeline` | ETL с Pandas + SQLAlchemy | sonnet, opus |
|  Data | `ml-model-training` | ML training pipelines | opus |
|  Data | `vector-db-rag` | RAG с vector databases | opus |
|  Data | `data-validation` | Data quality checks | sonnet, opus |
|  Data | `airflow-dags` | Orchestration with Airflow | sonnet, opus |
|  Data | `kafka-streams` | Real-time event processing | opus |
|  AI | `prompt-engineering` | LLM prompt optimization | opus |
|  AI | `llm-eval` | LLM evaluation metrics | opus |
|  AI | `embedding-chunking` | Text chunking & embeddings | sonnet, opus |
|  AI | `agent-design` | LLM agent architecture | opus |
|  QA | `api-testing` | REST/GraphQL pytest tests | haiku, sonnet |
|  QA | `database-migration` | PostgreSQL Alembic migrations | haiku, sonnet |
|  QA | `ci-cd-setup` | GitHub Actions CI/CD | haiku, sonnet |
|  QA | `test-reporting` | Allure reporting | sonnet, opus |
|  QA | `e2e-playwright` | E2E tests with Playwright | sonnet, opus |
|  QA | `contract-testing-pact` | API contract testing | sonnet, opus |
|  QA | `performance-k6` | Load testing with k6 | sonnet, opus |
|  QA | `security-owasp` | OWASP Top 10 testing | opus |
|  QA | `selenium-grid` | Distributed testing | sonnet, opus |
|  QA | `cypress-e2e` | Modern E2E testing | sonnet, opus |
|  Product | `user-story-mapping` | User story mapping | sonnet, opus |
|  Product | `prd-template` | Product Requirements Doc | sonnet, opus |
|  Product | `sprint-retro` | Sprint retrospective | sonnet, opus |
|  Product | `metrics-dora` | DORA metrics analysis | sonnet, opus |
|  Security | `secrets-management` | Vault & secrets handling | sonnet, opus |
|  Security | `sbom-generation` | SBOM for supply chain | sonnet, opus |
|  Security | `pentest-checklist` | Penetration testing | opus |
|  Security | `compliance-gdpr` | GDPR compliance audit | opus |
|  Blockchain | `solidity` | Smart contracts for Ethereum | opus |
|  Blockchain | `web3js` | Web3.js Ethereum interaction | sonnet, opus |
|  Blockchain | `smart-contracts` | Full smart contract development | opus |
|  Gamedev | `unity` | Unity game development with C# | opus |
|  Gamedev | `unreal` | Unreal Engine AAA games | opus |
|  Gamedev | `godot` | Open-source 2D/3D engine | sonnet, opus |
|  IoT | `esp32` | ESP32 WiFi/Bluetooth IoT | sonnet, opus |
|  IoT | `arduino` | Arduino hardware projects | haiku, sonnet |
|  IoT | `mqtt` | Lightweight IoT messaging | sonnet, opus |
|  Design | `figma-plugin` | Figma plugin development | sonnet, opus |
|  Design | `design-tokens` | Design system tokens | sonnet, opus |
|  Design | `accessibility` | WCAG accessibility standards | sonnet, opus |

>  **Совет**: Используй `Ctrl+K` в Claude для быстрого поиска скилла по тегу

---

##  Быстрый старт

```bash
# 1. Клонировать
git clone https://github.com/ssrjkk/claude-skills.git
cd claude-skills

# 2. В Claude.ai: Settings → Skills → Add local folder
#    Укажите путь: /путь/к/клауд-скиллам/.claude/skills/

# 3. В чате напишите: "Используй скилл python-fastapi"
#    Готово!
```

---

##  Навигация

-  [Поиск по тегам](#каталог-скиллов): `#python`, `#docker`, `#testing`
-  [Матрица моделей](.claude/MODELS.md): какой скилл для какой модели
-  [Добавить свой скилл](.github/CONTRIBUTING.md): гайд за 5 минут

---

##  Для контрибьюторов

```bash
# Валидация скиллов
python scripts/validate-skills.py

# Добавить новый скилл
./scripts/new-skill.sh my-awesome-skill
# → создаст шаблон .claude/skills/my-awesome-skill/SKILL.md
```

📖 Подробнее: [CONTRIBUTING.md](.github/CONTRIBUTING.md)

---

##  Статистика

[![Skills Count](https://img.shields.io/badge/dynamic/json?label=Skills&query=$.metadata.total_skills&url=https://raw.githubusercontent.com/ssrjkk/claude-skills/main/skills_catalog.json)](skills_catalog.json)
[![Domains](https://img.shields.io/badge/Domains-11-purple)](#каталог-скиллов)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](.github/CONTRIBUTING.md)

---

##  Contributing

Pull Request'ы приветствуются!  
Нашли баг? Есть идея для нового скилла? → [Открыть Issue](../../issues)

>  "Лучший способ предсказать будущее — создать его" — добавь свой скилл сегодня!

---

##  License

[MIT License](LICENSE) — используй в личных и коммерческих проектах.  
Укажи автора, если копируешь целиком — будет приятно

---

<sub>Made with  for the Claude community • [ssrjkk/claude-skills](https://github.com/ssrjkk/claude-skills)</sub>
