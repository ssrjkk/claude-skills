---
name: unreal
description: "Creates games on Unreal Engine with Blueprints or C++. Use for AAA-quality and high-performance games."
category: gamedev
tags: [unreal, cpp, blueprint, game-dev, aaa]
models: [opus]
version: 1.0.0
created: 2026-05-01
---
# Unreal Engine

> Professional engine for AAA games with Blueprints and C++.

## Quick Start
```cpp
// MyActor.cpp
#include "MyActor.h"

void AMyActor::BeginPlay()
{
    Super::BeginPlay();
    UE_LOG(LogTemp, Warning, TEXT("Actor started!"));
}
```

## When to Use
- ✅ AAA games with high-end graphics
- ✅ Complex game mechanics
- ❌ Not for simple mobile games (better use Unity)

## Step-by-Step Instructions
1. Install Unreal Engine via Epic Games Launcher
2. Create project (Blueprint or C++)
3. Use Blueprints for rapid prototyping
4. Write C++ for performance

## Dependencies
Install Unreal Engine via Epic Games Launcher

## Examples
Input: BeginPlay event → Output: Message in log

## Resources
- [Unreal Docs](https://docs.unrealengine.com/)
- [Examples](./examples/)

## Validation
1. Project compiles without errors
2. Blueprints work correctly
3. Game launches in Editor Mode
