---
name: ai-code-review
description: "Automated code review with AI agents"
category: ai
tags: [code-review, ai, automation, quality, security]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# AI Code Review

> Automate code reviews with AI agents that catch bugs, security issues, and style violations.

## Quick Start
```python
# ai_review.py — AI-powered code review script
import subprocess
import json
from anthropic import Anthropic

client = Anthropic()

def get_pr_diff():
    result = subprocess.run(
        ["git", "diff", "main...HEAD"],
        capture_output=True, text=True
    )
    return result.stdout

def review_code(diff: str) -> dict:
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        system="You are an expert code reviewer. Analyze diffs for:\n"
               "1. Security vulnerabilities (XSS, SQLI, CSRF, injection)\n"
               "2. Performance issues (N+1 queries, memory leaks)\n"
               "3. Logic bugs (off-by-one, race conditions)\n"
               "4. Type safety (missing null checks, any usage)\n"
               "5. Code quality (dead code, complexity, duplication)\n"
               "Rate each category: CRITICAL, WARNING, INFO",
        messages=[{
            "role": "user",
            "content": f"Review this diff:\n```diff\n{diff}\n```"
        }],
        max_tokens=2000
    )
    return response.content[0].text

if __name__ == "__main__":
    diff = get_pr_diff()
    if diff:
        print(review_code(diff))
```

## Key Concepts
AI code review complements (not replaces) human review. Best for catching common issues, suggesting improvements, and enforcing conventions. Integrate via CI pipeline or pre-commit hooks.

## When to Use
- CI pipeline gate before human review
- Pre-commit hooks for immediate feedback
- Large PRs where manual review is slow
- Security audits on every commit

## Validation
1. Review correctly identifies known issues in test diffs
2. False positive rate is acceptable (< 20%)
3. Review is actionable — each finding has a suggested fix
