# Claude Skills Library

> 66 specialized skills for Claude.ai — accelerate development, testing, and deployment.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Skills: 66](https://img.shields.io/badge/Skills-66-brightgreen)](.claude/skills/)
[![Domains: 12](https://img.shields.io/badge/Domains-12-purple)](#skills-catalog)
[![Last Update](https://img.shields.io/github/last-commit/ssrjkk/claude-skills)](../../commits)

---

## Why Choose Claude Skills?

| Benefit | Description |
|--------|-------------|
| **Save tokens** | No need to describe context every time — just load a skill |
| **Higher accuracy** | Specialized instructions for each task domain |
| **Reusability** | One skill — hundreds of projects |
| **Local & free** | No API keys needed, everything in your repo |
| **Validated** | All skills tested and verified |

---

## Skills Catalog (66 Skills)

### Backend (6 skills)
| Skill | Description | Models |
|-------|-------------|--------|
| `python-fastapi` | REST API with FastAPI + Pydantic | sonnet, opus |
| `nodejs-express` | Express + TypeScript boilerplate | haiku, sonnet |
| `go-gin` | High-performance Go API | sonnet, opus |
| `java-spring` | Spring Boot enterprise apps | opus |
| `django-rest` | Django REST Framework API | sonnet, opus |
| `laravel` | Laravel PHP web apps | sonnet, opus |

### Frontend (6 skills)
| Skill | Description | Models |
|-------|-------------|--------|
| `react-typescript` | Type-safe React components | sonnet, opus |
| `vue-composition` | Vue 3 Composition API | sonnet, opus |
| `nextjs-ssr` | SSR/SSG React framework | opus |
| `svelte-kit` | Lightweight Svelte framework | sonnet, opus |
| `angular-typescript` | Enterprise Angular apps | opus |
| `astro-ssg` | Static sites with Astro | sonnet, opus |

### Mobile (4 skills)
| Skill | Description | Models |
|-------|-------------|--------|
| `flutter-clean-arch` | Flutter with Clean Architecture | opus |
| `react-native-expo` | Cross-platform mobile | sonnet, opus |
| `ios-swiftui` | Native iOS SwiftUI | opus |
| `android-kotlin` | Native Android Kotlin | opus |

### DevOps (10 skills)
| Skill | Description | Models |
|-------|-------------|--------|
| `docker-optimization` | Multi-stage, caching, security | sonnet, opus |
| `k8s-helm-deploy` | Helm charts & K8s deploy | opus |
| `terraform-aws` | IaC for AWS | sonnet, opus |
| `ansible-automation` | Configuration management | sonnet, opus |
| `monitoring-prometheus` | Metrics & alerting | sonnet, opus |
| `logging-elk` | Centralized logging | opus |
| `gitops-argocd` | GitOps for K8s | opus |
| `jenkins-pipeline` | CI/CD automation | sonnet, opus |
| `argocd-rollback` | Quick rollback for K8s | opus |
| `security-scan` | Vulnerability scanning | sonnet, opus |

### Data (6 skills)
| Skill | Description | Models |
|-------|-------------|--------|
| `etl-pipeline` | ETL with Pandas + SQLAlchemy | sonnet, opus |
| `ml-model-training` | ML training pipelines | opus |
| `vector-db-rag` | RAG with vector databases | opus |
| `data-validation` | Data quality checks | sonnet, opus |
| `airflow-dags` | Orchestration with Airflow | sonnet, opus |
| `kafka-streams` | Real-time event processing | opus |

### AI (4 skills)
| Skill | Description | Models |
|-------|-------------|--------|
| `prompt-engineering` | LLM prompt optimization | opus |
| `llm-eval` | LLM evaluation metrics | opus |
| `embedding-chunking` | Text chunking & embeddings | sonnet, opus |
| `agent-design` | LLM agent architecture | opus |

### QA (10 skills)
| Skill | Description | Models |
|-------|-------------|--------|
| `api-testing` | REST/GraphQL pytest tests | haiku, sonnet |
| `database-migration` | PostgreSQL Alembic migrations | haiku, sonnet |
| `ci-cd-setup` | GitHub Actions CI/CD | haiku, sonnet |
| `test-reporting` | Allure reporting | sonnet, opus |
| `e2e-playwright` | E2E tests with Playwright | sonnet, opus |
| `contract-testing-pact` | API contract testing | sonnet, opus |
| `performance-k6` | Load testing with k6 | sonnet, opus |
| `security-owasp` | OWASP Top 10 testing | opus |
| `selenium-grid` | Distributed testing | sonnet, opus |
| `cypress-e2e` | Modern E2E testing | sonnet, opus |

### Product (4 skills)
| Skill | Description | Models |
|-------|-------------|--------|
| `user-story-mapping` | User story mapping | sonnet, opus |
| `prd-template` | Product Requirements Doc | sonnet, opus |
| `sprint-retro` | Sprint retrospective | sonnet, opus |
| `metrics-dora` | DORA metrics analysis | sonnet, opus |

### Security (4 skills)
| Skill | Description | Models |
|-------|-------------|--------|
| `secrets-management` | Vault & secrets handling | sonnet, opus |
| `sbom-generation` | SBOM for supply chain | sonnet, opus |
| `pentest-checklist` | Penetration testing | opus |
| `compliance-gdpr` | GDPR compliance audit | opus |

### Blockchain (3 skills)
| Skill | Description | Models |
|-------|-------------|--------|
| `solidity` | Smart contracts for Ethereum | opus |
| `web3js` | Web3.js Ethereum interaction | sonnet, opus |
| `smart-contracts` | Full smart contract development | opus |

### Gamedev (3 skills)
| Skill | Description | Models |
|-------|-------------|--------|
| `unity` | Unity game development with C# | opus |
| `unreal` | Unreal Engine AAA games | opus |
| `godot` | Open-source 2D/3D engine | sonnet, opus |

### IoT (3 skills)
| Skill | Description | Models |
|-------|-------------|--------|
| `esp32` | ESP32 WiFi/Bluetooth IoT | sonnet, opus |
| `arduino` | Arduino hardware projects | haiku, sonnet |
| `mqtt` | Lightweight IoT messaging | sonnet, opus |

### Design (3 skills)
| Skill | Description | Models |
|-------|-------------|--------|
| `figma-plugin` | Figma plugin development | sonnet, opus |
| `design-tokens` | Design system tokens | sonnet, opus |
| `accessibility` | WCAG accessibility standards | sonnet, opus |

> **Tip**: Use `Ctrl+K` in Claude to quickly search skills by tag.

---

## Quick Start

```bash
# 1. Clone
git clone https://github.com/ssrjkk/claude-skills.git
cd claude-skills

# 2. In Claude.ai: Settings → Skills → Add local folder
#    Point to: /path/to/claude-skills/.claude/skills/

# 3. In chat: "Use skill python-fastapi"
#    Done!
```

---

## Navigation

- [Search by tags](#skills-catalog): `#python`, `#docker`, `#testing`
- [Model Matrix](.claude/MODELS.md): which skill for which model
- [Contributing](.github/CONTRIBUTING.md): guide in 5 minutes

---

## For Contributors

```bash
# Validate skills
python scripts/validate-skills.py

# Add new skill
./scripts/new-skill.sh my-awesome-skill
# → creates .claude/skills/my-awesome-skill/SKILL.md
```

📖 More: [CONTRIBUTING.md](.github/CONTRIBUTING.md)

---

## Statistics

![Skills Count](https://img.shields.io/badge/dynamic/json?label=Skills&query=$.metadata.total_skills&url=https://raw.githubusercontent.com/ssrjkk/claude-skills/main/skills_catalog.json)
![Domains](https://img.shields.io/badge/Domains-12-purple)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](.github/CONTRIBUTING.md)

---

## Contributing

Pull Requests are welcome!  
Found a bug? Have an idea for a new skill? → [Open an Issue](../../issues)

> *"The best way to predict the future is to create it" — add your skill today!*

---

## License

[MIT License](LICENSE) — use in personal and commercial projects.  
Credit the author if you copy entirely — it would be nice 😊

---

<sub>Made with ❤️ for the Claude community • [ssrjkk/claude-skills](https://github.com/ssrjkk/claude-skills)</sub>
