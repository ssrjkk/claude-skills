# Claude Models Compatibility Matrix

| Model | Speed | Context | Best For |
|-------|-------|---------|----------|
| Haiku | Fast | 200K | Simple, repetitive tasks |
| Sonnet | Balanced | 200K | Most skills (34 domains, 6848 skills) |
| Opus | Powerful | 200K | Complex reasoning, architecture |

## Skills by Model

All 6848 skills across 38 domains work with **Sonnet** and **Opus**.  
Skills are organized under `.claude/skills/{domain}/{skill-name}/SKILL.md`.

### Domains covered
- ai (637 skills), ar-vr (80), backend (799), blockchain (147), communications (136)
- data (270), database (449), design (138), desktop (108), devops (653)
- ecommerce (102), education (68), embedded (88), energy (78), engineering (126)
- finance (96), frontend (633), gamedev (153), geospatial (96), healthcare (96)
- hr (112), iot (188), media (102), mobile (108), networking (168)
- os-admin (200), payments (88), product (150), qa (290), scientific (80)
- security (253), supply-chain (106), sustainability (48)
- Legacy: api-testing, ci-cd-setup, database-migration, test-reporting

### Opus (Best) — Complex skills
Skills requiring deep architectural reasoning:
- System design, architecture patterns
- Security and compliance (OWASP, GDPR, PCI DSS)
- Blockchain, smart contracts, DeFi protocols
- Game engine architecture (Unity, Unreal)
- Machine learning pipelines, LLM fine-tuning
- Distributed systems, consensus algorithms

## Recommendation
For most users: **Sonnet**. For complex architecture/security tasks: **Opus**. For simple tasks: **Haiku**.
