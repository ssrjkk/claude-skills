# Claude Models Compatibility Matrix

## Quick Reference

|Model|Speed|Context Window|Best For|
|-------|:-----:|:--------------:|----------|
|**Haiku**|Fastest|200K tokens|Simple, repetitive tasks, quick code gen|
| **Sonnet**|Balanced|200K tokens|**Most skills** (recommended default)|
|**Opus**|Most powerful|200K tokens|Complex reasoning, architecture, security|

## Skill Coverage by Model

All **21 skills** across **11 domains** are tested with **Sonnet** and **Opus**.

|Domain|Skills|Sonnet|Opus|
|--------|:-----:|:------:|:----:|
|DevOps|7||||
|Backend|3||||
|AI|2||||
|Frontend|2||||
|Blockchain|1||||
|Database|1||||
|Desktop|1||||
|Embedded|1||||
|Engineering|1||||
|Mobile|1||||
|Security|1||||

> Full support · No recommendation

## Recommendations

|Use Case|Recommended Model|
|----------|:-----------------:|
|Daily development, CRUD, scripting|**Sonnet**|
|Complex architecture, system design|**Opus**|
|Simple automation, file operations|**Haiku**|
|Security audits, penetration testing|**Opus**|
|Smart contract development|**Opus**|
|ML pipeline design|**Opus**|
|Quick code snippets, bash scripts|**Haiku**|

## Model Notes

- 20 of 21 skills declare `models: [sonnet, opus]`.
- `ai/llm-finetuning` is **Opus-only** (full fine-tuning runs benefit from the
  strongest reasoning model).
- No skill in the curated library declares Haiku support.

---

*Last updated: 2026-09-06*