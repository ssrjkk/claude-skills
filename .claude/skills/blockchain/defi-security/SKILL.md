---
name: defi-security
description: "DeFi security audits and best practices"
category: blockchain
tags: [defi, security, audits, smart-contracts, solidity]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# DeFi Security

> Secure DeFi protocols against common vulnerabilities with audit-grade practices.

## Quick Start
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

// Security patterns for DeFi

// 1. Reentrancy protection
import "@openzeppelin/contracts/utils/ReentrancyGuard.sol";

contract SecureVault is ReentrancyGuard {
    mapping(address => uint256) private balances;

    // CEI pattern: Checks-Effects-Interactions
    function withdraw(uint256 amount) external nonReentrant {
        // Checks
        require(balances[msg.sender] >= amount, "Insufficient balance");
        
        // Effects (state changes first)
        balances[msg.sender] -= amount;
        
        // Interactions (external calls last)
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");
    }

    // 2. Access control
    function emergencyPause() external onlyOwner {
        _pause();
    }

    // 3. Oracle manipulation protection
    function getSafePrice() internal view returns (uint256) {
        // Use TWAP instead of spot price
        uint256 twap = oracle.consult(address(this), 
            UniOracleV3Library.computePoolAddress(
                factory, token0, token1, fee
            ), 30 minutes
        );
        return twap;
    }
}
```

## Key Concepts
Top DeFi vulnerabilities: reentrancy, oracle manipulation, flash loan attacks, sandwich attacks, integer overflow, access control, and frontrunning. Use Checks-Effects-Interactions pattern, TWAP oracles, and comprehensive fuzz testing.

## When to Use
- Auditing smart contracts before deployment
- Building secure DeFi protocols (lending, DEX, staking)
- Implementing security controls in existing protocols

## Validation
1. Slither and Mythril static analysis pass with no critical findings
2. Reentrancy tests pass with malicious contracts
3. Oracle manipulation attempts fail within realistic bounds
4. Fuzz testing covers all state-changing functions
