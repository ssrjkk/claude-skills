#!/usr/bin/env python3
"""Generate high-quality skill content using templates.

This module provides structured templates for generating real,
production-quality skill content across all 39 domains.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path


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

# Train/eval split
X_train, X_eval, y_train, y_eval = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model.fit(X_train, y_train)

# Evaluate
predictions = model.predict(X_eval)
print(f"Accuracy: {accuracy_score(y_eval, predictions):.3f}")
```

## 🔗 Resources
- Official documentation for your ML framework
- Community best practices and tutorials
- Relevant research papers

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
    # Validate and persist
    return {"id": 1, **item.model_dump()}
```

## 🔗 Resources
- Framework documentation
- API design best practices (REST, GraphQL)
- Database optimization guides

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

## 🔗 Resources
- Framework documentation
- Component library (shadcn/ui, Radix, etc.)
- Accessibility guidelines (WCAG)

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
# .github/workflows/deploy.yml
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

## 🔗 Resources
- CNCF landscape and tools
- Cloud provider documentation
- SRE best practices

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
from itsdangerous import URLSafeTimedSerializer

# Hash a password
hashed = bcrypt.hash("user_password")

# Verify a password
is_valid = bcrypt.verify("user_password", hashed)

# Generate secure token
serializer = URLSafeTimedSerializer("secret-key")
token = serializer.dumps({"user_id": 123})
```

## 🔗 Resources
- OWASP Top 10 Web Security Risks
- NIST security guidelines
- CVE database and security advisories

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
-- Optimized query with index
CREATE INDEX idx_orders_user_date ON orders(user_id, created_at DESC);

EXPLAIN ANALYZE
SELECT * FROM orders
WHERE user_id = 123
  AND created_at >= NOW() - INTERVAL '30 days'
ORDER BY created_at DESC;
```

## 🔗 Resources
- Database documentation
- Query optimization guides
- Backup and recovery procedures

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
6. Configure test coverage thresholds
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

## 🔗 Resources
- Testing framework documentation
- Testing best practices
- Coverage reporting tools

## ✅ Validation
- Unit tests pass (coverage > 80%)
- Integration tests cover all API endpoints
- E2E tests cover critical user journeys
- Load tests show acceptable response times
""",
}

OTHER_TEMPLATES = """## 🚀 Quick Start
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
# Example implementation
def main():
    # Initialize
    config = load_config()
    result = process(config)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
```

## 🔗 Resources
- Official documentation
- Community forums and discussions
- Related skills in the library

## ✅ Validation
- All steps completed successfully
- Expected outputs match requirements
- Edge cases are handled
- Performance meets benchmarks
"""


def generate_skill_content(domain: str, skill_name: str, description: str) -> str:
    template = DOMAIN_TEMPLATES.get(domain, OTHER_TEMPLATES)
    display_name = skill_name.replace("-", " ").title()
    return (
        f"---\n"
        f"name: {skill_name}\n"
        f"description: {description}\n"
        f"category: {domain}\n"
        f"tags: [{skill_name}, {domain}, basics]\n"
        f"models: [sonnet, opus]\n"
        f"version: 1.0.0\n"
        f"language: en\n"
        f"created: 2026-06-19\n"
        f"---\n"
        f"# {display_name}\n\n"
        f"> {description}\n\n"
        f"{template}"
    )


def generate_ru_content(en_skill_name: str, en_description: str, domain: str) -> str:
    domain_ru = {
        "ai": "ИИ", "backend": "Бэкенд", "frontend": "Фронтенд", "devops": "DevOps",
        "security": "Безопасность", "database": "Базы данных", "qa": "Тестирование",
        "mobile": "Мобильная разработка", "data": "Data Science", "cloud": "Облачные технологии",
        "blockchain": "Блокчейн", "design": "Дизайн", "gamedev": "Геймдев", "iot": "IoT",
    }.get(domain, domain.replace("-", " ").title())

    display_name = en_skill_name.replace("-", " ").title()
    return (
        f"---\n"
        f"name: {en_skill_name}\n"
        f"description: {en_description}\n"
        f"category: {domain}\n"
        f"tags: [{en_skill_name}, {domain}, russian]\n"
        f"models: [sonnet, opus]\n"
        f"version: 1.0.0\n"
        f"language: ru\n"
        f"original: {en_skill_name}\n"
        f"---\n"
        f"# {display_name}\n\n"
        f"> {en_description}\n\n"
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


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate high-quality skills")
    parser.add_argument("domain", nargs="?", help="Domain/category for the skill")
    parser.add_argument("name", nargs="?", help="Skill name (kebab-case)")
    parser.add_argument("--description", "-d", default="", help="Skill description")
    parser.add_argument("--output-dir", "-o", default=".claude/skills", help="Output directory")
    parser.add_argument("--list-domains", action="store_true", help="List available domain templates")
    args = parser.parse_args()

    if args.list_domains:
        print("Available domain templates:")
        for d in sorted(DOMAIN_TEMPLATES):
            print(f"  {d}")
        print(f"\n  (other domains use the generic template)")
        return 0

    if not args.domain or not args.name:
        parser.print_help()
        return 1

    description = args.description or f"Professional {args.name.replace('-', ' ')} skill for Claude AI"

    en_content = generate_skill_content(args.domain, args.name, description)
    ru_content = generate_ru_content(args.name, description, args.domain)

    base = Path(args.output_dir) / args.domain / args.name
    base.mkdir(parents=True, exist_ok=True)

    en_path = base / "SKILL.md"
    ru_path = base / "SKILL.ru.md"

    en_path.write_text(en_content, encoding="utf-8")
    ru_path.write_text(ru_content, encoding="utf-8")

    print(f"Generated skill: {args.domain}/{args.name}")
    print(f"  EN: {en_path}")
    print(f"  RU: {ru_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
