# Infrastructure as Code

## Terraform

**What it is**  
Open-source IaC tool. 

**Why it matters**  
Cloud-agnostic, declarative. 

**Must know**  
HCL, providers, resources, state. 

**Must be able to do**  
Написать main.tf. Init, plan, apply. 

**Where it is used**  
Все облака. 

**Trade-offs**  
+Portable. -State management. 

**Common mistakes**  
State в git. 

**Interview check**  
Q: Terraform state? A: Хранит текущее состояние инфры, lock для командной работы. 

**Mini example**  
aws_instance: t2.micro, ami-12345.

## CloudFormation

**What it is**  
AWS native IaC. 

**Why it matters**  
Интегрировано с AWS, native. 

**Must know**  
YAML/JSON templates. Stacks, stack sets. 

**Must be able to do**  
Написать CFN template. 

**Where it is used**  
AWS-only. 

**Trade-offs**  
+AWS native. -AWS lock-in. 

**Common mistakes**  
Hand-edits ресурсов после CFN. 

**Interview check**  
Q: CloudFormation drift? A: Различие между template и реальными ресурсами. 

**Mini example**  
CloudFormation stack: VPC + EC2.

## State Management

**What it is**  
Хранение состояния инфры. 

**Why it matters**  
Terraform нуждается в state для tracking ресурсов. 

**Must know**  
Local state vs remote (S3 + DynamoDB lock). 

**Must be able to do**  
Настроить remote state в S3. 

**Where it is used**  
Terraform проекты. 

**Trade-offs**  
+Team работа. -Доп. инфра. 

**Common mistakes**  
Local state в команде. 

**Interview check**  
Q: Зачем remote state? A: Для командной работы, locking, backup. 

**Mini example**  
S3 bucket для state, DynamoDB table для lock.

## Modules

**What it is**  
Reusable Terraform код. 

**Why it matters**  
Don't repeat yourself. 

**Must know**  
Input variables, outputs. Module registry. 

**Must be able to do**  
Создать модуль VPC. 

**Where it is used**  
Большие инфры. 

**Trade-offs**  
+Reusable. -Абстракция. 

**Common mistakes**  
Over-abstraction. 

**Interview check**  
Q: Terraform module? A: Пакет ресурсов, можно переиспользовать. 

**Mini example**  
Module vpc: input CIDR, output VPC ID.