---
name: jenkins-pipeline
description: "Creates Jenkins pipeline scripts for CI/CD with declarative and scripted syntax support. Use for automation of builds and deployments."
category: devops
tags: [jenkins, pipeline, ci-cd, groovy, automation]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-01
---
# Jenkins Pipeline

> CI/CD automation with Jenkins Pipeline (Declarative/Groovy).

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

## 📋 When to Use
- ✅ CI/CD in corporate environment with Jenkins
- ✅ Complex pipelines with conditions and parallelism
- ❌ Not for simple projects (better use GitHub Actions)

## 🔧 Step-by-Step Instructions
1. Install Jenkins and necessary plugins
2. Create `Jenkinsfile` in project root
3. Configure pipeline in Jenkins UI
4. Run build

## 📦 Dependencies
Download Jenkins from https://www.jenkins.io/download/

## 🧪 Examples
Input: Pipeline run
Output: All stages pass successfully

## 🔗 Resources
- [Jenkins Docs](https://www.jenkins.io/doc/)
- [Examples](./examples/)

## ✅ Validation
1. Pipeline executes without errors
2. Stages execute in correct order
3. Artifacts saved correctly
