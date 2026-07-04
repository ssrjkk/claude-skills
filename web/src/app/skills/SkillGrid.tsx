"use client"

import { useState, useMemo } from "react"
import type { Skill } from "@/lib/catalog"
import { searchSkills } from "@/lib/search"
import { SkillCard } from "@/components/SkillCard"

export function SkillGrid({
  skills,
  categories,
}: {
  skills: Skill[]
  categories: string[]
}) {
  const [query, setQuery] = useState("")
  const [category, setCategory] = useState("all")
  const [page, setPage] = useState(0)
  const perPage = 48

  const filtered = useMemo(() => {
    let result = skills

    if (query.trim()) {
      const searchResults = searchSkills(skills, query)
      result = searchResults.map((r) => r.skill)
    }

    if (category !== "all") {
      result = result.filter((s) => s.category === category)
    }

    return result
  }, [skills, query, category])

  const paged = useMemo(
    () => filtered.slice(0, (page + 1) * perPage),
    [filtered, page],
  )

  const hasMore = paged.length < filtered.length

  function handleSearch(e: React.FormEvent) {
    e.preventDefault()
    setPage(0)
  }

  return (
    <>
      <div className="mb-6 space-y-4">
        <form onSubmit={handleSearch} className="flex gap-3">
          <input
            type="text"
            placeholder="Search by name, description, or tags..."
            value={query}
            onChange={(e) => {
              setQuery(e.target.value)
              setPage(0)
            }}
            className="flex-1 rounded-xl border border-zinc-200 bg-white px-5 py-3 text-sm text-zinc-900 placeholder-zinc-400 outline-none transition-colors focus:border-violet-400 focus:ring-2 focus:ring-violet-100 dark:border-zinc-700 dark:bg-zinc-900 dark:text-zinc-100 dark:placeholder-zinc-500 dark:focus:border-violet-500 dark:focus:ring-violet-900"
          />
        </form>

        <div className="flex flex-wrap gap-2">
          <button
            onClick={() => { setCategory("all"); setPage(0) }}
            className={`rounded-lg px-3 py-1.5 text-sm font-medium transition-colors ${
              category === "all"
                ? "bg-zinc-900 text-white dark:bg-zinc-100 dark:text-zinc-900"
                : "bg-zinc-100 text-zinc-600 hover:bg-zinc-200 dark:bg-zinc-800 dark:text-zinc-400 dark:hover:bg-zinc-700"
            }`}
          >
            All
          </button>
          {categories.map((cat) => (
            <button
              key={cat}
              onClick={() => { setCategory(cat); setPage(0) }}
              className={`rounded-lg px-3 py-1.5 text-sm font-medium transition-colors ${
                category === cat
                  ? "bg-zinc-900 text-white dark:bg-zinc-100 dark:text-zinc-900"
                  : "bg-zinc-100 text-zinc-600 hover:bg-zinc-200 dark:bg-zinc-800 dark:text-zinc-400 dark:hover:bg-zinc-700"
              }`}
            >
              {cat}
            </button>
          ))}
        </div>
      </div>

      <p className="mb-4 text-sm text-zinc-500 dark:text-zinc-400">
        {filtered.length} skill{filtered.length !== 1 ? "s" : ""}
        {query && ` for "${query}"`}
      </p>

      <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
        {paged.map((skill) => (
          <SkillCard key={skill.name} skill={skill} />
        ))}
      </div>

      {hasMore && (
        <div className="mt-8 text-center">
          <button
            onClick={() => setPage((p) => p + 1)}
            className="rounded-xl border border-zinc-200 bg-white px-8 py-3 text-sm font-semibold text-zinc-700 transition-all hover:border-zinc-300 hover:shadow-md dark:border-zinc-700 dark:bg-zinc-900 dark:text-zinc-300 dark:hover:border-zinc-600"
          >
            Load More ({filtered.length - paged.length} remaining)
          </button>
        </div>
      )}
    </>
  )
}
