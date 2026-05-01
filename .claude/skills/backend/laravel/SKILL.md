---
name: laravel
description: Создает веб-приложения на Laravel с Eloquent ORM и Blade шаблонами. Используется для PHP веб-разработки.
category: backend
tags: [laravel, php, eloquent, blade, mvc]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-01
---
# Laravel

> PHP framework для веб-приложений с элегантным синтаксисом.

## 🚀 Quick Start
```php
// routes/web.php
Route::get('/users', function () {
    return User::all();
});

// app/Models/User.php
class User extends Model
{
    protected $fillable = ['name', 'email'];
}
```

## 📋 Когда использовать
- ✅ Веб-приложения на PHP
- ✅ Нужна встроенная аутентификация и Blade шаблоны
- ❌ Не использовать для микросервисов без рендеринга

## 🔧 Пошаговая инструкция
1. Установи Laravel: `composer create-project laravel/laravel myproject`
2. Настрой .env с параметрами БД
3. Создай модели и миграции
4. Запусти: `php artisan serve`

## 📦 Зависимости
```bash
composer create-project laravel/laravel myproject
```

## 🧪 Примеры
Input: `GET /users` → Output: JSON массив пользователей

## 🔗 Ресурсы
- [Laravel Docs](https://laravel.com/docs)
- [Примеры кода](./examples/)

## ✅ Валидация
1. Приложение запускается без ошибок
2. Eloquent модели работают корректно
3. Blade шаблоны рендерятся
