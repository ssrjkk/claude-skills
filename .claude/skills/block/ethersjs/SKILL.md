---
name: ethersjs
description: "Interacts with Ethereum blockchain using ethers.js library for transactions, contracts, and accounts."
category: block
tags: [ethersjs, web3, ethereum, transactions, contracts]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# ethers.js
> JavaScript library for interacting with Ethereum blockchain.
## Quick Start
```javascript
import { ethers } from 'ethers'
const provider = new ethers.JsonRpcProvider('https://mainnet.infura.io/v3/YOUR_KEY')
const balance = await provider.getBalance('vitalik.eth')
console.log(ethers.formatEther(balance))
```
## Smart Contract Interaction
```javascript
const contract = new ethers.Contract(contractAddress, abi, signer)
const tx = await contract.transfer('0x...', ethers.parseEther('1.0'))
await tx.wait()
```
## When to Use
- DApp frontend development; Transaction signing; Contract interaction
## Validation
1. Provider connects; 2. Contract calls return data; 3. Transactions send correctly
