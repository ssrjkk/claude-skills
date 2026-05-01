---
name: smart-contracts
description: Создает, тестирует и деплоит смарт-контракты с использованием Hardhat или Foundry. Используется для полного цикла разработки на блокчейне.
category: block
tags: [smart-contracts, solidity, hardhat, foundry, testing]
models: [opus]
version: 1.0.0
created: 2026-05-01
---
# Smart Contracts

> Полный цикл разработки смарт-контрактов: от написания до деплоя.

## 🚀 Quick Start
```javascript
// hardhat.config.js
require("@nomicfoundation/hardhat-toolbox");

module.exports = {
  solidity: "0.8.20",
  networks: {
    goerli: {
      url: process.env.GOERLI_URL,
      accounts: [process.env.PRIVATE_KEY]
    }
  }
};
```

## 📋 Когда использовать
- ✅ Разработка DApps на Ethereum
- ✅ Тестирование смарт-контрактов
- ❌ Не использовать для обычных веб-приложений

## 🔧 Пошаговая инструкция
1. Инициализируй проект: `npx hardhat init`
2. Напиши контракты в `contracts/`
3. Создай тесты в `test/`
4. Деплой: `npx hardhat run scripts/deploy.js --network goerli`

## 📦 Зависимости
```bash
npm install --save-dev hardhat @nomicfoundation/hardhat-toolbox
```

## 🧪 Примеры
Input: `npx hardhat test` → Output: Все тесты проходят успешно

## 🔗 Ресурсы
- [Hardhat Docs](https://hardhat.org/docs)
- [Foundry Book](https://book.getfoundry.sh/)
- [Примеры кода](./examples/)

## ✅ Валидация
1. Все тесты проходят
2. Контракты деплоятся без ошибок
3. Верификация на Etherscan проходит
