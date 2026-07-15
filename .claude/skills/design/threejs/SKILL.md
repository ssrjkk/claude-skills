---
name: threejs
description: "Creates 3D graphics on the web with Three.js, including scenes, cameras, animations, and WebGL."
category: design
tags: [threejs, 3d, webgl, graphics, animation]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Three.js
> 3D JavaScript library for the web with WebGL.
## Quick Start
```javascript
import * as THREE from 'three'
const scene = new THREE.Scene(); const camera = new THREE.PerspectiveCamera(75, innerWidth/innerHeight, 0.1, 1000)
const renderer = new THREE.WebGLRenderer(); renderer.setSize(innerWidth, innerHeight); document.body.appendChild(renderer.domElement)
const cube = new THREE.Mesh(new THREE.BoxGeometry(1,1,1), new THREE.MeshStandardMaterial({ color: 0x00ff00 }))
scene.add(cube); camera.position.z = 5
function animate() { requestAnimationFrame(animate); cube.rotation.x += 0.01; renderer.render(scene, camera) }
animate()
```
## When to Use
- 3D product viewers; Interactive visualizations; Game-like web experiences
## Validation
1. Scene renders without WebGL errors; 2. Animations run at 60fps; 3. Lighting affects materials
