---
name: llm-finetuning
description: "Fine-tunes open-source LLMs (Llama, Mistral, Qwen) using LoRA/QLoRA with HuggingFace and Unsloth. Use for domain-specific model adaptation."
category: ai
tags: [llm-finetuning, ai, russian]
models: [sonnet, opus]
version: "1.0"
language: ru
original: llm-finetuning
---
# LLM Fine-Tuning (Тонкая настройка LLM)

> Дообучивайте open-source LLM через LoRA/QLoRA под доменные задачи.

## Быстрый старт
```python
from unsloth import FastLanguageModel
from datasets import load_dataset
from trl import SFTTrainer

# Загрузка модели с LoRA
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="unsloth/Meta-Llama-3.1-8B",
    max_seq_length=2048,
    load_in_4bit=True,  # QLoRA
)

model = FastLanguageModel.get_peft_model(
    model,
    r=16,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj"],
    lora_alpha=16,
    lora_dropout=0,
)

# Обучение
dataset = load_dataset("json", data_files="training_data.json")
trainer = SFTTrainer(
    model=model,
    tokenizer=tokenizer,
    train_dataset=dataset,
    dataset_text_field="text",
    max_seq_length=2048,
)
trainer.train()
```

## Когда использовать
- Доменная адаптация моделей
- Задача-специфичное дообучение (чат, код, классификация)
- Не для простых задач prompt engineering

## Пошаговые инструкции
1. Выберите базовую модель (Llama 3, Mistral, Qwen)
2. Подготовьте обучающий датасет в chat-формате
3. Настройте параметры LoRA/QLoRA
4. Обучите и сохраните адаптер

## Зависимости
```bash
pip install unsloth transformers datasets trl accelerate
```

## Примеры
Вход: обучающий датасет из 1000 примеров → Выход: дообученный LoRA-адаптер (50MB)

## Ресурсы
- [Unsloth](https://github.com/unslothai/unsloth)
- [HuggingFace SFT](https://huggingface.co/docs/trl/sft_trainer)
- [Examples](./examples/)

## Устранение неполадок
- **Потери рано выходят на плато** — слишком высокий learning rate.
  Уменьшите его в 10 раз и снизьте batch size, пока валидация не падает.
- **Катастрофическое забывание** — подмешивайте 5–10% исходного датасета
  в каждую эпоху или заморозьте первую треть модели через LoRA.
- **OOM при обучении** — используйте накопление градиентов,
  `gradient_checkpointing` (при обучении) и 4-битную QLoRA для GPU.
- **Модель повторяет обучающие данные** — переобучение. Увеличьте dropout,
  сократите число эпох и добавьте валидационный сплит с early stopping.

## Валидация
1. Loss стабильно снижается
2. Модель генерирует связные ответы после обучения
3. Адаптер успешно мёрджится (при необходимости)
