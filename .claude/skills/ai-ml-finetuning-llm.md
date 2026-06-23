# Fine-Tuning Large Language Models

## Overview
Master fine-tuning techniques for large language models including LoRA, QLoRA, instruction tuning, and domain adaptation.

## Context
You are an ML engineer optimizing LLMs for specific domains. You understand tokenization, loss functions, and training strategies.

## Key Principles
- **Parameter Efficiency**: Use LoRA instead of full fine-tuning
- **Data Quality**: High-quality data beats quantity
- **Domain Adaptation**: Specialize models for your use case
- **Cost**: Fine-tuning should be affordable
- **Evaluation**: Measure before and after

## Step-by-Step Instructions

### 1. LoRA (Low-Rank Adaptation)
```python
import torch
from peft import get_peft_model, LoraConfig, TaskType
from transformers import AutoModelForCausalLM

# Load base model
model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b")

# Configure LoRA
lora_config = LoraConfig(
    r=8,  # LoRA rank
    lora_alpha=16,
    target_modules=["q_proj", "v_proj"],  # Which layers to adapt
    lora_dropout=0.05,
    task_type=TaskType.CAUSAL_LM
)

# Wrap model
model = get_peft_model(model, lora_config)

# Only 0.3% parameters are trainable!
trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
total_params = sum(p.numel() for p in model.parameters())
print(f"Trainable: {trainable_params/total_params*100:.2f}%")
```

### 2. QLoRA (Quantized LoRA)
```python
from transformers import AutoModelForCausalLM, BitsAndBytesConfig
from peft import get_peft_model, LoraConfig

# Quantize to 4-bit
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16
)

# Load 70B model in 20GB VRAM
model = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Llama-2-70b",
    quantization_config=bnb_config,
    device_map="auto"
)

# Apply LoRA
lora_config = LoraConfig(
    r=16,
    lora_alpha=32,
    target_modules=["q_proj", "v_proj", "k_proj", "o_proj"]
)

model = get_peft_model(model, lora_config)
```

### 3. Instruction Tuning
```python
from datasets import Dataset
from transformers import TrainingArguments, Trainer, AutoTokenizer
import torch

# Prepare dataset
data = [
    {
        "instruction": "Classify the sentiment",
        "input": "I love this product!",
        "output": "Positive"
    },
    {
        "instruction": "Classify the sentiment",
        "input": "This is terrible.",
        "output": "Negative"
    }
]

# Format as prompts
def format_prompt(example):
    return {
        "text": f"Instruction: {example['instruction']}\nInput: {example['input']}\nOutput: {example['output']}"
    }

dataset = Dataset.from_dict({
    "text": [format_prompt(d)["text"] for d in data]
})

# Tokenize
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b")

def tokenize(example):
    return tokenizer(
        example["text"],
        truncation=True,
        max_length=512,
        padding="max_length"
    )

tokenized = dataset.map(tokenize, batched=True)

# Train
training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=3,
    per_device_train_batch_size=4,
    learning_rate=5e-4,
    save_steps=100,
    logging_steps=10
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized,
    tokenizer=tokenizer
)

trainer.train()
```

### 4. Domain Adaptation
```python
# Continued pre-training on domain data
from transformers import TextDataset, DataCollatorForLanguageModeling

# Load domain-specific text
domain_data = TextDataset(
    tokenizer=tokenizer,
    file_path="domain_texts.txt",
    block_size=512
)

data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=False
)

# Pre-train on domain
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=domain_data,
    data_collator=data_collator
)

trainer.train()
```

### 5. Evaluation & Metrics
```python
from datasets import load_metric
from transformers import pipeline

# Generate and evaluate
pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)

prompt = "Classify the sentiment: I really enjoyed this movie"
output = pipe(prompt, max_length=100, do_sample=True)

# BLEU score
bleu = load_metric("bleu")
predictions = ["I like this movie"]
references = [["I really enjoyed this movie"]]
results = bleu.compute(predictions=predictions, references=references)
```

## Real-World Examples

### Example 1: Customer Support Bot
```python
# Fine-tune Llama-2-7b for support tickets

# Training data
support_data = [
    {
        "instruction": "Respond to a support ticket",
        "input": "I cannot login to my account",
        "output": "Please try resetting your password..."
    },
    {
        "instruction": "Respond to a support ticket",
        "input": "Billing issue",
        "output": "I'll help you with your billing..."
    }
]

# LoRA config (99.7% parameters frozen)
lora_config = LoraConfig(r=8, lora_alpha=16, target_modules=["q_proj", "v_proj"])

# Train for 1 hour on GPU
# Deploy with 4x speedup over base model
```

### Example 2: Code Generation Model
```python
# Fine-tune on Python code
code_dataset = CodeDataset("python_code_samples.txt")

# Higher learning rate for code
trainer = Trainer(
    model=model,
    args=TrainingArguments(
        learning_rate=1e-3,
        num_train_epochs=5,
        per_device_train_batch_size=8
    ),
    train_dataset=code_dataset
)

# Result: Model generates better Python code
```

### Example 3: Multi-task Fine-tuning
```python
# Fine-tune on multiple tasks
multi_task_data = [
    {"task": "classification", "input": "...", "output": "..."},
    {"task": "summarization", "input": "...", "output": "..."},
    {"task": "qa", "input": "...", "output": "..."}
]

# Single model handles all tasks
# Outperforms single-task models
```

## Best Practices
- ✅ Use LoRA for 90% of cases
- ✅ Use QLoRA if memory-constrained
- ✅ Quality > quantity (100 good examples > 10k bad)
- ✅ Instruction format: be consistent
- ✅ Evaluate on held-out test set
- ✅ Monitor for catastrophic forgetting
- ✅ Use validation set to prevent overfitting
- ❌ Don't fine-tune if you don't have labeled data
- ❌ Don't ignore data leakage
- ❌ Don't use base model on production

## Advanced Patterns

### Multi-LoRA Adapters
```python
# Load base model once, multiple adapters
base_model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b")

# Adapter for support
support_adapter = LoraConfig(...)
model_support = get_peft_model(base_model, support_adapter)

# Adapter for coding
code_adapter = LoraConfig(...)
model_code = get_peft_model(base_model, code_adapter)

# Load specific adapter at inference time
model.load_adapter("support")  # Switch task
```

## Metrics to Track
- Loss (training and validation)
- Perplexity
- BLEU score
- Task-specific metrics (accuracy, F1)
- Inference latency

## Tools
- Hugging Face Transformers
- PEFT (Parameter Efficient Fine-Tuning)
- PyTorch
- Weights & Biases (tracking)

## Common Pitfalls
1. **Too many epochs**: Catastrophic forgetting
2. **Too high learning rate**: Divergence
3. **Imbalanced data**: One class dominates
4. **No validation set**: Overfitting
5. **Wrong batch size**: Memory issues

## Related Skills
- ai-ml-langchain-rag
- ai-ml-prompt-engineering-advanced
- backend-python-async-api
