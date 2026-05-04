---
name: terraform-aws
description: Provisions infrastructure in AWS using Terraform modules. Use for IaC management of cloud resources.
category: devops
tags: [terraform, aws, iac, infrastructure]
models: [sonnet, opus]
version: 1.0.0
created: 2026-04-29
---
# Terraform AWS

> Infrastructure as Code for AWS with modular approach.

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

## 📋 When to Use
- ✅ Creating/managing AWS resources
- ✅ Need version-controlled infrastructure
- ❌ Not for one-off local scripts

## 🔧 Step-by-Step Instructions
1. Install Terraform and configure AWS CLI
2. Create `main.tf` with provider and resources
3. Initialize: `terraform init`
4. Apply: `terraform apply`

## 📦 Dependencies
```bash
# Install Terraform
# https://developer.hashicorp.com/terraform/install

# Configure AWS CLI
pip install awscli
aws configure
```

## 🧪 Examples
Input: `terraform apply` in folder with config
Output: EC2 instance created in AWS

## 🔗 Resources
- [Terraform AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
- [Examples](./examples/)

## ✅ Validation
1. Terraform plan creates without errors
2. Resources appear in AWS Console
3. State file updates correctly
