---
name: hardhat
description: "Develops, tests, and deploys Ethereum smart contracts with Hardhat, including local node and debugging."
category: block
tags: [hardhat, ethereum, smart-contracts, solidity, testing]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Hardhat
> Ethereum development environment for smart contracts.
## Quick Start
```bash
npm install --save-dev hardhat
npx hardhat init
npx hardhat node     # Local Ethereum node
npx hardhat test     # Run tests
```
## Hardhat Config
```javascript
require("@nomicfoundation/hardhat-toolbox")
module.exports = { solidity: "0.8.20", networks: { hardhat: { chainId: 1337 } } }
```
## Testing with Hardhat
```javascript
const { expect } = require("chai")
describe("Token", function () {
  it("should deploy correctly", async function () {
    const Token = await ethers.getContractFactory("Token")
    const token = await Token.deploy()
    expect(await token.totalSupply()).to.equal(ethers.utils.parseEther("1000000"))
  })
})
```
## When to Use
- Ethereum smart contract development; Testing; Local blockchain simulation
## Validation
1. hardhat node starts; 2. Contracts compile; 3. Tests pass
