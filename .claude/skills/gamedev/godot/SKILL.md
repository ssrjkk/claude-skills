---
name: godot
description: Develops 2D/3D games on Godot Engine with GDScript. Use for lightweight cross-platform games.
category: gamedev
tags: [godot, gdscript, game-dev, 2d, 3d, open-source]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-01
---
# Godot

> Open-source game engine with GDScript for 2D/3D games.

## Quick Start
```gdscript
extends CharacterBody2D

@export var speed: float = 300.0

func _physics_process(delta):
    var direction = Input.get_vector("ui_left", "ui_right", "ui_up", "ui_down")
    velocity = direction * speed
    move_and_slide()
```

## When to Use
- ✅ Open engine without royalties
- ✅ 2D games (Godot excels at 2D)
- ❌ Not for AAA graphics

## Step-by-Step Instructions
1. Download Godot from https://godotengine.org/
2. Create scene (Node2D, Node3D)
3. Attach GDScript to node
4. Run scene

## Dependencies
Download Godot from https://godotengine.org/download

## Examples
Input: Key press → Output: Character moves on screen

## Resources
- [Godot Docs](https://docs.godotengine.org/)
- [Examples](./examples/)

## Validation
1. Scene loads without errors
2. GDScript executes correctly
3. Game works in exported form
