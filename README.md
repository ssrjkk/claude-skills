# 🎯 Claude Skills Library

> 🤖 Готовые скиллы для Claude.ai — ускоряй разработку, тестирование и деплой

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Skills: 28+](https://img.shields.io/badge/Skills-28+-brightgreen)](.claude/skills/)
[![Domains: 7](https://img.shields.io/badge/Domains-7-purple)](#-каталог-скиллов)
[![Last Update](https://img.shields.io/github/last-commit/ssrjkk/claude-skills)](../../commits)

---

## ✨ Зачем это нужно

- ⚡ **Экономь токены**: не описывай контекст каждый раз — подключи скилл
- 🎯 **Точнее результаты**: специализированные инструкции для каждой задачи
- 🔁 **Переиспользование**: один скилл — сотни проектов
- 🌐 **Локально и бесплатно**: никаких API-ключей, всё в твоем репо

---

## 🗂️ Каталог скиллов

| Домен | Скилл | Описание | Модели |
|-------|-------|----------|--------|
| 🔹 Backend | `python-fastapi` | REST API на FastAPI + Pydantic | sonnet, opus |
| 🔹 Backend | `nodejs-express` | Express + TypeScript boilerplate | haiku, sonnet |
| 🔹 Backend | `go-gin` | High-performance Go API | sonnet, opus |
| 🔹 Backend | `java-spring` | Spring Boot enterprise apps | opus |
| 🔹 Frontend | `react-typescript` | Type-safe React components | sonnet, opus |
| 🔹 Frontend | `vue-composition` | Vue 3 Composition API | sonnet, opus |
| 🔹 Frontend | `nextjs-ssr` | SSR/SSG React framework | opus |
| 🔹 Frontend | `svelte-kit` | Lightweight Svelte framework | sonnet, opus |
| 🔹 Mobile | `flutter-clean-arch` | Flutter с Clean Architecture | opus |
| 🔹 Mobile | `react-native-expo` | Cross-platform mobile | sonnet, opus |
| 🔹 Mobile | `ios-swiftui` | Native iOS SwiftUI | opus |
| 🔹 Mobile | `android-kotlin` | Native Android Kotlin | opus |
| 🔹 DevOps | `docker-optimization` | Multi-stage, caching, security | sonnet, opus |
| 🔹 DevOps | `k8s-helm-deploy` | Helm charts & K8s deploy | opus |
| 🔹 DevOps | `terraform-aws` | IaC for AWS | sonnet, opus |
| 🔹 DevOps | `ansible-automation` | Configuration management | sonnet, opus |
| 🔹 DevOps | `monitoring-prometheus` | Metrics & alerting | sonnet, opus |
| 🔹 DevOps | `logging-elk` | Centralized logging | opus |
| 🔹 DevOps | `gitops-argocd` | GitOps for K8s | opus |
| 🔹 DevOps | `security-scan` | Vulnerability scanning | sonnet, opus |
| 🔹 Data | `etl-pipeline` | ETL с Pandas + SQLAlchemy | sonnet, opus |
| 🔹 Data | `ml-model-training` | ML training pipelines | opus |
| 🔹 Data | `vector-db-rag` | RAG с vector databases | opus |
| 🔹 Data | `data-validation` | Data quality checks | sonnet, opus |
| 🔹 AI | `prompt-engineering` | LLM prompt optimization | opus |
| 🔹 AI | `llm-eval` | LLM evaluation metrics | opus |
| 🔹 AI | `embedding-chunking` | Text chunking & embeddings | sonnet, opus |
| 🔹 AI | `agent-design` | LLM agent architecture | opus |
| 🔹 QA | `api-testing` | REST/GraphQL pytest tests | haiku, sonnet |
| 🔹 QA | `database-migration` | PostgreSQL Alembic migrations | haiku, sonnet |
| 🔹 QA | `ci-cd-setup` | GitHub Actions CI/CD | haiku, sonnet |
| 🔹 QA | `test-reporting` | Allure reporting | sonnet, opus |
| 🔹 QA | `e2e-playwright` | E2E tests with Playwright | sonnet, opus |
| 🔹 QA | `contract-testing-pact` | API contract testing | sonnet, opus |
| 🔹 QA | `performance-k6` | Load testing with k6 | sonnet, opus |
| 🔹 QA | `security-owasp` | OWASP Top 10 testing | opus |
| 🔹 Product | `user-story-mapping` | User story mapping | sonnet, opus |
| 🔹 Product | `prd-template` | Product Requirements Doc | sonnet, opus |
| 🔹 Product | `sprint-retro` | Sprint retrospective | sonnet, opus |
| 🔹 Product | `metrics-dora` | DORA metrics analysis | sonnet, opus |
| 🔹 Security | `secrets-management` | Vault & secrets handling | sonnet, opus |
| 🔹 Security | `sbom-generation` | SBOM for supply chain | sonnet, opus |
| 🔹 Security | `pentest-checklist` | Penetration testing | opus |
| 🔹 Security | `compliance-gdpr` | GDPR compliance audit | opus |

> 💡 **Совет**: Используй `Ctrl+K` в Claude для быстрого поиска скилла по тегу

---

## 🚀 Быстрый старт

```bash
# 1. Клонировать
git clone https://github.com/ssrjkk/claude-skills.git
cd claude-skills

# 2. В Claude.ai: Settings → Skills → Add local folder
#    Укажите путь: /путь/к/клауд-скиллам/.claude/skills/

# 3. В чате напишите: "Используй скилл python-fastapi"
#    Готово! 🎉
```

---

## 🧭 Навигация

- 🔍 [Поиск по тегам](#-каталог-скиллов): `#python`, `#docker`, `#testing`
- 📊 [Матрица моделей](.claude/MODELS.md): какой скилл для какой модели
- 🤝 [Добавить свой скилл](.github/CONTRIBUTING.md): гайд за 5 минут

---

## 🛠️ Для контрибьюторов

```bash
# Добавить новый скилл
./scripts/new-skill.sh my-awesome-skill
# → создаст шаблон .claude/skills/my-awesome-skill/SKILL.md
```

📖 Подробнее: [CONTRIBUTING.md](.github/CONTRIBUTING.md)

---

## 📈 Статистика

[![Skills Count](https://img.shields.io/badge/dynamic/json?label=Skills&query=$.metadata.total_skills&url=https://raw.githubusercontent.com/ssrjkk/claude-skills/main/skills_catalog.json)](skills_catalog.json)
[![Domains](https://img.shields.io/badge/Domains-7-purple)](#-каталог-скиллов)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](.github/CONTRIBUTING.md)

---

## 🤝 Contributing

Pull Request'ы приветствуются! 🙌  
Нашли баг? Есть идея для нового скилла? → [Открыть Issue](../../issues)

> 💬 "Лучший способ предсказать будущее — создать его" — добавь свой скилл сегодня!

---

## 📄 License

[MIT License](LICENSE) — используй в личных и коммерческих проектах.  
Укажи автора, если копируешь целиком — будет приятно 😊

---

<sub>✨ Made with ❤️ for the Claude community • [ssrjkk/claude-skills](https://github.com/ssrjkk/claude-skills)</sub>
