---
name: python-311
description: "Python 3.11-3.13 new features"
category: backend
tags: [python, 3.11, 3.12, 3.13, features, typing]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Python 3.13

> Leverage the latest Python features from 3.11 through 3.13 for cleaner, faster, safer code.

## Quick Start
```python
# Python 3.11+ features

# 1. Variadic generics (3.11)
from typing import TypeVar, Generic

T = TypeVar("T")
Ts = TypeVar("Ts", *Ts)

class Array(Generic[T, *Ts]):
    def __init__(self, shape: tuple[int, *Ts]):
        self.shape = shape

# 2. Self type (3.11)
from typing import Self

class Builder:
    def set_name(self, name: str) -> Self:
        self.name = name
        return self
    
    def build(self) -> dict:
        return {"name": self.name}

# 3. Except* for exception groups (3.11)
try:
    raise ExceptionGroup("errors", [
        ValueError("bad value"),
        TypeError("bad type"),
    ])
except* ValueError as e:
    print(f"Value errors: {e.exceptions}")
except* TypeError as e:
    print(f"Type errors: {e.exceptions}")

# Python 3.12+ features

# 4. Type parameter syntax (3.12)
def first[T](items: list[T]) -> T:
    return items[0]

class Container[T]:
    def __init__(self, value: T):
        self.value = value

# 5. Override decorator (3.12)
from typing import override

class Base:
    def method(self) -> str:
        return "base"

class Derived(Base):
    @override
    def method(self) -> str:
        return "derived"

# Python 3.13+ features

# 6. Free-threaded CPython (3.13, experimental)
# Run with: python -X gil=1 script.py
import sys
sys._enable_gil(False)  # Disable GIL for CPU-bound threads

# 7. JIT compiler (3.13, experimental)
# Enabled with: PYTHON_JIT=1 python script.py

# 8. match statement improvements
def process(value: str | int | None) -> str:
    match value:
        case str() as s if len(s) > 10:
            return f"Long string: {s}"
        case int() as n:
            return f"Number: {n}"
        case None:
            return "Nothing"
        case _:
            return "Unknown"
```

## Key Concepts
Python 3.11: exception groups, Self type, variadic generics. Python 3.12: type parameter syntax, override decorator, perf improvements. Python 3.13: free-threaded mode (no GIL), experimental JIT, improved error messages.

## When to Use
- New projects should target 3.12+ for modern type features
- CPU-bound Python where free-threading improves performance
- Codebases wanting stricter type safety with new typing features

## Validation
1. Code runs with `python --version` matching target
2. Type hints pass `mypy --strict` or `pyright`
3. Exception groups propagate and catch correctly
4. Performance benchmarks show expected gains with free-threading
