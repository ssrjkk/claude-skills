---
name: agent-design
description: "Designs LLM agents with memory, tools, and reasoning cycle. Use for creating autonomous AI assistants."
category: ai
tags: [agent, llm, tools, memory, reasoning]
models: [opus]
version: 1.0.0
created: 2026-04-29
---
# Agent Design

> Design LLM agents with memory and tools.

## Quick Start
```python
from langchain_openai import ChatOpenAI
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.tools import tool
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

@tool
def search(query: str) -> str:
    """Search the web for information."""
    return f"Results for: {query}"

tools = [search]

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "{input}"),
    MessagesPlaceholder("agent_scratchpad"),
])

llm = ChatOpenAI(model="gpt-4o", temperature=0)
agent = create_tool_calling_agent(llm, tools, prompt)
executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
executor.invoke({"input": "Find information about Python"})
```

## When to Use
- ✅ Autonomous AI assistants
- ✅ Need reasoning and tool usage
- ❌ Not for simple Q&A tasks

## Step-by-Step Instructions
1. Define tools (search, calculator, API)
2. Setup system prompt with agent role
3. Add memory (buffer, summary)
4. Test reasoning cycle

## Dependencies
```bash
pip install langchain langchain-openai langchain-core
```

## Examples
Input: "What's the weather in Moscow?" → Output: Agent calls weather API, returns answer

## Resources
- [LangChain Agents](https://python.langchain.com/docs/modules/agents/)
- [Examples](./examples/)

## Validation
1. Agent selects correct tools
2. Memory preserves dialogue context
3. Reasoning chain is logical and complete
