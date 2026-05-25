---
name: fine-tuning-llm
description: Fine-tuning LLMs with LoRA/QLoRA
category: ai
tags: [fine-tuning, lora, qlora, llm, huggingface, pytorch]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Fine-Tuning LLMs

> Fine-tune large language models efficiently using LoRA and QLoRA for domain adaptation.

## Quick Start
```python
from datasets import load_dataset
from transformers import (
    AutoModelForCausalLM, AutoTokenizer,
    TrainingArguments, BitsAndBytesConfig
)
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from trl import SFTTrainer
import torch

# QLoRA configuration
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_use_double_quant=True
)

model = AutoModelForCausalLM.from_pretrained(
    "mistralai/Mistral-7B-v0.1",
    quantization_config=bnb_config,
    device_map="auto"
)

tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-v0.1")
tokenizer.pad_token = tokenizer.eos_token

# LoRA configuration
lora_config = LoraConfig(
    r=16,  # rank
    lora_alpha=32,
    target_modules=["q_proj", "v_proj", "k_proj", "o_proj"],
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM"
)

model = prepare_model_for_kbit_training(model)
model = get_peft_model(model, lora_config)

# Training
dataset = load_dataset("json", data_files="training_data.jsonl")
trainer = SFTTrainer(
    model=model,
    train_dataset=dataset["train"],
    args=TrainingArguments(
        per_device_train_batch_size=4,
        gradient_accumulation_steps=4,
        num_train_epochs=3,
        learning_rate=2e-4,
        fp16=True,
        logging_steps=10,
        output_dir="./lora-finetuned"
    ),
    tokenizer=tokenizer,
)
trainer.train()
```

## Key Concepts
LoRA adds small trainable rank decomposition matrices to attention layers, reducing trainable parameters by 10000x. QLoRA adds 4-bit quantization to further reduce memory. Fine-tune on 10-1000 high-quality examples for domain adaptation.

## When to Use
- Adapting models to domain-specific tasks (legal, medical, code)
- Improving model performance on specific output formats
- Teaching models new skills or knowledge

## Validation
1. Training loss decreases monotonically
2. Fine-tuned model outperforms base model on evaluation set
3. Model doesn't catastrophically forget original capabilities
4. LoRA adapter can be merged or loaded separately
