---
name: pyqt
description: Creates desktop applications with PyQt6, Qt Widgets, signals/slots, and Qt Designer.
category: desktop
tags: [pyqt, qt, desktop, python, gui]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# PyQt6
> Python bindings for Qt desktop application framework.
## Quick Start
```python
import sys; from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
class MainWindow(QWidget):
    def __init__(self):
        super().__init__(); self.setWindowTitle("My App"); layout = QVBoxLayout()
        self.label = QLabel("Hello!"); button = QPushButton("Click Me"); button.clicked.connect(self.on_click)
        layout.addWidget(self.label); layout.addWidget(button); self.setLayout(layout)
    def on_click(self): self.label.setText("Clicked!")
app = QApplication(sys.argv); w = MainWindow(); w.show(); sys.exit(app.exec())
```
## When to Use
- Cross-platform desktop apps; Data analysis tools with GUI; Internal business apps
## Validation
1. Window displays all widgets; 2. Signals/slots work; 3. Layouts resize correctly
