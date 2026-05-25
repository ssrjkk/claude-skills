---
name: langgraph-agents
description: Building agents with LangGraph
category: ai
tags: [langgraph, agents, python, llm, graph]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# LangGraph Agents

> Build stateful, multi-step AI agents using LangGraph's graph-based execution model.

## Quick Start
```python
from typing import TypedDict, Literal
from langgraph.graph import StateGraph, END
from langchain_core.messages import HumanMessage
from langchain_anthropic import ChatAnthropic

class AgentState(TypedDict):
    messages: list
    next_step: str

llm = ChatAnthropic(model="claude-sonnet-4-20250514")

def call_model(state: AgentState) -> AgentState:
    response = llm.invoke(state["messages"])
    state["messages"].append(response)
    return state

def should_continue(state: AgentState) -> Literal["tools", "end"]:
    if state["messages"][-1].tool_calls:
        return "tools"
    return "end"

builder = StateGraph(AgentState)
builder.add_node("agent", call_model)
builder.set_entry_point("agent")
builder.add_conditional_edges("agent", should_continue, {
    "tools": "agent",
    "end": END
})

graph = builder.compile()
result = graph.invoke({"messages": [HumanMessage("What is the weather in Tokyo?")]})
```

## Key Concepts
Agents are state machines where nodes are LLM calls, tools, or logic. Edges define control flow. The state is a typed dictionary that persists across steps. Conditional edges enable tool-calling loops.

## When to Use
- Building conversational agents that need tool access
- Creating multi-step reasoning pipelines
- Implementing agentic RAG and research assistants

## Validation
1. Graph compiles without errors
2. Agent correctly routes between LLM and tools
3. State is properly maintained across multiple turns
