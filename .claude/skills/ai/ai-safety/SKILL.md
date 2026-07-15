---
name: ai-safety
description: "AI safety and responsible AI practices"
category: ai
tags: [ai-safety, responsible-ai, ethics, security, governance]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# AI Safety

> Implement responsible AI practices including guardrails, monitoring, and ethical guidelines.

## Quick Start
```python
from guardrails import Guard
from guardrails.validators import Validator

class NoPIIValidator(Validator):
    def validate(self, value: str, metadata: dict) -> dict:
        import re
        # Check for emails, SSNs, credit cards
        patterns = {
            "email": r'\b[\w.+-]+@[\w-]+\.[\w.]+\b',
            "ssn": r'\b\d{3}-\d{2}-\d{4}\b',
            "credit_card": r'\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b'
        }
        found = {name: re.findall(pat, value)
                 for name, pat in patterns.items()
                 if re.search(pat, value)}
        if found:
            return {"valid": False, "error": f"PII detected: {found}"}
        return {"valid": True}

# Content moderation guard
content_guard = Guard().use(NoPIIValidator())

# Usage
result = content_guard.validate("My email is user@example.com")
print(result.error)  # "PII detected: {'email': ['user@example.com']}"
```

## Key Concepts
AI safety spans: prompt injection prevention, PII/redaction, content moderation, output validation, rate limiting, audit logging, and bias monitoring. Defense in depth — multiple layers of protection.

## When to Use
- Any production LLM deployment
- Applications handling user data or PII
- Systems where AI outputs affect real-world decisions
- Regulated industries (healthcare, finance, legal)

## Validation
1. Prompt injection attempts are blocked or sanitized
2. PII is detected and redacted in both inputs and outputs
3. Audit logs capture all LLM interactions for review
4. Rate limits prevent abuse and cost overruns
