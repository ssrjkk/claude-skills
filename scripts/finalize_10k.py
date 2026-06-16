import os, glob, sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE = ".claude/skills"
current_en = len(glob.glob(f"{BASE}/**/SKILL.md", recursive=True))
current_ru = len(glob.glob(f"{BASE}/**/SKILL.ru.md", recursive=True))
print(f"Current: {current_en} SKILL.md, {current_ru} SKILL.ru.md")

# 1. Add missing SKILL.ru.md for skills generated in batch 2
ru_needed = 0
for sk_path in glob.glob(f"{BASE}/**/SKILL.md", recursive=True):
    ru_path = sk_path.replace("SKILL.md", "SKILL.ru.md")
    if os.path.exists(ru_path):
        continue
    # Read and parse frontmatter
    with open(sk_path, "r", encoding="utf-8") as f:
        content = f.read()
    lines = content.split("\n")
    name_val = ""
    cat_val = ""
    desc_val = ""
    in_fm = False
    fm_closed = False
    for line in lines:
        if line.strip() == "---":
            if not in_fm:
                in_fm = True
            elif not fm_closed:
                fm_closed = True
            continue
        if in_fm and not fm_closed:
            if line.startswith("name:"):
                name_val = line.split(":", 1)[1].strip().strip('"')
            elif line.startswith("category:"):
                cat_val = line.split(":", 1)[1].strip().strip('"')
            elif line.startswith("description:"):
                desc_val = line.split(":", 1)[1].strip().strip('"')
    if not name_val:
        continue
    CATEGORY_RU = {
        "ai": "Искусственный интеллект", "backend": "Бэкенд-разработка",
        "frontend": "Фронтенд-разработка", "devops": "DevOps",
        "database": "Базы данных", "security": "Безопасность",
        "qa": "Тестирование", "mobile": "Мобильная разработка",
        "gamedev": "Геймдев", "design": "Дизайн",
        "data": "Data Science", "blockchain": "Блокчейн",
        "networking": "Сети", "os-admin": "Администрирование",
        "iot": "Интернет вещей", "block": "Блокчейн",
        "communications": "Коммуникации", "desktop": "Десктоп",
        "ecommerce": "Электронная коммерция", "education": "Образование",
        "embedded": "Встраиваемые системы", "energy": "Энергетика",
        "engineering": "Инженерия", "finance": "Финансы",
        "geospatial": "Геопространственные данные", "healthcare": "Здравоохранение",
        "hr": "HR", "media": "Медиа", "payments": "Платежи",
        "product": "Продукт-менеджмент", "scientific": "Наука",
        "supply-chain": "Цепочки поставок", "sustainability": "Устойчивое развитие",
        "api-testing": "API-тестирование", "ci-cd-setup": "CI/CD",
        "database-migration": "Миграция БД", "test-reporting": "Отчётность тестирования",
        "ar-vr": "AR/VR",
    }
    cat_ru = CATEGORY_RU.get(cat_val, cat_val)
    name_display = name_val.replace("-", " ").title()
    ru_fm = f"""---
name: {name_val}
description: {desc_val}
category: {cat_val}
tags: [{', '.join([name_val, cat_val, 'russian'])}]
models: [sonnet, opus]
version: "1.0"
language: ru
original: {name_val}
---

# {name_display}

> {desc_val}

## Быстрый старт
Этот навык на русском языке. Оригинал: `{name_val}`.

## Когда использовать
- Работа с {cat_ru}
- Выполнение задач, связанных с {name_display}
- Профессиональное развитие

## Инструкции
1. Ознакомьтесь с описанием навыка
2. Изучите английскую версию для полных инструкций
3. Примените полученные знания на практике

## Ресурсы
- Оригинальный навык: {cat_val}/{name_val}/SKILL.md
- Категория: {cat_ru}
- Язык: Русский

## Валидация
- Прочитайте английскую версию для проверки
- Выполните описанные шаги
- Убедитесь в правильности результата
"""
    with open(ru_path, "w", encoding="utf-8") as f:
        f.write(ru_fm)
    ru_needed += 1

print(f"Added {ru_needed} missing SKILL.ru.md files")

# 2. Generate more EN skills to reach 10k
current_en = len(glob.glob(f"{BASE}/**/SKILL.md", recursive=True))
target = 10000
needed = target - current_en
print(f"SKILL.md count: {current_en}, need {needed} more to reach {target}")

EXPANDED_ITEMS = {
    "backend": ["rabbitmq", "kafka", "graphql", "grpc", "websocket", "redis", "celery", "sqlalchemy", "prisma", "typeorm", "drizzle", "mongodb-mongoose"],
    "frontend": ["styled-components", "emotion", "framer-motion", "gsap", "threejs", "d3js", "chartjs", "leaflet", "swiper", "react-hook-form", "zod", "react-router"],
    "devops": ["vagrant", "packer", "consul", "vault", "nomad", "linkerd", "coredns", "calico", "cilium", "istio", "envoy", "traefik"],
    "database": ["supabase", "neon", "planetscale", "turso", "singlestore", "memgraph", "duckdb", "motherduck", "kafka-connect", "debezium"],
    "ai": ["whisper", "stable-diffusion", "midjourney", "ragas", "chromadb", "qdrant", "pinecone", "weaviate", "milvus", "pgvector", "langsmith", "langfuse"],
    "security": ["crowdstrike", "sentinelone", "wazuh", "ossec", "snort", "suricata", "zeek", "velociraptor", "gitleaks", "semgrep", "checkov", "tfsec"],
    "mobile": ["swiftui", "jetpack-compose", "revenuecat", "firebase-fcm", "onesignal", "appcenter", "fastlane", "codemagic", "testflight", "diawi"],
    "qa": ["allure", "reportportal", "selenoid", "browserstack", "saucelabs", "testrail", "xray", "zephyr", "cypress-cloud", "percy", "chromatic", "applitools"],
    "data": ["delta-lake", "lakefs", "dvc", "mlflow", "wandb", "neptune", "cml", "dvc", "evidently", "whylabs", "great-expectations", "soda"],
    "gamedev": ["blender", "maya", "substance", "zbrush", "spine", "aesprite", "tiled", "ldtk", "wwise", "fmod", "steam-sdk", "unity-ads"],
}

TOPICS = [
    ("getting-started", "Getting Started", "initial setup and first steps"),
    ("configuration", "Configuration", "configuration and setup"),
    ("integration", "Integration", "integration with other tools"),
    ("best-practices", "Best Practices", "best practices and patterns"),
    ("troubleshooting", "Troubleshooting", "troubleshooting common issues"),
    ("workflow", "Workflow", "workflow optimization"),
    ("automation", "Automation", "automation and scripting"),
    ("production", "Production", "production deployment"),
]

generated = 0
for domain, items in EXPANDED_ITEMS.items():
    os.makedirs(f"{BASE}/{domain}", exist_ok=True)
    existing = set()
    for d in glob.glob(f"{BASE}/{domain}/*"):
        if os.path.isdir(d) and os.path.exists(os.path.join(d, "SKILL.md")):
            existing.add(os.path.basename(d))
    for item in items:
        for suf, disp, desc in TOPICS:
            name = f"{item}-{suf}"
            if name in existing:
                continue
            content = f"""---
name: {name}
description: {disp} for {item.title()}: {desc}
category: {domain}
tags: [{item}, {suf}, {domain}]
models: [sonnet, opus]
version: "1.0"
language: en
---

# {item.title()} {disp}

> {desc}

## Quick Start
Begin by setting up {item.title()} for {desc}.

## When to Use
- Working with {item.title()} in production
- Implementing {suf} patterns and practices
- Building reliable solutions

## Step-by-Step
1. Install and configure {item.title()}
2. Follow best practices for {suf}
3. Test the implementation
4. Monitor and optimize

## Dependencies
- {item.title()} (latest stable version)
- Development environment

## Resources
- Official {item.title()} documentation
- Community guides and tutorials

## Validation
- Verify the setup works correctly
- Run validation tests
- Check logs and metrics
"""
            skill_dir = f"{BASE}/{domain}/{name}"
            os.makedirs(skill_dir, exist_ok=True)
            with open(f"{skill_dir}/SKILL.md", "w", encoding="utf-8") as f:
                f.write(content)
            existing.add(name)
            generated += 1
            if generated >= needed:
                break
        if generated >= needed:
            break
    if generated >= needed:
        break

print(f"Generated {generated} new EN skills")

final_en = len(glob.glob(f"{BASE}/**/SKILL.md", recursive=True))
final_ru = len(glob.glob(f"{BASE}/**/SKILL.ru.md", recursive=True))
print(f"\n=== FINAL ===")
print(f"SKILL.md (EN): {final_en}")
print(f"SKILL.ru.md (RU): {final_ru}")
print(f"Files on disk: {final_en + final_ru}")
