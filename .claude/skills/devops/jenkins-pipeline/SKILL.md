---
name: jenkins-pipeline
description: Создает Jenkins pipeline скрипты для CI/CD с поддержкой declarative и scripted синтаксиса. Используется для автоматизации сборки и деплоя.
category: devops
tags: [jenkins, pipeline, ci-cd, groovy, automation]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-01
---
# Jenkins Pipeline

> CI/CD автоматизация с Jenkins Pipeline (Declarative/Groovy).

## 🚀 Quick Start
```groovy
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'npm install'
            }
        }
        stage('Test') {
            steps {
                sh 'npm test'
            }
        }
    }
}
```

## 📋 Когда использовать
- ✅ CI/CD в корпоративной среде с Jenkins
- ✅ Сложные пайплайны с условиями и параллелизмом
- ❌ Не использовать для простых проектов (лучше GitHub Actions)

## 🔧 Пошаговая инструкция
1. Установи Jenkins и необходимые плагины
2. Создай `Jenkinsfile` в корне проекта
3. Настрой pipeline в Jenkins UI
4. Запусти сборку

## 📦 Зависимости
Скачай Jenkins с https://www.jenkins.io/download/

## 🧪 Примеры
Input: Запуск пайплайна → Output: Все стадии проходят успешно

## 🔗 Ресурсы
- [Jenkins Docs](https://www.jenkins.io/doc/)
- [Примеры кода](./examples/)

## ✅ Валидация
1. Pipeline выполняется без ошибок
2. Стадии выполняются в правильном порядке
3. Артефакты сохраняются корректно
