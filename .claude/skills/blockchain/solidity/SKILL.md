---
name: solidity
description: "Develops smart contracts on Solidity for Ethereum and EVM-compatible blockchains. Use for decentralized applications."
category: blockchain
tags: [solidity, ethereum, smart-contracts, evm, blockchain]
models: [opus]
version: 1.0.0
created: 2026-05-01
---
# Solidity

> Smart contract development on Solidity for Ethereum and EVM.

## Quick Start
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

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

## When to Use
- ✅ Creating smart contracts for Ethereum
- ✅ Developing DeFi protocols
- ❌ Not for non-blockchain applications

## Step-by-Step Instructions
1. Install Hardhat or Foundry: `npm install --save-dev hardhat`
2. Create contract in `contracts/` folder
3. Write tests in `test/`
4. Deploy: `npx hardhat run scripts/deploy.js`

## Dependencies
```bash
npm install --save-dev hardhat @nomicfoundation/hardhat-toolbox
```

## Examples
Input: Call `set(100)` → Output: `get()` returns 100

## Resources
- [Solidity Docs](https://docs.soliditylang.org/)
- [Examples](./examples/)

## Validation
1. Contract compiles without errors
2. Tests pass successfully
3. Gas-optimized functions
