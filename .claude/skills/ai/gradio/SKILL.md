---
name: gradio
description: "Creates ML demo interfaces with Gradio, supporting images, text, audio, and video inputs/outputs."
category: ai
tags: [gradio, python, ml, demo, interactive]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Gradio
> Build demo web apps for machine learning models.
## Quick Start
```python
import gradio as gr
def greet(name, intensity): return "Hello " + name + "!" * intensity
demo = gr.Interface(fn=greet, inputs=[gr.Textbox(label="Name"), gr.Slider(1, 5, value=2)], outputs=gr.Textbox())
demo.launch()
```
## Blocks Layout
```python
with gr.Blocks() as demo:
    gr.Markdown("# My App")
    with gr.Row():
        with gr.Column(): input_img = gr.Image(); btn = gr.Button("Process")
        with gr.Column(): output_img = gr.Image()
    btn.click(fn=process, inputs=input_img, outputs=output_img)
```
## When to Use
- ML model demos; Team sharing; User testing; API prototyping
## Validation
1. Interface launches on shareable URL; 2. Input types work; 3. Function returns expected output
