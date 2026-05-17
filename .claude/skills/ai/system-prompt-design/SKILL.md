---
name: system-prompt-design
description: Designs effective system prompts for LLM agents, chatbots, and assistants with role definition, constraints, and behavioral guidelines. Use for production AI systems.
category: ai
tags: [prompt, system-prompt, agent, chatbot, persona]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# System Prompt Design

> Crafting system-level prompts for consistent agent behavior.

## Quick Start
```
You are a helpful coding assistant.
- Write clean, well-documented code
- Explain your reasoning briefly
- Provide working examples
- When unsure, say "I'm not sure"
- Never execute code without user approval
```

## When to Use
- Chatbot personality and tone
- Agent role and capability definition
- Safety and boundary constraints
- Multi-turn conversation consistency

## Components

### Role Definition
Who the AI is and what it does.

### Behavior Rules
Explicit do/don't guidelines.

### Output Format
Expected response structure.

### Constraints
Limitations and boundaries (time, scope, knowledge).

### Conversation Flow
How to handle greetings, follow-ups, clarifications.

## Dependencies
No additional libraries — pure prompt design.

## Examples
```
You are an expert SQL analyst.
- Write queries only, no explanations unless asked
- Use PostgreSQL syntax
- Add comments for complex JOINs
- If a query would be destructive, warn and ask for confirmation
- Reference table schemas when relevant
```

## Resources
- [Anthropic System Prompts](https://docs.anthropic.com/claude/docs/system-prompts)

## Validation
1. Agent follows rules consistently across sessions
2. Boundaries are respected (no prompt injection)
3. Response style matches defined persona
4. Multi-turn context is maintained correctly
