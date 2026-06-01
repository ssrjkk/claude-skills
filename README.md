# Claude Skills Library

> 🚀 **Лидерская библиотека специализированных навыков для Claude AI**

Это официальная коллекция 10,000+ высококачественных, проверенных Claude Skills для повышения производительности разработки, тестирования, развертывания и управления.

## 🎯 Что такое Claude Skills?

Claude Skills — это структурированные, пошаговые инструкции, оптимизированные для работы с Claude AI. Каждый навык содержит:
- ✅ Четкие, атомарные шаги
- ✅ Примеры использования в реальных проектах
- ✅ Best practices от индустрии
- ✅ Проверенные инструменты и альтернативы

## 📊 Статистика библиотеки

| Метрика | Значение |
|---------|----------|
| **Всего навыков** | 10,000+ |
| **Категорий** | 50 |
| **Языков** | English, Русский |
| **Статус** | Production Ready ✅ |

Подробнее: [SKILLS_STATISTICS.md](SKILLS_STATISTICS.md)

## 📚 Навигация

- **[Каталог навыков](SKILLS_LIBRARY.md)** — Полный индекс всех навыков по категориям
- **[Как начать](CONTRIBUTING.md)** — Руководство для контрибьюторов
- **[Система валидации](.github/workflows/validate-skills.yml)** — Автоматическая проверка качества

## 🏗️ Структура репозитория

```
claude-skills/
├── .github/
│   ├── copilot-instructions.md        # Claude system prompt
│   ├── copilot-custom-instructions.md # Copilot context
│   └── workflows/
│       └── validate-skills.yml         # CI/CD pipeline
├── scripts/                            # Инструменты валидации
│   ├── validate_schema.py             # JSON validation
│   ├── check_ids.py                   # Duplicate detection
│   ├── check_skill_fields.py          # Required fields check
│   ├── detect_anti_patterns.py        # Pattern detection
│   ├── generate_stats.py              # Statistics generation
│   ├── generate_index.py              # Index generation
│   └── test_examples.py               # Example testing
├── skills/                             # Individual skills directory
├── skills_library.json                # Main skills catalog
├── SKILLS_LIBRARY.md                  # Generated index
├── SKILLS_STATISTICS.md               # Generated stats
├── CONTRIBUTING.md                    # Contribution guidelines
├── README.md                          # This file
└── LICENSE                            # MIT License
```

## 🚀 Быстрый старт

### Для пользователей
1. Посмотри каталог навыков в [SKILLS_LIBRARY.md](SKILLS_LIBRARY.md)
2. Найди нужный навык по категории или ключевому слову
3. Используй инструкции на своем проекте

### Для контрибьюторов
1. Прочитай [CONTRIBUTING.md](CONTRIBUTING.md)
2. Следуй [системе промптов](.github/copilot-instructions.md)
3. Запусти валидацию: `python scripts/validate_schema.py skills_library.json`
4. Отправь PR с новым навыком

## ✅ Система контроля качества

Каждый навык автоматически проверяется:
- ✅ **JSON Schema Validation** — структура и обязательные по��я
- ✅ **Duplicate Detection** — уникальность ID
- ✅ **Field Verification** — все требуемые поля присутствуют
- ✅ **Anti-Pattern Detection** — нет вагу-формулировок
- ✅ **Example Testing** — примеры выполнимы
- ✅ **Statistics Auto-Generation** — автоматическое обновление статистики

### Запуск проверок локально

```bash
# Проверить JSON схему
python scripts/validate_schema.py skills_library.json --strict

# Найти дубликаты
python scripts/check_ids.py skills_library.json

# Проверить обязательные поля
python scripts/check_skill_fields.py skills_library.json

# Обнаружить антипаттерны
python scripts/detect_anti_patterns.py skills_library.json

# Генерировать статистику
python scripts/generate_stats.py skills_library.json

# Генерировать индекс
python scripts/generate_index.py skills_library.json
```

## 📖 Форматы

### Структура Skill в JSON

```json
{
  "id": "DEV-PY-042",
  "category": "Development",
  "subcategory": "Python",
  "title": "Implementing Type-Safe Database Queries",
  "description": "Create ORM-based queries with automatic type validation",
  "difficulty": "intermediate",
  "time_estimate": "1h",
  "prerequisites": ["DEV-PY-001"],
  "steps": [
    "Install SQLAlchemy: pip install sqlalchemy",
    "Define model with type hints: class User(Base):",
    "..."
  ],
  "best_practices": [
    "Always use type hints for columns",
    "Validate input at query time"
  ],
  "tools": [
    "SQLAlchemy (ORM framework)",
    "PostgreSQL (database)"
  ],
  "keywords": ["database", "ORM", "SQLAlchemy"],
  "examples": [
    {
      "scenario": "Build user lookup query",
      "input": "user_id=42",
      "output": "User(id=42, name='Alice')",
      "context": "API endpoint for fetching user profile"
    }
  ],
  "anti_patterns": [
    "❌ Dynamic query construction without escaping",
    "❌ N+1 query problems with relationships"
  ],
  "related_skills": ["DEV-PY-041", "DEV-PY-043"],
  "language": "en"
}
```

## 🌍 Поддерживаемые категории

| Категория | Примеры |
|-----------|---------|
| **Development** | Python, JavaScript, Go, Rust, Java |
| **Testing** | Unit, Integration, E2E, Performance |
| **Deployment** | Docker, Kubernetes, CI/CD |
| **DevOps** | Monitoring, Logging, Infrastructure |
| **Security** | Authentication, Encryption, Compliance |
| **AI** | LLM Integration, Prompt Engineering |
| **Documentation** | API Docs, Architecture |

## 🤝 Лицензия

MIT License — используй свободно в коммерческих и личных проектах.

## 💬 Контакт

- **GitHub Issues** — Для отчетов об ошибках и предложений
- **Discussions** — Для обсуждения новых идей

---

**Миссия**: Создать де-факто стандартную библиотеку Claude Skills, которая будет форкаться и использоваться тысячами разработчиков по всему миру. 🚀

**Качество > Количество** — Каждый навык 100% верифицирован.
