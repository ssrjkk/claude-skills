---
name: langgraph-multi-agent
description: Multi-agent systems with LangGraph
category: ai
tags: [langgraph, multi-agent, orchestration, coordination, python]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# LangGraph Multi-Agent

> Build coordinated multi-agent systems where specialized agents collaborate on complex tasks.

## Quick Start
```python
from typing import TypedDict, Literal
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolExecutor
from langchain_core.messages import HumanMessage, AIMessage

class TeamState(TypedDict):
    messages: list
    task: str
    plan: str
    code: str
    review: str

def planner_agent(state: TeamState) -> TeamState:
    """Creates implementation plan"""
    state["plan"] = f"Plan: Build a REST API with FastAPI"
    state["messages"].append(AIMessage(content=f"Plan created: {state['plan']}"))
    return state

def coder_agent(state: TeamState) -> TeamState:
    """Writes code based on plan"""
    state["code"] = 'from fastapi import FastAPI\napp = FastAPI()\n\n@app.get("/")\ndef root():\n    return {"hello": "world"}'
    state["messages"].append(AIMessage(content="Code written"))
    return state

def reviewer_agent(state: TeamState) -> TeamState:
    """Reviews code for issues"""
    state["review"] = "Code looks good. Consider adding error handling."
    state["messages"].append(AIMessage(content=f"Review: {state['review']}"))
    return state

def router(state: TeamState) -> Literal["planner", "coder", "reviewer", END]:
    last_msg = state["messages"][-1].content if state["messages"] else ""
    if "Plan" in last_msg and not state.get("code"):
        return "coder"
    elif state.get("code") and not state.get("review"):
        return "reviewer"
    elif state.get("review"):
        return END
    return "planner"

builder = StateGraph(TeamState)
for name in ["planner", "coder", "reviewer"]:
    builder.add_node(name, eval(f"{name}_agent"))
builder.set_conditional_edge("planner", router)
```

## Key Concepts
Each agent is a specialized node with its own LLM, tools, and responsibilities. Agents share a common state but only modify their domain. A supervisor agent or conditional router coordinates handoffs.

## When to Use
- Software development with specialized roles (planner, coder, reviewer, tester)
- Customer support triage with tiered agent escalation
- Research pipelines with separate search, analysis, and synthesis agents

## Validation
1. Each agent correctly handles its specialized role
2. Handoffs between agents preserve context
3. The full system completes complex tasks end-to-end
