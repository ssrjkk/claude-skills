---
name: jupyter
description: Creates and manages Jupyter notebooks for data analysis, visualization, and reproducible research.
category: data
tags: [jupyter, notebooks, python, data-science, visualization]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Jupyter

> Interactive computing environment for data science and research.

## Quick Start
```bash
pip install jupyterlab
jupyter lab
```

## Magic Commands
```python
%matplotlib inline           # Show plots inline
%timeit df.groupby('col').sum()  # Time execution
%load_ext autoreload         # Auto-reload modules
%autoreload 2
%%bash                      # Run bash commands
echo "Hello from shell"
```

## When to Use
- Exploratory data analysis
- Reproducible research
- Data storytelling
- Model prototyping

## Validation
1. JupyterLab UI loads correctly
2. Kernels execute code successfully
3. Plots render inline
