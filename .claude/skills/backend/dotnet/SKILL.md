---
name: dotnet
description: Builds ASP.NET Core Web APIs and microservices with C# and Entity Framework. Use for enterprise-grade .NET applications.
category: backend
tags: [dotnet, csharp, aspnet, entity-framework, backend]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# ASP.NET Core

> Build robust Web APIs and microservices with ASP.NET Core and C#.

## Quick Start
```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services.AddControllers();
builder.Services.AddDbContext<AppDbContext>(options =>
    options.UseSqlServer(builder.Configuration.GetConnectionString("Default")));

var app = builder.Build();
app.MapControllers();
app.Run();
```

## When to Use
- ✅ Enterprise-grade REST APIs
- ✅ Microservices architecture
- ❌ Not for small scripts (better Node.js/Python)

## Step-by-Step Instructions
1. Install SDK: `dotnet new webapi -n MyApi`
2. Add Entity Framework: `dotnet add package Microsoft.EntityFrameworkCore.SqlServer`
3. Create models and DbContext
4. Run: `dotnet run`

## Dependencies
```bash
# Install .NET SDK
# https://dotnet.microsoft.com/download
```

## Examples
Input: `dotnet new webapi -n ShopApi` → Output: ASP.NET Core project with controllers

## Resources
- [ASP.NET Core Docs](https://learn.microsoft.com/en-us/aspnet/core/)
- [Examples](./examples/)

## Validation
1. Project builds: `dotnet build`
2. API responds on expected port
3. EF migrations work correctly
