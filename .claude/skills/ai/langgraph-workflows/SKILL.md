---
name: langgraph-workflows
description: LangGraph workflow orchestration
category: ai
tags: [langgraph, workflows, orchestration, pipeline, python]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# LangGraph Workflows

> Orchestrate complex multi-step AI workflows with LangGraph's graph execution engine.

## Quick Start
```python
from typing import TypedDict, Optional
from langgraph.graph import StateGraph, END
import asyncio

class WorkflowState(TypedDict):
    input_text: str
    summary: Optional[str]
    entities: Optional[list]
    sentiment: Optional[str]
    report: Optional[str]

def extract_entities(state: WorkflowState) -> WorkflowState:
    # Simulated entity extraction
    state["entities"] = ["AI", "machine learning", "automation"]
    return state

def analyze_sentiment(state: WorkflowState) -> WorkflowState:
    # Simulated sentiment analysis
    state["sentiment"] = "positive"
    return state

def summarize(state: WorkflowState) -> WorkflowState:
    state["summary"] = f"Summary of: {state['input_text'][:50]}..."
    return state

def generate_report(state: WorkflowState) -> WorkflowState:
    state["report"] = f"""
## Report
- Summary: {state['summary']}
- Entities: {', '.join(state['entities'])}
- Sentiment: {state['sentiment']}
"""
    return state

# Parallel branches then join
builder = StateGraph(WorkflowState)
builder.add_node("summarize", summarize)
builder.add_node("extract_entities", extract_entities)
builder.add_node("analyze_sentiment", analyze_sentiment)
builder.add_node("generate_report", generate_report)

builder.set_entry_point("summarize")
builder.set_conditional_edge("summarize", lambda s: ["extract_entities", "analyze_sentiment"])
builder.add_edge(["extract_entities", "analyze_sentiment"], "generate_report")
builder.add_edge("generate_report", END)
```

## Key Concepts
LangGraph supports parallel fan-out, conditional branching, and state sharing across nodes. Each node is a pure function that reads and updates state. The graph scheduler handles execution order and concurrency.

## When to Use
- Multi-stage document processing pipelines
- Data enrichment workflows that fan out to parallel processors
- Complex decision trees with conditional routing

## Validation
1. Graph runs all nodes in correct order
2. Parallel nodes execute concurrently and results merge
3. Conditional routing reaches the expected paths
