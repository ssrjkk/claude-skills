---
name: autogen
description: Creates multi-agent AI systems with AutoGen, enabling agent conversations, tool use, and group chats.
category: ai
tags: [autogen, agents, multi-agent, conversation, ai]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# AutoGen
> Multi-agent conversation framework for building AI agent systems.
## Quick Start
```python
import autogen
config_list = [{"model": "gpt-4", "api_key": "..."}]
assistant = autogen.AssistantAgent(name="assistant", llm_config={"config_list": config_list})
user_proxy = autogen.UserProxyAgent(name="user", human_input_mode="NEVER")
user_proxy.initiate_chat(assistant, message="Write a Python script to fetch stock prices")
```
## Group Chat
```python
group_chat = autogen.GroupChat(agents=[agent1, agent2, agent3], messages=[], max_round=10)
manager = autogen.GroupChatManager(groupchat=group_chat, llm_config={...})
```
## When to Use
- Multi-agent problem-solving; Code generation; Research assistance
## Validation
1. Agents initiate conversations; 2. Tools discovered and called; 3. Group chat reaches consensus
