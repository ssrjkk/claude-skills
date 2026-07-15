---
name: laravel
description: "Creates web applications on Laravel with Eloquent ORM and Blade templates. Use for PHP web development."
category: backend
tags: [laravel, php, eloquent, blade, mvc]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-01
---
# Laravel

> PHP framework for web applications with elegant syntax.

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

## 📋 When to Use
- ✅ Web applications on PHP
- ✅ Need built-in authentication and Blade templates
- ❌ Not for microservices without rendering

## 🔧 Step-by-Step Instructions
1. Install Laravel: `composer create-project laravel/laravel myproject`
2. Configure .env with DB parameters
3. Create models and migrations
4. Run: `php artisan serve`

## 📦 Dependencies
```bash
composer create-project laravel/laravel myproject
```

## 🧪 Examples
Input: `GET /users` 
Output: JSON array of users

## 🔗 Resources
- [Laravel Docs](https://laravel.com/docs)
- [Examples](./examples/)

## ✅ Validation
1. Application starts without errors
2. Eloquent models work correctly
3. Blade templates render properly
