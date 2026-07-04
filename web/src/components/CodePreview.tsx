"use client"

import { useState } from "react"

export function CodePreview({ code, language = "bash" }: { code: string; language?: string }) {
  const [copied, setCopied] = useState(false)

  async function handleCopy() {
    try {
      await navigator.clipboard.writeText(code)
      setCopied(true)
      setTimeout(() => setCopied(false), 2000)
    } catch {
      // clipboard not available
    }
  }

  return (
    <div className="group relative my-4 overflow-hidden rounded-xl border border-zinc-200 bg-zinc-950 dark:border-zinc-700">
      <div className="flex items-center justify-between border-b border-zinc-800 px-4 py-2">
        <span className="text-xs text-zinc-500">{language}</span>
        <button
          onClick={handleCopy}
          className="rounded-md px-2 py-1 text-xs text-zinc-400 transition-colors hover:bg-zinc-800 hover:text-zinc-200"
        >
          {copied ? "Copied!" : "Copy"}
        </button>
      </div>
      <pre className="overflow-x-auto p-4 text-sm leading-relaxed">
        <code className="font-mono text-zinc-300">{code}</code>
      </pre>
    </div>
  )
}
