---
name: godot
description: Разрабатывает 2D/3D игры на Godot Engine с GDScript. Используется для легковесных кроссплатформенных игр.
category: gamedev
tags: [godot, gdscript, game-dev, 2d, 3d, open-source]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-01
---
# Godot

> Открытый игровой движок с GDScript для 2D/3D игр.

## 🚀 Quick Start
```gdscript
extends CharacterBody2D

@export var speed: float = 300.0

func _physics_process(delta):
    var direction = Input.get_vector("ui_left", "ui_right", "ui_up", "ui_down")
    velocity = direction * speed
    move_and_slide()
```

## 📋 Когда использовать
- ✅ Открытый движок без роялти
- ✅ 2D игры (Godot особенно силен в 2D)
- ❌ Не использовать для AAA графики

## 🔧 Пошаговая инструкция
1. Скачай Godot с https://godotengine.org/
2. Создай сцену (Node2D, Node3D)
3. Прикрепи GDScript скрипт к ноде
4. Запусти сцену

## 📦 Зависимости
Скачай Godot с https://godotengine.org/download

## 🧪 Примеры
Input: Нажатие клавиш → Output: Персонаж движется по экрану

## 🔗 Ресурсы
- [Godot Docs](https://docs.godotengine.org/)
- [Примеры кода](./examples/)

## ✅ Валидация
1. Сцена загружается без ошибок
2. GDScript выполняется корректно
3. Игра работает в экспортированном виде
