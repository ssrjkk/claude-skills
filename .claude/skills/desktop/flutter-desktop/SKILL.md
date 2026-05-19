---
name: flutter-desktop
description: Builds desktop applications with Flutter for Windows, macOS, and Linux from a single codebase.
category: desktop
tags: [flutter, desktop, cross-platform, dart, gui]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Flutter Desktop
> Build native desktop apps for Windows, macOS, and Linux.
## Quick Start
```bash
flutter create --platforms=windows,macos,linux my_desktop_app
cd my_desktop_app && flutter run -d windows
```
## Window Management
```dart
import 'package:window_manager/window_manager'
void main() async {
  WidgetsFlutterBinding.ensureInitialized(); await windowManager.ensureInitialized()
  await windowManager.setSize(const Size(1280, 800)); await windowManager.setTitle('My App')
  runApp(MyApp())
}
```
## When to Use
- Cross-platform desktop apps; Material Design desktop; Existing Flutter mobile to desktop
## Validation
1. App builds for all platforms; 2. Window size settings apply; 3. Platform channels work
