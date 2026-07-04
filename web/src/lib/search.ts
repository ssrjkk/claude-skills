import type { Skill } from "./catalog"

export interface SearchResult {
  skill: Skill
  score: number
}

export function searchSkills(skills: Skill[], query: string): SearchResult[] {
  const q = query.toLowerCase().trim()
  if (!q) return []

  const results: SearchResult[] = []

  for (const skill of skills) {
    const name = skill.name.toLowerCase()
    const desc = skill.description.toLowerCase()
    const tags = skill.tags.map((t) => t.toLowerCase())
    const nameScore = scoreExact(name, q) * 100
    const descScore = scoreExact(desc, q) * 50
    const tagScore = tags.some((t) => t === q) ? 75 : tags.some((t) => t.includes(q)) ? 60 : 0

    const total = nameScore + descScore + tagScore
    if (total > 0) {
      results.push({ skill, score: total })
    }
  }

  results.sort((a, b) => b.score - a.score)
  return results
}

function scoreExact(text: string, query: string): number {
  if (text === query) return 1.0
  if (text.startsWith(query)) return 0.9
  if (text.includes(query)) return 0.7
  if (query.split(/\s+/).some((word) => text.includes(word))) return 0.4
  return 0
}

export function filterByCategory(skills: Skill[], category: string): Skill[] {
  if (!category || category === "all") return skills
  return skills.filter((s) => s.category === category)
}

export function filterByTag(skills: Skill[], tag: string): Skill[] {
  if (!tag) return skills
  return skills.filter((s) => s.tags.some((t) => t.toLowerCase() === tag.toLowerCase()))
}
