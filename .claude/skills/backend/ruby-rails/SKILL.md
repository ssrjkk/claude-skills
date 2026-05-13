---
name: ruby-rails
description: Creates Ruby on Rails applications with ActiveRecord, MVC pattern, and RESTful routes. Use for rapid web application development.
category: backend
tags: [ruby, rails, active-record, mvc, backend]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Ruby on Rails

> Rapid web application development with Rails conventions.

## Quick Start
```bash
rails new myapp --api -d postgresql
cd myapp
rails generate scaffold Post title:string body:text
rails db:migrate
rails server
```

## When to Use
- ✅ Rapid prototyping and MVPs
- ✅ Full-stack web applications
- ❌ Not for real-time/high-throughput systems

## Step-by-Step Instructions
1. Install Rails: `gem install rails`
2. Create project: `rails new app --api`
3. Generate models/controllers: `rails generate scaffold User name email`
4. Run: `rails server`

## Dependencies
```bash
gem install rails
# or follow https://guides.rubyonrails.org/getting_started.html
```

## Examples
Input: `rails generate scaffold Product name price:decimal` → Output: Full CRUD with views

## Resources
- [Ruby on Rails Guides](https://guides.rubyonrails.org/)
- [Examples](./examples/)

## Validation
1. Server starts: `rails s`
2. Routes work: `rails routes`
3. Migrations run without errors
