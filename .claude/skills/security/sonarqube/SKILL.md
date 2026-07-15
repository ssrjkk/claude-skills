---
name: sonarqube
description: "Analyzes code quality and security with SonarQube, detecting bugs, vulnerabilities, and code smells. Use for continuous code inspection."
category: security
tags: [sonarqube, code-quality, static-analysis, security, linting]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# SonarQube

> Continuous code quality and security inspection platform.

## Quick Start
```bash
docker run -d --name sonarqube -p 9000:9000 sonarqube:community
```

## When to Use
- Code quality gate in CI/CD
- Security vulnerability detection
- Technical debt tracking
- Code review automation

## Step-by-Step
1. Start SonarQube server
2. Generate project token
3. Configure scanner in CI/CD
4. Run: `sonar-scanner`

## Dependencies
```bash
# Using Docker
docker run -d -p 9000:9000 sonarqube:community

# Scanner
sonar-scanner -Dsonar.projectKey=myapp -Dsonar.token=sq...
```

## Examples
```yaml
# .github/workflows/sonarqube.yml
- name: SonarQube Scan
  uses: SonarSource/sonarqube-scan-action@v2
  env:
    SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
```

## Resources
- [SonarQube Docs](https://docs.sonarqube.org)

## Validation
1. SonarQube UI loads on port 9000
2. Analysis completes without errors
3. Quality gate passes
