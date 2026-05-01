---
name: web3js
description: Интегрирует Web3.js для взаимодействия с Ethereum блокчейном из JavaScript/TypeScript. Используется для создания фронтенда DApps.
category: block
tags: [web3, ethereum, dapp, javascript, typescript]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-01
---
# Web3.js

> Взаимодействие с Ethereum блокчейном из JavaScript приложений.

## 🚀 Quick Start
```javascript
import Web3 from 'web3';

const web3 = new Web3('https://mainnet.infura.io/v3/YOUR_INFURA_KEY');

// Получение баланса
const balance = await web3.eth.getBalance('0x...');
console.log(web3.utils.fromWei(balance, 'ether'));
```

## 📋 Когда использовать
- ✅ Создание фронтенда для DApps
- ✅ Чтение данных из смарт-контрактов
- ❌ Не использовать для бэкенда на Python

## 🔧 Пошаговая инструкция
1. Установи: `npm install web3`
2. Создай инстанс Web3 с провайдером
3. Взаимодействуй с контрактами через ABI
4. Подпиши транзакции через кошелек

## 📦 Зависимости
```bash
npm install web3
```

## 🧪 Примеры
Input: `getBalance(address)` → Output: Баланс в Wei, конвертируемый в ETH

## 🔗 Ресурсы
- [Web3.js Docs](https://web3js.readthedocs.io/)
- [Примеры кода](./examples/)

## ✅ Валидация
1. Подключение к ноде устанавливается
2. Чтение данных работает корректно
3. Транзакции подписываются и отправляются
