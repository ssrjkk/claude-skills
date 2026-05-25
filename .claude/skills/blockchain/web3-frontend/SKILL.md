---
name: web3-frontend
description: Web3 dApp frontend with wagmi/viem
category: blockchain
tags: [web3, dapp, frontend, wagmi, viem, react]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Web3 Frontend

> Build modern dApp frontends using wagmi hooks and viem for Ethereum interaction.

## Quick Start
```tsx
import { createConfig, http, useAccount, useReadContract, useWriteContract } from 'wagmi';
import { mainnet, sepolia } from 'wagmi/chains';
import { injected, metaMask } from 'wagmi/connectors';
import { formatEther, parseEther } from 'viem';

// Configuration
const config = createConfig({
  chains: [mainnet, sepolia],
  connectors: [injected(), metaMask()],
  transports: {
    [mainnet.id]: http(),
    [sepolia.id]: http(),
  },
});

// Component with hooks
function TokenBalance() {
  const { address, isConnected } = useAccount();
  const { data: balance } = useReadContract({
    address: '0x...',
    abi: erc20Abi,
    functionName: 'balanceOf',
    args: [address],
  });

  const { writeContract } = useWriteContract();

  const sendTokens = async () => {
    await writeContract({
      address: '0x...',
      abi: erc20Abi,
      functionName: 'transfer',
      args: ['0xrecipient', parseEther('10')],
    });
  };

  if (!isConnected) return <ConnectButton />;
  return (
    <div>
      <p>Balance: {formatEther(balance || 0n)}</p>
      <button onClick={sendTokens}>Send 10 Tokens</button>
    </div>
  );
}
```

## Key Concepts
wagmi provides React hooks for accounts, contracts, and transactions. viem is a type-safe Ethereum interaction library. Use `useReadContract` for reads, `useWriteContract` for writes, and `useWaitForTransactionReceipt` for confirmation.

## When to Use
- Building wallet-connected dApps
- Displaying on-chain data in React components
- Sending transactions with proper UX (pending, success, error states)

## Validation
1. Wallet connection works with MetaMask, WalletConnect, and Coinbase Wallet
2. Contract reads display correct on-chain data
3. Transaction submission shows loading/success/error states
4. Chain switching works correctly between networks
