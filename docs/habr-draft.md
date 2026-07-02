# Habr Article Draft (Russian)

## Заголовок
**Как я создал крупнейшую библиотеку навыков для Claude: 10,000+ скиллов на 39 доменов**

## Вступление
Все мы знаем эту ситуацию: просишь Claude написать тесты — получаешь базовые примеры. Просишь настроить Kubernetes — получаешь generic манифест. Каждый раз нужно объяснять контекст заново.

Я решил эту проблему раз и навсегда.

## Проблема
- Каждый запрос к AI требует контекста
- Результаты непредсказуемы
- Нет стандартизации в команде
- Потеря времени на однотипные объяснения

## Решение: структурированные навыки
YAML frontmatter + markdown body. Каждый навык — это:
- name, description, category
- tags для поиска
- models для совместимости
- version для версионирования

## Архитектура
- .claude/skills/{domain}/{skill}/SKILL.md
- Python SDK для валидации
- Система оценки качества (A–F)
- Двуязычность (EN + RU)

## Масштабирование до 10,000
...

## Результаты
- 10,000+ навыков
- 39 доменов
- 93% test coverage
- 7.8 секунд на полную валидацию
- Первая двуязычная библиотека

## Как использовать
```bash
curl -fsSL https://raw.githubusercontent.com/ssrjkk/claude-skills/main/install.sh | bash
claude-skills stats
```

## Ссылки
- GitHub: https://github.com/ssrjkk/claude-skills
- Документация: https://ssrjkk.github.io/claude-skills/
- Telegram: t.me/claude_skills
