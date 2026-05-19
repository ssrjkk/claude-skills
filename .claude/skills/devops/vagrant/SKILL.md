---
name: vagrant
description: Creates and manages portable development environments with Vagrant, VirtualBox, and provisioners.
category: devops
tags: [vagrant, virtualbox, dev-environment, provisioning, vm]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Vagrant
> Reproducible development environments as code.
## Quick Start
```ruby
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/jammy64"
  config.vm.network "forwarded_port", guest: 80, host: 8080
  config.vm.provision "shell", inline: "apt-get update && apt-get install -y nginx"
end
```
```bash
vagrant up && vagrant ssh
```
## Multi-Machine
```ruby
config.vm.define "web" do |web| web.vm.network "private_network", ip: "192.168.33.10" end
config.vm.define "db" do |db| db.vm.network "private_network", ip: "192.168.33.11" end
```
## When to Use
- Team dev environments; Cross-platform testing; Reproducible demos
## Validation
1. vagrant up creates VM; 2. Port forwarding works; 3. Provisioning executes
