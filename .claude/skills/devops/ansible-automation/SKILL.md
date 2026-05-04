---
name: ansible-automation
description: Automates server configuration and deployment using Ansible playbooks. Use for configuration management.
category: devops
tags: [ansible, automation, configuration-management, devops]
models: [sonnet, opus]
version: 1.0.0
created: 2026-04-29
---
# Ansible Automation

> Declarative configuration management for servers.

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

## 📋 When to Use
- ✅ Configuring multiple servers
- ✅ Deploying applications to bare-metal or VPS
- ❌ Not for single local computer

## 🔧 Step-by-Step Instructions
1. Install Ansible: `pip install ansible`
2. Create inventory file with hosts
3. Write playbook.yml with tasks
4. Run: `ansible-playbook -i inventory playbook.yml`

## 📦 Dependencies
```bash
pip install ansible
```

## 🧪 Examples
Input: `ansible-playbook -i hosts site.yml`
Output: Nginx installed and started on all webservers

## 🔗 Resources
- [Ansible Docs](https://docs.ansible.com/)
- [Examples](./examples/)

## ✅ Validation
1. Playbook runs without errors
2. Services running on target hosts
3. Idempotency maintained (re-run doesn't change state)
