---
name: django-rest
description: Создает REST API на Django с Django REST Framework. Используется для Python веб-приложений с мощной админкой.
category: backend
tags: [django, drf, rest, python, admin]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-01
---
# Django REST Framework

> REST API на Django с мощной админкой и ORM.

## 🚀 Quick Start
```python
# serializers.py
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

# views.py
from rest_framework import viewsets
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
```

## 📋 Когда использовать
- ✅ Сложные веб-приложения на Python
- ✅ Нужна встроенная админка
- ❌ Не использовать для микросервисов (лучше FastAPI)

## 🔧 Пошаговая инструкция
1. Установи: `pip install django djangorestframework`
2. Создай проект: `django-admin startproject myproject`
3. Добавь DRF и создай API views
4. Запусти: `python manage.py runserver`

## 📦 Зависимости
```bash
pip install django djangorestframework
```

## 🧪 Примеры
Input: `GET /api/users/` → Output: JSON список пользователей

## 🔗 Ресурсы
- [DRF Docs](https://www.django-rest-framework.org/)
- [Примеры кода](./examples/)

## ✅ Валидация
1. API отвечает корректно
2. Админка доступна по `/admin/`
3. ORM запросы работают без ошибок
