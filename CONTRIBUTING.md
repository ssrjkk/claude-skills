# Contribution Guidelines

Спасибо за желание добавить навык в Claude Skills Library! Следуй этому руководству.

## 📋 Требования к Skill

Каждый skill ДОЛЖЕН содержать:

```json
{
  "id": "CAT-SUB-###",
  "category": "Development|Testing|Deployment|DevOps|Security|AI|Documentation|Other",
  "subcategory": "Конкретная область",
  "title": "Действие в форме герундия: Implementing X, Building Y",
  "description": "Одна строка - результат, который получит пользователь",
  "difficulty": "beginner|intermediate|advanced",
  "time_estimate": "15min|1h|4h|1d",
  "prerequisites": ["CAT-SUB-001"],
  "steps": [
    "Атомарный шаг 1",
    "Атомарный шаг 2",
    "Каждый шаг - 5-15 минут"
  ],
  "best_practices": [
    "Производственный паттерн с источником",
    "Общая ошибка и как её избежать"
  ],
  "tools": [
    "Основной инструмент",
    "Альтернатива #1",
    "Альтернатива #2"
  ],
  "keywords": ["keyword1", "keyword2"],
  "examples": [
    {
      "scenario": "Реальный use case",
      "input": "Входные данные",
      "output": "Ожидаемый результат",
      "context": "Когда использовать"
    }
  ],
  "anti_patterns": [
    "❌ Что НЕ делать и почему",
    "❌ Частая ошибка"
  ],
  "related_skills": ["CAT-SUB-003", "CAT-SUB-004"],
  "language": "en"
}
```

## ✅ Чек-лист перед отправкой

- [ ] ID имеет формат `{CATEGORY}-{SUBCATEGORY}-{###}`
- [ ] Заголовок использует герундий (Implementing, Building, Configuring)
- [ ] Описание - результат, не процесс
- [ ] Все шаги атомарные и независимые
- [ ] Best practices ссылаются на авторитеты (OWASP, AWS, etc.)
- [ ] Инструменты: 2-3 вариант с ранжированием
- [ ] Примеры: happy path + edge case
- [ ] Нет дубликатов в библиотеке
- [ ] JSON валидируется: `python scripts/validate_schema.py skills_library.json --strict`

## 🔴 Недопустимо

| ❌ Неправильно | ✅ Правильно |
|---|---|
| "Learn about X" | "Implementing X with Y in Z minutes" |
| Расплывчатые шаги | Точные команды: `terraform apply` |
| Один инструмент | Несколько альтернатив |
| Платные инструменты | Free tier или open-source |
| Без примеров | С примерами выполнения |

## 🚀 Процесс обновления

1. **Создай ветку**: `git checkout -b skill/category/descriptive-name`
2. **Добавь skill** в `skills_library.json` в массив `"skills"`
3. **Локально проверь**: 
   ```bash
   python scripts/validate_schema.py skills_library.json --strict
   ```
4. **Отправь PR** с описанием added skill
5. **Получи review** - проверим по чек-листу
6. **Merge** - автоматически обновится статистика

## 📝 Примеры навыков

Посмотри существующие skills в `skills_library.json` для вдохновения. Они все следуют одному стандарту.

## 🆘 Вопросы?

- Посмотри [README.md](README.md) для обзора
- Прочитай `.github/copilot-instructions.md` для деталей
- Открой issue с вопросом

---

**Remember**: Качество важнее количества. Один отличный skill лучше 100 посредственных! 🎯
