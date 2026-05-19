---
name: blender
description: Creates 3D models, animations, and scenes in Blender using Python scripting and the bpy module.
category: gamedev
tags: [blender, 3d-modeling, animation, python, bpy]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Blender
> Open-source 3D creation suite with Python API.
## Quick Start
```python
import bpy
bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 0, 0))
mat = bpy.data.materials.new(name="Red")
mat.use_nodes = True; mat.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (1, 0, 0, 1)
bpy.context.object.data.materials.append(mat)
```
## Animation
```python
obj = bpy.context.object; obj.location = (0, 0, 0); obj.keyframe_insert(data_path="location", frame=1)
obj.location = (5, 0, 0); obj.keyframe_insert(data_path="location", frame=50)
```
## When to Use
- 3D asset creation for games; Procedural content generation; Automated modeling
## Validation
1. Scripts execute in Blender; 2. Mesh creation correct; 3. Keyframes animate
