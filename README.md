Here's the **clean, professional English README.md** with `->` arrows and no emojis/stickers:

```markdown
# Claude Skills Library

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Skills: 63+](https://img.shields.io/badge/Skills-63+-brightgreen)](.claude/skills/)
[![Domains: 11](https://img.shields.io/badge/Domains-11-purple)](#-skill-catalog)
[![Last Update](https://img.shields.io/github/last-commit/ssrjkk/claude-skills?label=Updated)](../../commits)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

> Pre-built skills for Claude.ai — accelerate development, testing, and deployment with specialized, reusable instructions.

---

## Why Use Claude Skills?

| Benefit | Description |
|---------|-------------|
| Save Tokens | Skip repetitive context setup — activate a skill and go |
| Higher Accuracy | Domain-specific prompts yield better, more consistent results |
| Reusable | One skill, infinite projects — scale your workflow |
| Local & Free | Zero API keys, zero SaaS — everything runs in your repo |
| Modular | Mix & match skills for complex multi-step tasks |

---

## Skill Catalog

> Pro Tip: Use Ctrl+K in Claude.ai to search skills by tag like #python, #docker, or #testing

### Backend
| Skill | Description | Best For |
|-------|-------------|----------|
| python-fastapi | REST API scaffolding with FastAPI + Pydantic v2 | Sonnet, Opus |
| nodejs-express | Express + TypeScript boilerplate with best practices | Haiku, Sonnet |
| go-gin | High-performance Go APIs with Gin framework | Sonnet, Opus |
| java-spring | Spring Boot enterprise application patterns | Opus |
| django-rest | Django REST Framework API design & auth | Sonnet, Opus |
| laravel | Laravel PHP web app architecture & Eloquent | Sonnet, Opus |

### Frontend
| Skill | Description | Best For |
|-------|-------------|----------|
| react-typescript | Type-safe React components with hooks & context | Sonnet, Opus |
| vue-composition | Vue 3 Composition API patterns & reactivity | Sonnet, Opus |
| nextjs-ssr | Next.js SSR/SSG, App Router, and server actions | Opus |
| svelte-kit | SvelteKit routing, endpoints, and adapters | Sonnet, Opus |
| angular-typescript | Enterprise Angular architecture & DI | Opus |
| astro-ssg | Astro static site generation & islands architecture | Sonnet, Opus |

### Mobile
| Skill | Description | Best For |
|-------|-------------|----------|
| flutter-clean-arch | Flutter with Clean Architecture & BLoC | Opus |
| react-native-expo | Cross-platform mobile with Expo & TypeScript | Sonnet, Opus |
| ios-swiftui | Native iOS development with SwiftUI & Combine | Opus |
| android-kotlin | Modern Android with Kotlin, Coroutines, Jetpack | Opus |

### DevOps & Cloud
| Skill | Description | Best For |
|-------|-------------|----------|
| docker-optimization | Multi-stage builds, caching, security hardening | Sonnet, Opus |
| k8s-helm-deploy | Helm chart creation & Kubernetes deployment | Opus |
| terraform-aws | Infrastructure as Code for AWS resources | Sonnet, Opus |
| ansible-automation | Idempotent configuration management | Sonnet, Opus |
| monitoring-prometheus | Metrics collection, alerting, Grafana dashboards | Sonnet, Opus |
| logging-elk | Centralized logging with Elasticsearch, Logstash, Kibana | Opus |
| gitops-argocd | GitOps workflows with ArgoCD for K8s | Opus |
| jenkins-pipeline | Declarative Jenkins pipelines & shared libraries | Sonnet, Opus |
| argocd-rollback | Safe, instant rollbacks for Kubernetes apps | Opus |
| security-scan | SCA, SAST, and container vulnerability scanning | Sonnet, Opus |

### Data & AI
| Skill | Description | Best For |
|-------|-------------|----------|
| etl-pipeline | ETL workflows with Pandas, SQLAlchemy, and validation | Sonnet, Opus |
| ml-model-training | End-to-end ML training, evaluation, and logging | Opus |
| vector-db-rag | RAG pipelines with Pinecone, Weaviate, or Qdrant | Opus |
| data-validation | Great Expectations-style data quality checks | Sonnet, Opus |
| airflow-dags | Apache Airflow DAG design & orchestration | Sonnet, Opus |
| kafka-streams | Real-time event processing with Kafka Streams | Opus |
| prompt-engineering | Advanced prompt patterns, few-shot, and chain-of-thought | Opus |
| llm-eval | LLM evaluation metrics: BLEU, ROUGE, faithfulness | Opus |
| embedding-chunking | Optimal text chunking & embedding strategies | Sonnet, Opus |
| agent-design | LLM agent architectures: ReAct, Plan-and-Execute, tools | Opus |

### QA & Testing
| Skill | Description | Best For |
|-------|-------------|----------|
| api-testing | REST/GraphQL test suites with pytest & httpx | Haiku, Sonnet |
| database-migration | Alembic migrations for PostgreSQL with best practices | Haiku, Sonnet |
| ci-cd-setup | GitHub Actions workflows for CI/CD pipelines | Haiku, Sonnet |
| test-reporting | Allure reports with screenshots, steps, and history | Sonnet, Opus |
| e2e-playwright | Reliable E2E tests with Playwright & TypeScript | Sonnet, Opus |
| contract-testing-pact | Consumer-driven contract testing with Pact | Sonnet, Opus |
| performance-k6 | Load & stress testing with k6 and thresholds | Sonnet, Opus |
| security-owasp | OWASP Top 10 vulnerability testing checklist | Opus |
| selenium-grid | Distributed Selenium testing across browsers | Sonnet, Opus |
| cypress-e2e | Modern Cypress E2E with component testing | Sonnet, Opus |

### Product & Process
| Skill | Description | Best For |
|-------|-------------|----------|
| user-story-mapping | Collaborative user story mapping techniques | Sonnet, Opus |
| prd-template | Product Requirements Document template & guidelines | Sonnet, Opus |
| sprint-retro | Structured sprint retrospective facilitation | Sonnet, Opus |
| metrics-dora | DORA metrics analysis & improvement strategies | Sonnet, Opus |

### Security
| Skill | Description | Best For |
|-------|-------------|----------|
| secrets-management | HashiCorp Vault integration & secret rotation | Sonnet, Opus |
| sbom-generation | Software Bill of Materials for supply chain security | Sonnet, Opus |
| pentest-checklist | Structured penetration testing methodology | Opus |
| compliance-gdpr | GDPR compliance audit checklist & documentation | Opus |

### Blockchain
| Skill | Description | Best For |
|-------|-------------|----------|
| solidity | Secure smart contract development for Ethereum | Opus |
| web3js | Web3.js integration patterns & wallet interactions | Sonnet, Opus |
| smart-contracts | Full-cycle dApp development & testing | Opus |

### Gamedev
| Skill | Description | Best For |
|-------|-------------|----------|
| unity | Unity game architecture with C# & ECS patterns | Opus |
| unreal | Unreal Engine 5 AAA game development workflows | Opus |
| godot | Godot 4 GDScript & 2D/3D project setup | Sonnet, Opus |

### IoT
| Skill | Description | Best For |
|-------|-------------|----------|
| esp32 | ESP32 WiFi/Bluetooth projects with Arduino/ESP-IDF | Sonnet, Opus |
| arduino | Arduino hardware prototyping & sensor integration | Haiku, Sonnet |
| mqtt | Lightweight MQTT messaging for IoT edge devices | Sonnet, Opus |

### Design
| Skill | Description | Best For |
|-------|-------------|----------|
| figma-plugin | Figma plugin development with TypeScript | Sonnet, Opus |
| design-tokens | Design system tokens & cross-platform sync | Sonnet, Opus |
| accessibility | WCAG 2.2 compliance & inclusive design patterns | Sonnet, Opus |

---

## Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/ssrjkk/claude-skills.git
cd claude-skills

# 2. In Claude.ai:
#    Settings -> Skills -> Add local folder
#    Point to: /path/to/claude-skills/.claude/skills/

# 3. In chat, activate any skill:
#    "Use skill python-fastapi to scaffold a new API"
#    Done!
```

> Skills auto-update when you git pull — stay current with best practices.

---

## Navigation Tips

- Search by tag: #python, #docker, #testing, #security
- Model compatibility: Each skill lists recommended Claude models (haiku/sonnet/opus)
- Skill anatomy: Every skill includes SKILL.md with context, instructions, and examples
- Catalog JSON: Machine-readable index at skills_catalog.json for tooling integration

---

## For Contributors

```bash
# Validate all skills (linting + structure checks)
python scripts/validate-skills.py

# Scaffold a new skill (interactive)
./scripts/new-skill.sh my-new-skill
# -> Creates: .claude/skills/my-new-skill/SKILL.md with template

# Run local tests (if applicable)
python -m pytest tests/ -v
```

Full contribution guide: [CONTRIBUTING.md](CONTRIBUTING.md)

### Contribution Checklist
- [ ] Skill follows the SKILL.md template
- [ ] Includes clear #tags for discoverability
- [ ] Specifies compatible Claude models
- [ ] Adds entry to skills_catalog.json (or run scripts/update-catalog.py)
- [ ] Passes scripts/validate-skills.py

---

## Project Stats

| Metric | Value |
|--------|-------|
| Total Skills | 63+ |
| Domains Covered | 11 (Backend, Frontend, Mobile, DevOps, Data, AI, QA, Product, Security, Blockchain, Gamedev, IoT, Design) |
| Contributors | 1 (you could be next!) |
| Last Updated | [See commits](../../commits) |
| Catalog Format | JSON + Markdown (human & machine readable) |

---

## Contributing

Pull Requests are welcome!

- Found a bug? -> [Open an Issue](../../issues)
- Have a skill idea? -> [Start a Discussion](../../discussions)
- Ready to contribute? -> Fork, code, test, PR!

> "The best way to predict the future is to create it."  
> Add your skill today and help thousands of developers work smarter with Claude.

---

## License

Distributed under the MIT License. See LICENSE for details.

- Free for personal & commercial use  
- Modify, distribute, and extend  
- Please credit ssrjkk/claude-skills if you reuse substantial portions

---

<div align="center">

**Made for the Claude community**  
[github.com/ssrjkk/claude-skills](https://github.com/ssrjkk/claude-skills)

[Star this repo](../../stargazers) • [Fork it](../../fork) • [Share it](https://twitter.com/intent/tweet?text=Check%20out%20Claude%20Skills%20Library%20%E2%80%94%2063%2B%20pre-built%20skills%20to%20supercharge%20your%20Claude.ai%20workflow%3A&url=https%3A%2F%2Fgithub.com%2Fssrjkk%2Fclaude-skills)

</div>
```

---

### Changes applied:
- Replaced all `→` with `->`
- Removed all emojis and decorative stickers
- Kept clean markdown structure, tables, and badges
- Maintained professional tone and full functionality

### To deploy:
```bash
git add README.md
git commit -m "docs: clean README - arrows to ->, no emojis"
git push
```
