---
name: flask-python
description: "Creates lightweight web applications and REST APIs with Flask, Jinja2 templates, and SQLAlchemy. Use for simple Python web apps and microservices."
category: backend
tags: [python, flask, web, jinja, sqlalchemy]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Flask Python

> Lightweight Python web framework with Jinja2 templates.

## Quick Start
```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(debug=True)
```

## When to Use
- Simple web apps and APIs
- Prototyping and MVPs
- Small microservices
- Traditional server-rendered apps

## Step-by-Step
1. Install: `pip install flask`
2. Create `app.py` with routes
3. Use Jinja2 templates for HTML
4. Run: `python app.py`

## Dependencies
```bash
pip install flask flask-sqlalchemy jinja2
```

## Examples
```python
@app.route("/users/<int:id>")
def get_user(id):
    return jsonify({"id": id, "name": "Alice"})
```

## Resources
- [Flask Docs](https://flask.palletsprojects.com)

## Validation
1. Server starts on http://localhost:5000
2. `/api/health` returns 200
3. Templates render correctly
