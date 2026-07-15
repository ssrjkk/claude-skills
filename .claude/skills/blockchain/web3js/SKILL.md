---
name: web3js
description: "Integrates Web3.js for interacting with Ethereum blockchain from JavaScript/TypeScript. Use for DApp frontend development."
category: blockchain
tags: [web3, ethereum, dapp, javascript, typescript]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-01
---
# Web3.js

> Interact with the Ethereum blockchain from JavaScript applications.

## Quick Start
```javascript
import Web3 from 'web3';

const web3 = new Web3('https://mainnet.infura.io/v3/YOUR_INFURA_KEY');

// Get balance
const balance = await web3.eth.getBalance('0x...');
console.log(web3.utils.fromWei(balance, 'ether'));
```

## When to Use
- ✅ Building DApp frontends
- ✅ Reading data from smart contracts
- ❌ Not for Python backends

## Step-by-Step Instructions
1. Install: `npm install web3`
2. Create Web3 instance with provider
3. Interact with contracts via ABI
4. Sign transactions via wallet

## Dependencies
```bash
npm install web3
```

## Examples
Input: `getBalance(address)` → Output: Balance in Wei, convertible to ETH

## Resources
- [Web3.js Docs](https://web3js.readthedocs.io/)
- [Examples](./examples/)

## Validation
1. Connection to node established
2. Reading data works correctly
3. Transactions are signed and sent
