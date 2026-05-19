---
name: procedural-gen
description: Generates game content algorithmically with procedural generation techniques for terrains, dungeons, and textures.
category: gamedev
tags: [procedural-generation, gamedev, terrain, algorithms, content]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Procedural Generation
> Algorithmic content creation for games.
## Quick Start (Terrain)
```python
import noise, numpy as np
def generate_heightmap(width, height, scale=10.0, octaves=6):
    terrain = np.zeros((width, height))
    for x in range(width):
        for z in range(height):
            terrain[x][z] = noise.pnoise2(x/scale, z/scale, octaves=octaves, repeatx=1024, repeaty=1024, base=42)
    return terrain
```
## Dungeon Generation (BSP)
```python
def generate_dungeon(width, height, min_room=5):
    grid = [[1] * width for _ in range(height)]
    rooms = []
    def split(x, y, w, h, depth=0):
        if depth > 3 or (w < min_room*2 and h < min_room*2):
            rw, rh = random.randint(min_room, w-2), random.randint(min_room, h-2)
            rx, ry = x + random.randint(1, w-rw-1), y + random.randint(1, h-rh-1)
            for ry in range(ry, ry+rh):
                for rx in range(rx, rx+rw): grid[ry][rx] = 0
            return
        split_h = random.choice([True, False])
        if split_h: split(x, y, w, h//2, depth+1); split(x, y+h//2, w, h-h//2, depth+1)
    split(0, 0, width, height); return grid, rooms
```
## When to Use
- Infinite worlds; Roguelike dungeons; Texture/terrain creation; Level design
## Validation
1. Generated content playable; 2. Parameters produce varied output; 3. Performance acceptable
