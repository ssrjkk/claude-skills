---
name: unity
description: Develops games on Unity using C# scripts and component architecture. Use for 2D/3D games across multiple platforms.
category: gamedev
tags: [unity, csharp, game-dev, 2d, 3d]
models: [opus]
version: 1.0.0
created: 2026-05-01
---
# Unity

> Cross-platform game development with Unity and C#.

## Quick Start
```csharp
using UnityEngine;

public class PlayerController : MonoBehaviour
{
    public float speed = 10.0f;
    
    void Update()
    {
        float move = Input.GetAxis("Vertical") * speed * Time.deltaTime;
        transform.Translate(0, 0, move);
    }
}
```

## When to Use
- ✅ Developing 2D/3D games
- ✅ Cross-platform deploy (PC, Mobile, Console)
- ❌ Not for non-graphics applications

## Step-by-Step Instructions
1. Install Unity Hub and select Unity version
2. Create project (2D/3D Template)
3. Write C# scripts in `Assets/Scripts/`
4. Test in Play Mode

## Dependencies
Install Unity Hub from https://unity.com/download

## Examples
Input: Press W key → Output: Character moves forward

## Resources
- [Unity Docs](https://docs.unity3d.com/)
- [Examples](./examples/)

## Validation
1. Scene starts without errors
2. Scripts compile successfully
3. Game mechanics work correctly
