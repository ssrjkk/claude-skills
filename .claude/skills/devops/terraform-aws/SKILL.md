---
name: terraform-aws
description: Провизионит инфраструктуру в AWS с использованием Terraform модулей. Используется для IaC управления облачными ресурсами.
category: devops
tags: [terraform, aws, iac, infrastructure]
models: [sonnet, opus]
version: 1.0.0
created: 2026-04-29
---
# Terraform AWS

> Infrastructure as Code для AWS с модульным подходом.

## 🚀 Quick Start
```hcl
provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  
  tags = {
    Name = "WebServer"
  }
}
```

## 📋 Когда использовать
- ✅ Создание/управление AWS ресурсами
- ✅ Нужна версионируемая инфраструктура
- ❌ Не использовать для одноразовых локальных скриптов

## 🔧 Пошаговая инструкция
1. Установи Terraform и настрой AWS CLI
2. Создай `main.tf` с провайдером и ресурсами
3. Инициализируй: `terraform init`
4. Применяй: `terraform apply`

## 📦 Зависимости
```bash
# Установить Terraform
# https://developer.hashicorp.com/terraform/install

# Настроить AWS CLI
pip install awscli
aws configure
```

## 🧪 Примеры
Input: `terraform apply` в папке с конфигом
Output: EC2 инстанс создан в AWS

## 🔗 Ресурсы
- [Terraform AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
- [Примеры кода](./examples/)

## ✅ Валидация
1. Terraform план создается без ошибок
2. Ресурсы появляются в AWS Console
3. State файл корректно обновляется
