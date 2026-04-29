---
name: ansible-automation
description: Автоматизирует настройку серверов и деплой с использованием Ansible playbooks. Используется для конфигурации инфраструктуры как кода.
category: devops
tags: [ansible, automation, configuration-management, devops]
models: [sonnet, opus]
version: 1.0.0
created: 2026-04-29
---
# Ansible Automation

> Управление конфигурацией серверов через декларативные playbooks.

## 🚀 Quick Start
```yaml
---
- name: Install and start Nginx
  hosts: webservers
  become: yes
  
  tasks:
    - name: Install Nginx
      apt:
        name: nginx
        state: present
    
    - name: Start Nginx
      service:
        name: nginx
        state: started
```

## 📋 Когда использовать
- ✅ Настройка множества серверов
- ✅ Деплой приложений на bare-metal или VPS
- ❌ Не использовать для одного локального компьютера

## 🔧 Пошаговая инструкция
1. Установи Ansible: `pip install ansible`
2. Создай inventory файл с хостами
3. Напиши playbook.yml с задачами
4. Запусти: `ansible-playbook -i inventory playbook.yml`

## 📦 Зависимости
```bash
pip install ansible
```

## 🧪 Примеры
Input: `ansible-playbook -i hosts site.yml`
Output: Nginx установлен и запущен на всех серверах из группы webservers

## 🔗 Ресурсы
- [Ansible Docs](https://docs.ansible.com/)
- [Примеры кода](./examples/)

## ✅ Валидация
1. Playbook выполняется без ошибок
2. Сервисы запущены на целевых хостах
3. Idempotency соблюдена (повторный запуск не меняет состояние)
