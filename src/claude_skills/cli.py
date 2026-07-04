from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path
from typing import Optional
import difflib

from claude_skills.catalog import CatalogBuilder
from claude_skills.models import QualityScore, SkillFile
from claude_skills.quality import QualityAnalyzer, QualityReport
from claude_skills.validator import ValidationPipeline, SkillValidator


REPO = "ssrjkk/claude-skills"
BRANCH = "main"
GITHUB_RAW = f"https://raw.githubusercontent.com/{REPO}/{BRANCH}"
GITHUB_API = f"https://api.github.com/repos/{REPO}"


def _find_catalog() -> Optional[Path]:
    for path in [Path("skills_catalog.json"), Path("../skills_catalog.json")]:
        if path.exists():
            return path
    return None


def _get_skills_base() -> Path:
    for path in [Path(".claude/skills"), Path("../.claude/skills")]:
        if path.exists():
            return path.resolve()
    return Path(".claude/skills")


def _github_get(path: str) -> Optional[str]:
    url = f"{GITHUB_RAW}/{path.lstrip('/')}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "claude-skills-cli"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.read().decode("utf-8")
    except (urllib.error.HTTPError, urllib.error.URLError, OSError):
        return None


def _fetch_skill_from_github(name: str) -> Optional[dict]:
    """Try to find and download a skill from GitHub by scanning categories via GitHub API."""
    url = f"{GITHUB_API}/contents/.claude/skills"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "claude-skills-cli", "Accept": "application/vnd.github.v3+json"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            categories = json.loads(resp.read().decode("utf-8"))
    except (urllib.error.HTTPError, urllib.error.URLError, OSError, json.JSONDecodeError):
        return None

    for cat in categories:
        if cat["type"] != "dir":
            continue
        cat_name = cat["name"]
        skill_url = f"{GITHUB_API}/contents/.claude/skills/{cat_name}/{name}"
        try:
            req = urllib.request.Request(skill_url, headers={"User-Agent": "claude-skills-cli", "Accept": "application/vnd.github.v3+json"})
            with urllib.request.urlopen(req, timeout=15) as resp:
                files = json.loads(resp.read().decode("utf-8"))
                has_sk = any(f["name"] == "SKILL.md" for f in files if f["type"] == "file")
                if has_sk:
                    en = None
                    ru = None
                    for f in files:
                        if f["name"] == "SKILL.md":
                            en = _github_get(f"claude/skills/{cat_name}/{name}/SKILL.md")
                        elif f["name"] == "SKILL.ru.md":
                            ru = _github_get(f"claude/skills/{cat_name}/{name}/SKILL.ru.md")
                    return {"category": cat_name, "name": name, "en": en, "ru": ru}
        except urllib.error.HTTPError:
            continue
    return None


def cmd_validate(args: argparse.Namespace) -> int:
    skills_dir = Path(args.dir)
    pipeline = ValidationPipeline(skills_dir)

    start = time.time()
    results = pipeline.run_all()
    elapsed = time.time() - start

    report = pipeline.report(results)

    print(f"Validation complete: {report['total']} files in {elapsed:.2f}s")
    print(f"  Errors:   {report['errors']}")
    print(f"  Warnings: {report['warnings']}")
    print(f"  Info:     {report['info']}")

    if report["error_details"]:
        print("\nErrors:")
        for e in report["error_details"][:10]:
            print(f"  {e}")
    if report["warning_details"]:
        print("\nWarnings (first 10):")
        for w in report["warning_details"][:10]:
            print(f"  {w}")

    return 1 if report["errors"] > 0 else 0


def cmd_quality(args: argparse.Namespace) -> int:
    skills_dir = Path(args.dir)
    analyzer = QualityAnalyzer()
    scores: dict[str, QualityScore] = {}

    for sk_path in sorted(skills_dir.rglob("SKILL.md")):
        skill_file = SkillFile(en_path=sk_path)
        content = sk_path.read_text(encoding="utf-8")
        skill_file.en_content = content

        end = content.find("---", 3)
        if end > 0:
            import yaml  # type: ignore[import-untyped]
            try:
                skill_file.en_frontmatter = yaml.safe_load(content[3:end].strip()) or {}
            except yaml.YAMLError:
                skill_file.en_frontmatter = {}
            skill_file.en_body = content[end + 3 :].strip()

        ru_path = sk_path.parent / "SKILL.ru.md"
        if ru_path.exists():
            skill_file.ru_path = ru_path
            ru_content = ru_path.read_text(encoding="utf-8")
            skill_file.ru_content = ru_content
            end_ru = ru_content.find("---", 3)
            if end_ru > 0:
                skill_file.ru_body = ru_content[end_ru + 3 :].strip()

        scores[sk_path.parent.name] = analyzer.analyze(skill_file)

    report = QualityReport(scores)
    print(report.summary())

    if args.json:
        out_path = Path(args.json)
        out_path.write_text(
            json.dumps(
                {
                    "summary": {
                        "total": len(scores),
                        "average": {
                            "completeness": report.average.completeness,
                            "depth": report.average.depth,
                            "code_quality": report.average.code_quality,
                            "freshness": report.average.freshness,
                            "bilingual": report.average.bilingual,
                            "overall": report.average.overall,
                        },
                        "grades": report.grade_distribution,
                    },
                    "skills": {name: {"overall": s.overall, "grade": s.grade} for name, s in scores.items()},
                },
                indent=2,
            ),
            encoding="utf-8",
        )
        print(f"\nReport saved to {out_path}")

    return 0


def cmd_catalog(args: argparse.Namespace) -> int:
    builder = CatalogBuilder(root=Path(args.root) if args.root else None)
    catalog = builder.build_catalog()

    out_path = Path(args.output) if args.output else Path("skills_catalog.json")
    builder.to_json(catalog, path=out_path)

    print(f"Catalog: {catalog.metadata.total_skills} skills, {len(catalog.metadata.domains)} domains")
    print(f"  RU: {catalog.metadata.total_ru} skills")
    print(f"  Saved to {out_path}")
    return 0


def cmd_stats(args: argparse.Namespace) -> int:
    builder = CatalogBuilder(root=Path(args.root) if args.root else None)
    catalog = builder.build_catalog()

    by_cat = catalog.by_category
    print(f"{'='*60}")
    print("  CLAUDE SKILLS LIBRARY — STATISTICS")
    print(f"{'='*60}")
    print(f"  Total skills:    {catalog.metadata.total_skills}")
    print(f"  Total RU:        {catalog.metadata.total_ru}")
    print(f"  Bilingual rate:  {catalog.metadata.total_ru/max(catalog.metadata.total_skills,1)*100:.1f}%")
    print(f"  Domains:         {len(catalog.metadata.domains)}")
    print(f"  Schema version:  {catalog.metadata.schema_version}")
    print(f"  Generated:       {catalog.metadata.generated_at}")
    print()
    print("  By domain:")
    for domain in sorted(by_cat):
        skills = by_cat[domain]
        ru_in_cat = sum(1 for s in skills if s.has_ru)
        print(f"    {domain:25s}: {len(skills):5d} skills, {ru_in_cat:5d} RU")

    if args.output:
        text = json.dumps(
            {
                "total_skills": catalog.metadata.total_skills,
                "total_ru": catalog.metadata.total_ru,
                "bilingual_rate": round(catalog.metadata.total_ru / max(catalog.metadata.total_skills, 1) * 100, 1),
                "domains": sorted(catalog.metadata.domains),
                "domain_skills": {d: len(by_cat[d]) for d in sorted(by_cat)},
            },
            indent=2,
            ensure_ascii=False,
        )
        Path(args.output).write_text(text, encoding="utf-8")
        print(f"\n  Stats saved to {args.output}")

    return 0


def cmd_install(args: argparse.Namespace) -> int:
    skill_name = args.skill
    target_dir = Path(args.dir)
    target_dir.mkdir(parents=True, exist_ok=True)

    skills_base = _get_skills_base()

    found: Optional[dict] = None

    if skills_base.exists():
        for domain_dir in sorted(skills_base.iterdir()):
            if not domain_dir.is_dir():
                continue
            skill_dir = domain_dir / skill_name
            if skill_dir.is_dir() and (skill_dir / "SKILL.md").exists():
                found = {"category": domain_dir.name, "name": skill_name, "en": (skill_dir / "SKILL.md").read_text(encoding="utf-8")}
                ru_path = skill_dir / "SKILL.ru.md"
                if ru_path.exists():
                    found["ru"] = ru_path.read_text(encoding="utf-8")
                break

    if not found and args.catalog:
        cat_path = Path(args.catalog)
        if cat_path.exists():
            catalog = CatalogBuilder.from_json(cat_path)
            skill_meta = catalog.get(skill_name)
            if skill_meta:
                src = Path(skill_meta.path)
                if src.exists():
                    found = {"category": skill_meta.category, "name": skill_name, "en": src.read_text(encoding="utf-8")}
                    ru_path = src.parent / "SKILL.ru.md"
                    if ru_path.exists():
                        found["ru"] = ru_path.read_text(encoding="utf-8")

    if not found:
        print(f"Searching GitHub for '{skill_name}'...", file=sys.stderr)
        found = _fetch_skill_from_github(skill_name)

    if not found:
        print(f"Error: skill '{skill_name}' not found", file=sys.stderr)
        return 1

    category = found["category"]
    target = target_dir / category / skill_name
    target.mkdir(parents=True, exist_ok=True)

    (target / "SKILL.md").write_text(found["en"], encoding="utf-8")
    if found.get("ru"):
        (target / "SKILL.ru.md").write_text(found["ru"], encoding="utf-8")

    print(f"Installed '{skill_name}' ({category}) to {target}")
    return 0


def cmd_search(args: argparse.Namespace) -> int:
    query = args.query.lower()
    limit = args.limit

    catalog_path = _find_catalog()
    if catalog_path:
        catalog = CatalogBuilder.from_json(catalog_path)
        skills_list = catalog.skills
    else:
        skills_base = _get_skills_base()
        if skills_base.exists():
            builder = CatalogBuilder()
            catalog = builder.build_catalog()
            skills_list = catalog.skills
        else:
            print("Error: no catalog found. Generate one with 'claude-skills catalog'", file=sys.stderr)
            return 1

    results = []
    for s in skills_list:
        name = s.name.lower()
        desc = s.description.lower()
        tags = [t.lower() for t in s.tags]
        name_ratio = difflib.SequenceMatcher(None, query, name).ratio()
        tag_match = any(query in t or difflib.SequenceMatcher(None, query, t).ratio() > 0.6 for t in tags)
        query_in_name = query in name
        query_in_desc = query in desc

        if query_in_name or query_in_desc or tag_match or name_ratio > 0.4:
            score = 0
            if query_in_name:
                score += 100
            if query_in_desc:
                score += 50
            if tag_match:
                score += 75
            score += int(name_ratio * 50)
            results.append((score, s))

    if args.category:
        results = [(s, skill) for s, skill in results if skill.category == args.category]
    if args.tag:
        results = [(s, skill) for s, skill in results if args.tag.lower() in [t.lower() for t in skill.tags]]

    results.sort(key=lambda x: -x[0])
    results = results[:limit]

    if args.json:
        data = [
            {
                "name": s.name,
                "description": s.description,
                "category": s.category,
                "tags": s.tags,
                "version": s.version,
                "has_ru": s.has_ru,
            }
            for _, s in results
        ]
        print(json.dumps(data, indent=2, ensure_ascii=False))
    else:
        if not results:
            print(f"No skills found for '{query}'")
            return 0
        print(f"Found {len(results)} skill(s) for '{query}':\n")
        for idx, (_, s) in enumerate(results, 1):
            ru_tag = " [RU]" if s.has_ru else ""
            print(f"  {idx}. {s.name}{ru_tag}")
            print(f"       {s.description}")
            print(f"       Category: {s.category} | Tags: {', '.join(s.tags[:5])}")
            print()

    return 0


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


def cmd_share(args: argparse.Namespace) -> int:
    target = Path(args.skill)

    if target.is_dir():
        skill_path = target / "SKILL.md"
    else:
        skill_path = target

    if not skill_path.exists():
        print(f"Error: '{skill_path}' not found", file=sys.stderr)
        return 1

    content = skill_path.read_text(encoding="utf-8")
    end = content.find("---", 3)
    if end < 0:
        print("Error: invalid skill file (no frontmatter)", file=sys.stderr)
        return 1

    front = content[3:end].strip()
    import yaml
    try:
        fm = yaml.safe_load(front) or {}
    except yaml.YAMLError:
        print("Error: invalid YAML frontmatter", file=sys.stderr)
        return 1

    name = fm.get("name", skill_path.parent.name)
    desc = fm.get("description", "")
    category = fm.get("category", "unknown")

    if args.github:
        body = (
            f"## Skill Submission\n\n"
            f"**Name:** {name}\n"
            f"**Category:** {category}\n"
            f"**Description:** {desc}\n\n"
            f"**Content:**\n```markdown\n{content}\n```\n"
        )
        import urllib.parse
        params = urllib.parse.urlencode({
            "title": f"Share skill: {name}",
            "body": body,
            "labels": "skill-submission",
        })
        url = f"https://github.com/{REPO}/issues/new?{params}"
        print(f"Open this URL to submit your skill:\n{url}")
    elif args.text:
        print(f"[Skill] {name}")
        print(f"[Category] {category}")
        print(f"[Description] {desc}")
        print()
        print(f"Install: claude-skills install {name}")
        print()
        body = (content[end + 3:]).strip()
        preview = body[:500] + "..." if len(body) > 500 else body
        print(f"Content preview:\n{preview}")
    else:
        print(f"Name:        {name}")
        print(f"Category:    {category}")
        print(f"Description: {desc}")
        print(f"Path:        {skill_path}")
        print(f"Install:     claude-skills install {name}")
        print()
        print("Use --github to create a GitHub issue or --text for a text summary.")

    return 0


def _fix_encoding():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, LookupError):
        pass


def main() -> int:
    _fix_encoding()
    parser = argparse.ArgumentParser(
        description="Claude Skills SDK — install, search, generate, and share Claude Code skills",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  claude-skills install k8s-debugger\n"
            "  claude-skills search kubernetes\n"
            "  claude-skills generate \"Debug PostgreSQL slow queries\" --domain database\n"
            "  claude-skills validate --dir .claude/skills\n"
            "  claude-skills share my-skill --github\n"
        ),
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_install = sub.add_parser("install", help="Install a skill from the catalog")
    p_install.add_argument("skill", help="Skill name to install (e.g., k8s-debugger)")
    p_install.add_argument("--dir", default=".claude/skills", help="Target skills directory (default: .claude/skills)")
    p_install.add_argument("--catalog", help="Path to catalog JSON (auto-detected if omitted)")
    p_install.set_defaults(func=cmd_install)

    p_search = sub.add_parser("search", help="Search skills in the catalog")
    p_search.add_argument("query", help="Search query")
    p_search.add_argument("--category", help="Filter by category")
    p_search.add_argument("--tag", help="Filter by tag")
    p_search.add_argument("--limit", type=int, default=20, help="Max results (default: 20)")
    p_search.add_argument("--json", action="store_true", help="Output as JSON")
    p_search.set_defaults(func=cmd_search)

    p_generate = sub.add_parser("generate", help="Generate a new skill via template or LLM")
    p_generate.add_argument("prompt", help="Description of the skill to generate")
    p_generate.add_argument("--domain", help="Domain/category (auto-detected from prompt if omitted)")
    p_generate.add_argument("--name", help="Skill name in kebab-case (auto-generated from prompt if omitted)")
    p_generate.add_argument("--dir", default=".claude/skills", help="Output directory (default: .claude/skills)")
    p_generate.add_argument("--api", action="store_true", help="Use Claude API for generation (requires ANTHROPIC_API_KEY)")
    p_generate.set_defaults(func=cmd_generate)

    p_share = sub.add_parser("share", help="Share a skill (format for GitHub issue or text output)")
    p_share.add_argument("skill", help="Path to skill directory or SKILL.md file")
    p_share.add_argument("--github", action="store_true", help="Generate GitHub issue link")
    p_share.add_argument("--text", action="store_true", help="Output formatted text summary")
    p_share.set_defaults(func=cmd_share)

    p_validate = sub.add_parser("validate", help="Validate all skills")
    p_validate.add_argument("--dir", default=".claude/skills", help="Skills directory")
    p_validate.set_defaults(func=cmd_validate)

    p_quality = sub.add_parser("quality", help="Analyze skill quality")
    p_quality.add_argument("--dir", default=".claude/skills", help="Skills directory")
    p_quality.add_argument("--json", help="Output JSON report to path")
    p_quality.set_defaults(func=cmd_quality)

    p_catalog = sub.add_parser("catalog", help="Build catalog from skills")
    p_catalog.add_argument("--root", help="Project root directory")
    p_catalog.add_argument("-o", "--output", help="Output path for catalog JSON")
    p_catalog.set_defaults(func=cmd_catalog)

    p_stats = sub.add_parser("stats", help="Show statistics")
    p_stats.add_argument("--root", help="Project root directory")
    p_stats.add_argument("--output", help="Save stats to JSON")
    p_stats.set_defaults(func=cmd_stats)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
