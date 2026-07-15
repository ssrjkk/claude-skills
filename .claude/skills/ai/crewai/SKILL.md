---
name: crewai
description: "Orchestrates AI agent teams with CrewAI, role-based agents, tasks, and sequential/parallel workflows."
category: ai
tags: [crewai, agents, orchestration, tasks, ai]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# CrewAI
> Framework for orchestrating role-based AI agent teams.
## Quick Start
```python
from crewai import Agent, Task, Crew, Process
researcher = Agent(role='Researcher', goal='Find accurate information', backstory='Expert researcher')
writer = Agent(role='Writer', goal='Write engaging content', backstory='Professional writer')
research = Task(description='Research AI trends', agent=researcher, expected_output='Notes')
write = Task(description='Write blog post about AI', agent=writer, expected_output='Blog post')
crew = Crew(agents=[researcher, writer], tasks=[research, write], process=Process.sequential)
result = crew.kickoff()
```
## When to Use
- Content creation pipelines; Research workflows; Automated report generation
## Validation
1. Agents assigned correct roles; 2. Tasks execute in order; 3. Final output is cohesive
