name: "📖 New Skill"
description: Add a new skill to the library
labels: ["contribution"]
body:
  - type: markdown
    attributes:
      value: |
        Thanks for contributing! Before submitting, please:
        - [ ] Check the skill doesn't exist: `claude-skills search <name>`
        - [ ] Run `make test` locally
        - [ ] Run `ruff check src/`

  - type: input
    id: name
    attributes:
      label: "Skill name"
      placeholder: "kebab-case-name"
    validations:
      required: true

  - type: dropdown
    id: domain
    attributes:
      label: "Domain"
      options:
        - ai, ar-vr, backend, block, blockchain, cloud, communications
        - data, database, design, desktop, devops, ecommerce, education
        - embedded, energy, engineering, finance, frontend, gamedev
        - geospatial, healthcare, hr, iot, media, mobile, networking
        - os-admin, payments, product, qa, scientific, security
        - supply-chain, sustainability
    validations:
      required: true

  - type: checkboxes
    id: checklist
    attributes:
      label: "PR Checklist"
      options:
        - label: "SKILL.md has all required frontmatter"
          required: true
        - label: "SKILL.ru.md is a real translation (not auto-generated)"
        - label: "Code examples compile and run"
          required: true
        - label: "`make validate` passes"
          required: true
        - label: "`make test` passes"
          required: true
