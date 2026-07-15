from __future__ import annotations

import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Optional
import argparse

from claude_skills.validator import SkillValidator


DOMAIN_TEMPLATES: dict[str, str] = {
    "ai": """## 🚀 Quick Start
Configure your AI/ML environment and select the right model for your task.

## 📋 When to Use
- Building or fine-tuning machine learning models
- Implementing NLP, computer vision, or predictive analytics
- Integrating AI capabilities into existing applications

## 🔧 Step-by-Step
1. Set up the environment with required dependencies
2. Prepare and validate your dataset
3. Choose the appropriate model architecture
4. Train the model with monitoring
5. Evaluate performance metrics
6. Deploy the trained model

## 📦 Dependencies
- Python 3.9+
- PyTorch or TensorFlow
- scikit-learn, pandas, numpy
- Weights & Biases or MLflow for tracking

## 🧪 Examples
```python
# Example: model training pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X_train, X_eval, y_train, y_eval = train_test_split(X, y, test_size=0.2, random_state=42)
model.fit(X_train, y_train)
predictions = model.predict(X_eval)
print(f"Accuracy: {accuracy_score(y_eval, predictions):.3f}")
```

## ✅ Validation
- Run the complete pipeline end-to-end
- Verify metrics meet baseline thresholds
- Test with sample inference inputs
""",
    "backend": """## 🚀 Quick Start
Set up your backend service with the chosen framework and establish the project structure.

## 📋 When to Use
- Building RESTful or GraphQL APIs
- Implementing microservices architecture
- Creating server-side business logic

## 🔧 Step-by-Step
1. Initialize the project with dependency management
2. Configure the application (env vars, settings)
3. Define data models and database schema
4. Implement API endpoints with validation
5. Add authentication and authorization
6. Write integration tests
7. Set up logging and monitoring

## 📦 Dependencies
- FastAPI / Django / Express.js / Spring Boot
- Database driver (SQLAlchemy, Prisma, etc.)
- Pydantic / Zod for validation
- Redis for caching (optional)

## 🧪 Examples
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.post("/items")
async def create_item(item: Item):
    return {"id": 1, **item.model_dump()}
```

## ✅ Validation
- All endpoints return correct status codes
- Input validation rejects invalid data
- Auth middleware blocks unauthorized requests
- Test suite passes with >80% coverage
""",
    "frontend": """## 🚀 Quick Start
Initialize your frontend project and set up the development environment.

## 📋 When to Use
- Building responsive web interfaces
- Creating component libraries
- Implementing client-side state management

## 🔧 Step-by-Step
1. Scaffold the project with Vite / Next.js
2. Set up the UI component architecture
3. Implement routing and navigation
4. Add state management (React Query, Zustand, etc.)
5. Style components (Tailwind, CSS Modules, etc.)
6. Add client-side validation
7. Optimize bundle size and performance

## 📦 Dependencies
- React 18+ / Vue 3+ / Svelte
- TypeScript
- Tailwind CSS / styled-components
- React Router / Vue Router

## 🧪 Examples
```tsx
import { useState } from 'react';

export function Counter() {
  const [count, setCount] = useState(0);
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(c => c + 1)}>
        Increment
      </button>
    </div>
  );
}
```

## ✅ Validation
- Components render without errors
- Responsive design works on all breakpoints
- Lighthouse score > 90
- Accessibility audit passes
""",
    "devops": """## 🚀 Quick Start
Set up CI/CD pipeline and infrastructure automation.

## 📋 When to Use
- Automating build, test, and deployment processes
- Managing cloud infrastructure as code
- Containerizing and orchestrating applications

## 🔧 Step-by-Step
1. Define infrastructure with Terraform/Pulumi
2. Containerize the application with Docker
3. Configure CI/CD pipeline (GitHub Actions, GitLab CI)
4. Set up Kubernetes manifests
5. Implement monitoring and alerting
6. Configure backup and disaster recovery
7. Document runbooks

## 📦 Dependencies
- Docker & Docker Compose
- Kubernetes (kubectl, Helm)
- Terraform or Pulumi
- GitHub Actions / GitLab CI

## 🧪 Examples
```yaml
name: Deploy
on:
  push:
    branches: [main]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Build and push
        run: |
          docker build -t app:${{ github.sha }} .
          docker push app:${{ github.sha }}
```

## ✅ Validation
- Pipeline runs successfully end-to-end
- Infrastructure deploys without drift
- Rollback procedure tested
- Alert rules trigger correctly
""",
    "security": """## 🚀 Quick Start
Set up security scanning and implement secure coding practices.

## 📋 When to Use
- Performing security audits and penetration testing
- Implementing authentication and authorization
- Securing APIs and data in transit/at rest
- Complying with security standards (OWASP, ISO 27001)

## 🔧 Step-by-Step
1. Run dependency vulnerability scan
2. Configure SAST/DAST tools
3. Implement authentication (OAuth 2.0, JWT)
4. Set up RBAC with least privilege
5. Encrypt sensitive data at rest and in transit
6. Add rate limiting and input sanitization
7. Configure security headers and CORS
8. Set up security monitoring and alerting

## 📦 Dependencies
- OWASP Dependency-Check / Snyk
- Auth library (Auth0, Clerk, etc.)
- bcrypt / argon2 for password hashing
- SSL/TLS certificates

## 🧪 Examples
```python
from passlib.hash import bcrypt

hashed = bcrypt.hash("user_password")
is_valid = bcrypt.verify("user_password", hashed)
```

## ✅ Validation
- OWASP Top 10 vulnerabilities addressed
- Dependency scan shows zero critical CVEs
- Auth system passes integration tests
- Security headers present in responses
""",
    "database": """## 🚀 Quick Start
Set up and configure your database with optimal schema design.

## 📋 When to Use
- Designing database schemas for new applications
- Optimizing query performance
- Migrating between database systems
- Implementing data replication and backup

## 🔧 Step-by-Step
1. Choose the right database (relational vs NoSQL)
2. Design the schema with normalization
3. Create indexes for query performance
4. Set up connection pooling
5. Implement migrations
6. Configure backups and replication
7. Monitor query performance

## 📦 Dependencies
- PostgreSQL / MySQL / MongoDB
- Database driver (psycopg2, mysql-connector, pymongo)
- Migration tool (Alembic, Flyway, Prisma Migrate)
- Connection pooler (PgBouncer, etc.)

## 🧪 Examples
```sql
CREATE INDEX idx_orders_user_date ON orders(user_id, created_at DESC);

EXPLAIN ANALYZE
SELECT * FROM orders
WHERE user_id = 123
  AND created_at >= NOW() - INTERVAL '30 days'
ORDER BY created_at DESC;
```

## ✅ Validation
- Schema migrations run cleanly
- Query execution time < 100ms for common queries
- Backup and restore tested successfully
- Connection pool handles peak load
""",
    "qa": """## 🚀 Quick Start
Set up your testing framework and write comprehensive tests.

## 📋 When to Use
- Writing unit, integration, and E2E tests
- Implementing test automation in CI/CD
- Performing regression and smoke testing
- Measuring and improving code coverage

## 🔧 Step-by-Step
1. Choose testing framework (pytest, Jest, Vitest)
2. Set up test configuration and fixtures
3. Write unit tests for business logic
4. Add integration tests for API endpoints
5. Implement E2E tests for critical paths
6. Configure coverage thresholds
7. Add performance/load tests

## 📦 Dependencies
- pytest / Jest / Vitest
- pytest-cov / c8 for coverage
- Playwright / Cypress for E2E
- locust / k6 for load testing

## 🧪 Examples
```python
import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_create_item():
    response = client.post("/items", json={"name": "test", "price": 10.0})
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "test"
    assert data["price"] == 10.0
```

## ✅ Validation
- Unit tests pass (coverage > 80%)
- Integration tests cover all API endpoints
- E2E tests cover critical user journeys
- Load tests show acceptable response times
""",
}

GENERIC_TEMPLATE = """## 🚀 Quick Start
Get started quickly with the essential setup and configuration.

## 📋 When to Use
- When you need domain-specific expertise
- Implementing best practices in this field
- Solving common problems efficiently

## 🔧 Step-by-Step
1. Review the prerequisites and requirements
2. Set up the development environment
3. Implement the core functionality
4. Test and validate the implementation
5. Document and share the results

## 📦 Dependencies
- Standard tooling for the domain
- Relevant SDKs and libraries
- Development and testing frameworks

## 🧪 Examples
```python
def main():
    config = load_config()
    result = process(config)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
```

## ✅ Validation
- All steps completed successfully
- Expected outputs match requirements
- Edge cases are handled
- Performance meets benchmarks
"""

DOMAIN_KEYWORDS: dict[str, list[str]] = {
    "ai": ["machine learning", "deep learning", "neural", "llm", "gpt", "claude", "ai", "intelligence", "nlp", "computer vision", "tensorflow", "pytorch", "model"],
    "backend": ["backend", "api", "rest", "graphql", "server", "microservice", "fastapi", "django", "flask", "express"],
    "frontend": ["frontend", "react", "vue", "svelte", "ui", "component", "tailwind", "css", "html", "javascript", "typescript"],
    "devops": ["devops", "ci/cd", "deploy", "docker", "kubernetes", "k8s", "terraform", "ansible", "jenkins", "github actions"],
    "security": ["security", "auth", "oauth", "jwt", "encrypt", "vulnerability", "owasp", " penetration", "cve"],
    "database": ["database", "sql", "nosql", "postgresql", "mysql", "mongodb", "redis", "query", "schema", "migration"],
    "qa": ["test", "qa", "quality", "pytest", "jest", "assert", "coverage", "regression", "e2e"],
    "mobile": ["mobile", "android", "ios", "swift", "kotlin", "react native", "flutter"],
    "cloud": ["cloud", "aws", "azure", "gcp", "lambda", "s3", "ec2", "serverless"],
    "data": ["data", "analytics", "pipeline", "etl", "spark", "hadoop", "dataframe", "pandas"],
    "blockchain": ["blockchain", "ethereum", "solidity", "web3", "crypto", "nft", "smart contract"],
    "gamedev": ["game", "unity", "unreal", "godot", "3d", "2d", "sprite", "physics"],
}


def _detect_domain(prompt: str) -> str:
    prompt_lower = prompt.lower()
    max_score = 0
    best_domain = "general"
    for domain, keywords in DOMAIN_KEYWORDS.items():
        score = sum(2 if kw in prompt_lower else 0 for kw in keywords)
        if score > max_score:
            max_score = score
            best_domain = domain
    return best_domain


def _generate_skill_content(domain: str, skill_name: str, description: str) -> str:
    template = DOMAIN_TEMPLATES.get(domain, GENERIC_TEMPLATE)
    display_name = skill_name.replace("-", " ").title()
    now = time.strftime("%Y-%m-%d")
    return (
        f"---\n"
        f"name: {skill_name}\n"
        f"description: {description}\n"
        f"category: {domain}\n"
        f"tags: [{skill_name}, {domain}]\n"
        f"models: [sonnet, opus]\n"
        f"version: 1.0.0\n"
        f"language: en\n"
        f"created: {now}\n"
        f"---\n"
        f"# {display_name}\n\n"
        f"> {description}\n\n"
        f"{template}"
    )


def _generate_ru_content(skill_name: str, description: str, domain: str) -> str:
    display_name = skill_name.replace("-", " ").title()
    now = time.strftime("%Y-%m-%d")
    domain_ru_map = {
        "ai": "ИИ", "backend": "Бэкенд", "frontend": "Фронтенд", "devops": "DevOps",
        "security": "Безопасность", "database": "Базы данных", "qa": "Тестирование",
        "mobile": "Мобильная разработка", "data": "Data Science", "cloud": "Облачные технологии",
        "blockchain": "Блокчейн", "design": "Дизайн", "gamedev": "Геймдев", "iot": "IoT",
    }
    domain_ru = domain_ru_map.get(domain, domain.replace("-", " ").title())
    return (
        f"---\n"
        f"name: {skill_name}\n"
        f"description: {description}\n"
        f"category: {domain}\n"
        f"tags: [{skill_name}, {domain}, russian]\n"
        f"models: [sonnet, opus]\n"
        f"version: 1.0.0\n"
        f"language: ru\n"
        f"original: {skill_name}\n"
        f"created: {now}\n"
        f"---\n"
        f"# {display_name}\n\n"
        f"> {description}\n\n"
        f"## Быстрый старт\n"
        f"Настройте окружение и приступите к работе.\n\n"
        f"## Когда использовать\n"
        f"- Работа с {domain_ru}\n"
        f"- Выполнение задач, связанных с {display_name}\n\n"
        f"## Инструкции\n"
        f"1. Ознакомьтесь с предварительными требованиями\n"
        f"2. Настройте среду разработки\n"
        f"3. Реализуйте основную функциональность\n"
        f"4. Проверьте и протестируйте результат\n\n"
        f"## Ресурсы\n"
        f"- Официальная документация\n"
        f"- Сообщество разработчиков\n\n"
        f"## Валидация\n"
        f"- Все шаги выполнены успешно\n"
        f"- Результат соответствует требованиям\n"
    )


def _llm_generate(prompt: str) -> Optional[str]:
    api_key = os.environ.get("ANTHROPIC_API_KEY") or os.environ.get("CLAUDE_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY environment variable required for LLM generation", file=sys.stderr)
        return None

    system_prompt = (
        "You are a skill generator for Claude Code. Generate a complete SKILL.md file "
        "with YAML frontmatter (name, description, category, tags, models, version, language, created) "
        "and markdown body with sections: Quick Start, When to Use, Step-by-Step, Dependencies, "
        "Examples (with code), Validation. Use the .md format exactly."
    )

    body = {
        "model": "claude-sonnet-4-20250514",
        "max_tokens": 4096,
        "system": system_prompt,
        "messages": [{"role": "user", "content": f"Generate a Claude Code skill for: {prompt}"}],
    }

    try:
        req = urllib.request.Request(
            "https://api.anthropic.com/v1/messages",
            data=json.dumps(body).encode(),
            headers={
                "Content-Type": "application/json",
                "x-api-key": api_key,
                "anthropic-version": "2023-06-01",
                "User-Agent": "claude-skills-cli",
            },
        )
        with urllib.request.urlopen(req, timeout=60) as resp:
            result = json.loads(resp.read().decode())
            return result.get("content", [{}])[0].get("text", "")
    except (urllib.error.HTTPError, urllib.error.URLError, OSError, json.JSONDecodeError) as e:
        print(f"Error calling Claude API: {e}", file=sys.stderr)
        return None


def cmd_generate(args: argparse.Namespace) -> int:
    prompt = args.prompt
    output_dir = Path(args.dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    if args.api:
        content = _llm_generate(prompt)
        if not content:
            return 1
    else:
        domain = args.domain or _detect_domain(prompt)
        skill_name = args.name or prompt.lower().strip().replace(" ", "-")[:60].strip("-")
        skill_name = re.sub(r"[^a-z0-9-]", "", skill_name)
        if not skill_name:
            skill_name = "custom-skill"
        description = prompt.strip()
        if len(description) > 120:
            description = description[:117] + "..."

        content = _generate_skill_content(domain, skill_name, description)
        ru_content = _generate_ru_content(skill_name, description, domain)

        target = output_dir / domain / skill_name
        target.mkdir(parents=True, exist_ok=True)
        (target / "SKILL.md").write_text(content, encoding="utf-8")
        (target / "SKILL.ru.md").write_text(ru_content, encoding="utf-8")

        validator = SkillValidator()
        results = validator.validate_skill_file(target / "SKILL.md")
        errors = [r for r in results if r.severity.name == "ERROR"]
        warnings = [r for r in results if r.severity.name == "WARNING"]

        print(f"Generated skill: {domain}/{skill_name}")
        print(f"  EN: {target / 'SKILL.md'}")
        print(f"  RU: {target / 'SKILL.ru.md'}")
        if errors:
            print(f"  Validation errors: {len(errors)}")
            for e in errors:
                print(f"    {e}")
        if warnings:
            print(f"  Validation warnings: {len(warnings)}")
            for w in warnings:
                print(f"    {w}")
        if not errors:
            print("  Validation: PASSED")
        return 0

    if content:
        print(content)
        print("\n--- Content generated. Save to .claude/skills/<category>/<name>/SKILL.md ---")
    return 0
