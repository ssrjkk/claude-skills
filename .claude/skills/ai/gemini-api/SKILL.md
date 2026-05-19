---
name: gemini-api
description: Integrates Google's Gemini API for text generation, vision, embeddings, and function calling.
category: ai
tags: [gemini, google, api, llm, multimodal]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Gemini API
> Google's multimodal AI model API with text, vision, and code capabilities.
## Quick Start
```python
import google.generativeai as genai
genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("Explain quantum computing")
print(response.text)
```
## Chat & Vision
```python
chat = model.start_chat(history=[]); response = chat.send_message("Tell me a joke")
import PIL.Image; model = genai.GenerativeModel('gemini-pro-vision')
image = PIL.Image.open('diagram.png'); response = model.generate_content(["Explain this", image])
```
## When to Use
- Multimodal analysis; Code generation; Embeddings; Google Cloud integration
## Validation
1. API key authenticates; 2. Text generation returns content; 3. Vision processes images
