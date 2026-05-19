---
name: packer
description: Creates identical machine images for multiple platforms with Packer, including AWS AMIs and Docker images.
category: devops
tags: [packer, images, ami, iac, immutable]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Packer
> Build automated machine images for multiple platforms.
## Quick Start
```hcl
source "amazon-ebs" "ubuntu" {
  ami_name = "my-app-{{timestamp}}"; instance_type = "t2.micro"; region = "us-east-1"
  source_ami_filter { filters = { virtualization-type = "hvm", name = "ubuntu/images/*ubuntu-jammy-*" }; owners = ["099720109477"] }
  ssh_username = "ubuntu"
}
build { sources = ["source.amazon-ebs.ubuntu"]; provisioner "shell" { inline = ["sudo apt-get update", "sudo apt-get install -y nginx"] } }
```
## When to Use
- Golden AMI pipelines; Immutable infrastructure; CI/CD image building
## Validation
1. packer validate passes; 2. Image builds successfully; 3. Provisioner executes
