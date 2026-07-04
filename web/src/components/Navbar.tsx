"use client"

import Link from "next/link"
import { useState } from "react"
import { useRouter } from "next/navigation"

export function Navbar() {
  const [query, setQuery] = useState("")
  const router = useRouter()

  function handleSearch(e: React.FormEvent) {
    e.preventDefault()
    if (query.trim()) {
      router.push(`/skills?q=${encodeURIComponent(query.trim())}`)
    }
  }

  return (
    <nav className="sticky top-0 z-50 border-b border-zinc-200 bg-white/80 backdrop-blur-md dark:border-zinc-800 dark:bg-zinc-950/80">
      <div className="mx-auto flex h-16 max-w-7xl items-center gap-6 px-4 sm:px-6 lg:px-8">
        <Link href="/" className="flex items-center gap-2 font-semibold text-zinc-900 dark:text-zinc-100 shrink-0">
          <span className="flex h-8 w-8 items-center justify-center rounded-lg bg-gradient-to-br from-violet-500 to-cyan-500 text-xs font-bold text-white">
            CS
          </span>
          <span className="hidden sm:inline">Claude Skills</span>
        </Link>

        <form onSubmit={handleSearch} className="flex-1 max-w-md">
          <input
            type="text"
            placeholder="Search skills..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            className="w-full rounded-lg border border-zinc-200 bg-zinc-50 px-4 py-2 text-sm text-zinc-900 placeholder-zinc-400 outline-none transition-colors focus:border-violet-400 focus:bg-white focus:ring-2 focus:ring-violet-100 dark:border-zinc-700 dark:bg-zinc-800 dark:text-zinc-100 dark:placeholder-zinc-500 dark:focus:border-violet-500 dark:focus:bg-zinc-800 dark:focus:ring-violet-900"
          />
        </form>

        <div className="flex items-center gap-4 text-sm">
          <Link href="/skills" className="text-zinc-600 transition-colors hover:text-zinc-900 dark:text-zinc-400 dark:hover:text-zinc-100">
            Browse
          </Link>
          <a
            href="https://github.com/ssrjkk/claude-skills"
            target="_blank"
            rel="noopener noreferrer"
            className="text-zinc-600 transition-colors hover:text-zinc-900 dark:text-zinc-400 dark:hover:text-zinc-100"
          >
            GitHub
          </a>
        </div>
      </div>
    </nav>
  )
}
