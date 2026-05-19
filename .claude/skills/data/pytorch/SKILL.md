---
name: pytorch
description: Builds and trains deep learning models with PyTorch, including tensors, autograd, and neural network modules.
category: data
tags: [pytorch, deep-learning, neural-networks, tensor, gpu]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# PyTorch

> Machine learning framework with dynamic computation graphs.

## Quick Start
```python
import torch, torch.nn as nn
model = nn.Sequential(nn.Linear(784, 256), nn.ReLU(), nn.Linear(256, 10), nn.LogSoftmax(dim=1))
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
for images, labels in dataloader:
    output = model(images); loss = nn.CrossEntropyLoss()(output, labels)
    loss.backward(); optimizer.step(); optimizer.zero_grad()
```

## Custom Module
```python
class MyCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 32, 3); self.dropout = nn.Dropout2d(0.25)
        self.fc1 = nn.Linear(5408, 128)
    def forward(self, x):
        x = self.conv1(x); x = self.dropout(x); return self.fc1(x)
```

## When to Use
- Deep learning research
- Custom neural architectures
- NLP and computer vision
- GPU-accelerated training

## Validation
1. Model runs forward pass without error
2. Loss decreases during training
3. GPU utilization is correct
