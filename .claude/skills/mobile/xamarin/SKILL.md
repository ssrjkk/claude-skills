---
name: xamarin
description: Builds native mobile apps with Xamarin and .NET MAUI, sharing C# code across iOS, Android, and Windows.
category: mobile
tags: [xamarin, dotnet, mobile, csharp, maui]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Xamarin / .NET MAUI
> Build native cross-platform apps with .NET and C#.
## Quick Start
```xml
<ContentPage xmlns="http://schemas.microsoft.com/dotnet/2021/maui" x:Class="MyApp.MainPage">
  <VerticalStackLayout Padding="30">
    <Label Text="Hello, MAUI!" FontSize="32" />
    <Button Text="Click Me" Clicked="OnButtonClicked" />
  </VerticalStackLayout>
</ContentPage>
```
```csharp
public partial class MainPage : ContentPage {
    int count = 0;
    private void OnButtonClicked(object sender, EventArgs e) => count++;
}
```
## When to Use
- .NET cross-platform mobile apps; Enterprise C# mobile; Code sharing
## Validation
1. App builds for all platforms; 2. UI renders correctly; 3. Platform-specific code works
