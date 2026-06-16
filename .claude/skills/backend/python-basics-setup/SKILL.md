---
name: python-basics-setup
description: Master Python fundamentals — installation, environment setup, basic syntax, and first programs
category: backend
tags: [python, programming, fundamentals, beginner, setup]
models: [sonnet, opus]
version: "1.1"
language: en
---

# SD-LANG-001: Python Basics and Setup

**Category:** Software Development > Programming Languages
**Difficulty:** Beginner
**Time to Master:** 2-3 hours
**Prerequisites:** None

## Overview

Mastering Python fundamentals is essential for any developer. This skill covers installation, environment setup, basic syntax, and your first Python program. By the end, you'll understand Python's philosophy and be ready to write simple scripts.

## Learning Objectives

- Install Python and configure your development environment
- Understand Python's design philosophy and core concepts
- Write and execute your first Python program
- Understand the Python interpreter and interactive shell
- Know how to manage Python packages and virtual environments
- Set up a professional Python development environment

## Step-by-Step Instructions

### Step 1: Install Python

1. Visit python.org and download the latest Python release
2. Run the installer:
   - **Windows**: Click installer, check "Add Python to PATH"
   - **macOS**: Use `brew install python3` or download from python.org
   - **Linux**: Use `sudo apt-get install python3` (Ubuntu/Debian)
3. Verify installation: Open terminal and run `python --version`
4. You should see Python 3.x installed

### Step 2: Understand the Python Interpreter

1. Open terminal/command prompt
2. Type `python` or `python3` to enter interactive mode
3. You'll see `>>>`  prompt
4. Try simple commands:
   ```python
   >>> print("Hello, Python!")
   >>> 5 + 3
   >>> name = "Claude"
   >>> print(name)
   ```
5. Exit with `exit()` or `Ctrl+D`

### Step 3: Create Your First Script

1. Create a file named `hello.py`
2. Add this content:
   ```python
   print("Hello, Python!")
   name = "Developer"
   print(f"Welcome, {name}!")
   ```
3. Save the file
4. Run it: `python hello.py`
5. You should see output in your terminal

### Step 4: Set Up Virtual Environments

1. Create project directory: `mkdir my_python_project`
2. Navigate into it: `cd my_python_project`
3. Create virtual environment: `python -m venv venv`
4. Activate it:
   - **Windows**: `venv\Scripts\activate`
   - **macOS/Linux**: `source venv/bin/activate`
5. Your prompt should show `(venv)` prefix
6. Deactivate with: `deactivate`

### Step 5: Manage Dependencies

1. Create `requirements.txt` file
2. Add packages you need:
   ```
   requests==2.28.0
   numpy==1.23.0
   ```
3. Install them: `pip install -r requirements.txt`
4. Check installed packages: `pip list`
5. Freeze current environment: `pip freeze > requirements.txt`

### Step 6: Configure Your IDE

**VS Code Setup:**
1. Install Python extension by Microsoft
2. Select Python interpreter: Ctrl+Shift+P > Python: Select Interpreter
3. Choose your virtual environment
4. Install linting: `pip install pylint`
5. Install formatting: `pip install black`

## Code Examples

### Basic Script

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
My First Python Program
Demonstrates basic Python concepts
"""

def greet(name):
    """Simple greeting function"""
    return f"Hello, {name}!"


if __name__ == "__main__":
    user_name = input("What is your name? ")
    message = greet(user_name)
    print(message)
```

### Virtual Environment Setup Script

```bash
#!/bin/bash
# setup_env.sh - Automated environment setup

echo "Creating Python virtual environment..."
python3 -m venv venv

echo "Activating virtual environment..."
source venv/bin/activate

echo "Upgrading pip..."
pip install --upgrade pip

echo "Installing requirements..."
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
fi

echo "Setup complete! Virtual environment is active."
```

### Package Management Example

```python
# install_packages.py
import subprocess
import sys

required_packages = [
    'requests',
    'numpy',
    'pandas'
]

for package in required_packages:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

print("All packages installed successfully!")
```

## Common Pitfalls

- **Python 2 vs 3**: Always use Python 3. Python 2 is deprecated.
- **PATH issues**: If `python` command not found, use `python3` explicitly
- **Virtual environment confusion**: Always activate venv before installing packages
- **Package conflicts**: Use virtual environments to isolate project dependencies
- **Encoding issues**: Include UTF-8 declaration at top of files with special characters
- **Long import times**: First import is slower; subsequent imports are cached

## Advanced Tips

1. **Use .gitignore**: Add `venv/` to avoid tracking virtual environment
   ```
   venv/
   __pycache__/
   *.pyc
   .env
   ```

2. **Poetry Alternative**: Consider using Poetry for modern dependency management
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

3. **Python Version Management**: Use pyenv to manage multiple Python versions
   ```bash
   brew install pyenv
   pyenv install 3.11.0
   ```

4. **IDE Debugger**: Set breakpoints in VS Code for interactive debugging

5. **Type Hints**: Start using type hints from the beginning
   ```python
   def add(a: int, b: int) -> int:
       return a + b
   ```

## Related Skills

- [SD-LANG-002: Python Data Types and Variables](./PYTHON_DATA_TYPES.md)
- [SD-LANG-003: Python Control Flow](./PYTHON_CONTROL_FLOW.md)
- [PT-IDE-001: VS Code Setup](../productivity-tools/VS_CODE_SETUP.md)
- [PT-AUTO-001: Bash Scripting](../productivity-tools/BASH_SCRIPTING.md)

## Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [Real Python Tutorials](https://realpython.com/)
- [Python Enhancement Proposals (PEPs)](https://www.python.org/dev/peps/)
