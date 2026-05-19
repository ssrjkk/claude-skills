---
name: aspnet-core
description: Builds web APIs and applications with ASP.NET Core, controllers, Entity Framework, and middleware.
category: backend
tags: [aspnet, dotnet, csharp, web-api, entity-framework]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# ASP.NET Core
> Cross-platform framework for building modern web apps with .NET.
## Quick Start
```csharp
var builder = WebApplication.CreateBuilder(args); builder.Services.AddControllers();
var app = builder.Build(); app.MapControllers(); app.Run();
[ApiController, Route("api/[controller]")]
public class UsersController : ControllerBase {
    [HttpGet] public IActionResult GetUsers() => Ok(new[] { new { Id = 1, Name = "Alice" } });
}
```
## When to Use
- Enterprise .NET APIs; Microservices; Cross-platform C# applications
## Validation
1. Server starts; 2. Endpoints return correct data; 3. EF Core queries execute
