---
name: smart-contracts
description: Creates, tests, and deploys smart contracts using Hardhat or Foundry. Use for full blockchain development lifecycle.
category: blockchain
tags: [smart-contracts, solidity, hardhat, foundry, testing]
models: [opus]
version: 1.0.0
created: 2026-05-01
---
# Smart Contracts

> Full smart contract development lifecycle: from coding to deployment.

## Quick Start
```javascript
// hardhat.config.js
require("@nomicfoundation/hardhat-toolbox");

module.exports = {
  solidity: "0.8.28",
  networks: {
    sepolia: {
      url: process.env.SEPOLIA_URL,
      accounts: [process.env.PRIVATE_KEY]
    }
  }
};
```

## When to Use
- ✅ Building DApps on Ethereum
- ✅ Testing smart contracts
- ❌ Not for regular web applications

## Step-by-Step Instructions
1. Initialize project: `npx hardhat init`
2. Write contracts in `contracts/`
3. Create tests in `test/`
4. Deploy: `npx hardhat run scripts/deploy.js --network sepolia`

## Dependencies
```bash
npm install --save-dev hardhat @nomicfoundation/hardhat-toolbox
```

## Examples
Input: `npx hardhat test` → Output: All tests pass successfully

## Resources
- [Hardhat Docs](https://hardhat.org/docs)
- [Foundry Book](https://book.getfoundry.sh/)
- [Examples](./examples/)

## Validation
1. All tests pass
2. Contracts deploy without errors
3. Verification on Etherscan succeeds
