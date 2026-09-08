---
name: electron
description: "Builds cross-platform desktop applications with Electron, React, and IPC communication. Use for native desktop apps with web tech."
category: desktop
tags: [electron, desktop, russian]
models: [sonnet, opus]
version: "1.0"
language: ru
original: electron
---
# Electron

> Кросс-платформенные десктоп-приложения на JavaScript, HTML и CSS.

## Быстрый старт
```javascript
// main.js
const { app, BrowserWindow, ipcMain } = require('electron');

function createWindow() {
  const win = new BrowserWindow({
    width: 1200,
    height: 800,
    webPreferences: {
      nodeIntegration: false,
      contextIsolation: true,
      preload: __dirname + '/preload.js',
    },
  });
  win.loadURL('http://localhost:5173'); // или loadFile('dist/index.html')
}

app.whenReady().then(createWindow);

// IPC-обработчик
ipcMain.handle('get-user-data', async () => {
  return { name: 'Alice', role: 'admin' };
});
```

```javascript
// preload.js
const { contextBridge, ipcRenderer } = require('electron');
contextBridge.exposeInMainWorld('electronAPI', {
  getUserData: () => ipcRenderer.invoke('get-user-data'),
});
```

## Когда использовать
- Кросс-платформенные десктоп-приложения (Windows, Mac, Linux)
- Приложения на веб-фреймворках (React, Vue, Svelte)
- Не для лёгких приложений (лучше Tauri)

## Пошаговые инструкции
1. Инициализация: `npm init; npm install electron --save-dev`
2. Создайте `main.js` с созданием окна
3. Создайте `preload.js` для безопасного IPC
4. Сборка и упаковка: `npx electron-builder`

## Зависимости
```bash
npm install electron --save-dev
npm install electron-builder --save-dev
```

## Примеры
Вход: `npm run start` → Выход: нативное десктоп-окно с веб-приложением

## Ресурсы
- [Electron Docs](https://www.electronjs.org/docs)
- [Examples](./examples/)

## Устранение неполадок
- **Раздувание из-за `node_modules`** — в сборку попало всё подряд.
  Используйте `files`/`asar` в `electron-builder` и исключите dev-зависимости.
- **Белый экран** — упал renderer. Откройте консоль DevTools и проверьте,
  что preload-скрипт безопасно работает с IPC при `contextIsolation`.
- **Приложение не перезапускается** — главное окно уничтожается при закрытии.
  Отключите выход по `window-all-closed` на macOS или повесьте `before-quit`.
- **Нативные модули не грузятся** — рассинхрон ABI после апгрейда Node.
  Пересоберите через `electron-rebuild` и зафиксируйте версию ABI.

## Валидация
1. Окно приложения открывается корректно
2. IPC-коммуникация работает
3. Приложение упаковывается под целевую ОС
