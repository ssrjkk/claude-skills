---
name: solidity-optimization
description: "Gas optimization in Solidity"
category: blockchain
tags: [solidity, gas-optimization, ethereum, smart-contracts]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Solidity Optimization

> Minimize gas costs in Solidity smart contracts with advanced optimization techniques.

## Quick Start
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

// Gas optimization patterns

// 1. Pack structs to fit in fewer storage slots
struct User {                // Slot layout:
    uint128 balance;         // Slot 0 (shared)
    uint128 lastActivity;    // Slot 0 (shared)
    address userAddress;     // Slot 1
    bool isActive;           // Slot 1 (shared with address)
}

// 2. Use immutable for constants
address public immutable factory;  // Cheaper than storage
uint256 public constant DENOMINATOR = 1_000_000;  // Cheapest

// 3. Calldata vs memory
function processBatch(
    uint256[] calldata ids,     // calldata = cheaper for read-only
    address[] calldata owners
) external returns (uint256) {
    uint256 total;
    for (uint256 i = 0; i < ids.length; i++) {
        total += ids[i];
    }
    return total;
}

// 4. Unchecked arithmetic (Solidity 0.8+)
function sum(uint256[] calldata values) external pure returns (uint256 result) {
    uint256 length = values.length;
    unchecked {  // Skip overflow checks in loops
        for (uint256 i = 0; i < length; i++) {
            result += values[i];
        }
    }
}

// 5. Delete instead of reset
function resetBalance() external {
    delete balances[msg.sender];  // Gets gas refund
}
```

## Key Concepts
Storage is the most expensive operation. Pack variables into fewer slots, use `calldata` over `memory`, prefer `immutable`/`constant`, batch operations, and use `unchecked` blocks for loop counters.

## When to Use
- Deploying contracts where users pay gas
- High-frequency operations (DEX swaps, lending)
- Competitive DeFi protocols needing edge in gas efficiency

## Validation
1. Hardhat gas reporter shows improvements from baseline
2. Contract deploys with lower gas than naive implementation
3. Common operations (transfer, swap, mint) are < 200k gas
4. All optimizations pass the same functional tests
