---
name: flutter-clean-arch
description: Создает Flutter приложения с Clean Architecture и разделением на слои. Используется для масштабируемых мобильных приложений.
category: mobile
tags: [flutter, clean-arch, mobile, dart]
models: [opus]
version: 1.0.0
created: 2026-04-29
---
# Flutter Clean Architecture

> Структура Flutter приложения с соблюдением принципов Clean Architecture.

## 🚀 Quick Start
```dart
// domain/entities/user.dart
class User {
    final String id;
    final String name;
    User(this.id, this.name);
}

// presentation/pages/user_page.dart
class UserPage extends StatelessWidget {
    @override
    Widget build(BuildContext context) {
        return Scaffold(body: Center(child: Text('User Page')));
    }
}
```

## 📋 Когда использовать
- ✅ Масштабируемые Flutter приложения
- ✅ Нужно четкое разделение слоев (domain, data, presentation)
- ❌ Не использовать для простых прототипов или демо

## 🔧 Пошаговая инструкция
1. Создай Flutter проект: `flutter create my_app`
2. Организуй папки: `domain/`, `data/`, `presentation/`
3. Определи сущности и use cases
4. Запусти: `flutter run`

## 📦 Зависимости
```bash
flutter create my_app
```

## 🧪 Примеры
Input: Навигация на UserPage → отображается страница пользователя

## 🔗 Ресурсы
- [Flutter Docs](https://flutter.dev/docs)
- [Примеры кода](./examples/)

## ✅ Валидация
1. Проект собирается без ошибок
2. Слои изолированы корректно
3. Навигация работает между страницами
