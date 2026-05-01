---
name: solidity
description: Разрабатывает смарт-контракты на Solidity для Ethereum и EVM-совместимых блокчейнов. Используется для создания децентрализованных приложений.
category: block
tags: [solidity, ethereum, smart-contracts, evm, blockchain]
models: [opus]
version: 1.0.0
created: 2026-05-01
---
# Solidity

> Разработка смарт-контрактов на Solidity для Ethereum и EVM.

## 🚀 Quick Start
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleStorage {
    uint256 private storedData;
    
    function set(uint256 x) public {
        storedData = x;
    }
    
    function get() public view returns (uint256) {
        return storedData;
    }
}
```

## 📋 Когда использовать
- ✅ Создание смарт-контрактов для Ethereum
- ✅ Разработка DeFi протоколов
- ❌ Не использовать для не-блокчейн приложений

## 🔧 Пошаговая инструкция
1. Установи Hardhat или Foundry: `npm install --save-dev hardhat`
2. Создай контракт в папке `contracts/`
3. Напиши тесты в `test/`
4. Деплой: `npx hardhat run scripts/deploy.js`

## 📦 Зависимости
```bash
npm install --save-dev hardhat @nomicfoundation/hardhat-toolbox
```

## 🧪 Примеры
Input: Вызов `set(100)` → Output: `get()` возвращает 100

## 🔗 Ресурсы
- [Solidity Docs](https://docs.soliditylang.org/)
- [Примеры кода](./examples/)

## ✅ Валидация
1. Контракт компилируется без ошибок
2. Тесты проходят успешно
3. Газо-оптимизированные функции
