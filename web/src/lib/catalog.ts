export interface Skill {
  name: string
  description: string
  category: string
  tags: string[]
  models: string[]
  version: string
  path: string
  languages: string[]
  has_ru: boolean
  created: string
  updated: string
}

export interface CatalogData {
  metadata: {
    schema_version: string
    generated_at: string
    total_skills: number
    total_ru: number
    domains: string[]
    bilingual: boolean
  }
  skills: Skill[]
}

export async function loadCatalog(): Promise<CatalogData> {
  if (typeof window === "undefined") {
    const fs = await import("fs")
    const path = await import("path")
    const filePath = path.join(process.cwd(), "public", "data", "catalog.json")
    const raw = fs.readFileSync(filePath, "utf-8")
    const data: CatalogData = JSON.parse(raw)
    return normalizeCatalog(data)
  }
  const res = await fetch("/data/catalog.json")
  if (!res.ok) throw new Error("Failed to load catalog")
  const data: CatalogData = await res.json()
  return normalizeCatalog(data)
}

function normalizeCatalog(data: CatalogData): CatalogData {
  for (const skill of data.skills) {
    if (typeof skill.tags === "string") {
      skill.tags = (skill.tags as string).split(",").map((t: string) => t.trim()).filter(Boolean)
    }
    if (typeof skill.models === "string") {
      skill.models = (skill.models as string).split(",").map((t: string) => t.trim()).filter(Boolean)
    }
  }
  return data
}

export function getCategories(catalog: CatalogData): string[] {
  return catalog.metadata.domains.sort()
}

export function getSkillBySlug(catalog: CatalogData, slug: string): Skill | undefined {
  return catalog.skills.find((s) => s.name === slug)
}

export function getSkillsByCategory(catalog: CatalogData, category: string): Skill[] {
  return catalog.skills.filter((s) => s.category === category)
}

export function getRelatedSkills(catalog: CatalogData, skill: Skill, limit = 6): Skill[] {
  const tagSet = new Set(skill.tags.map((t) => t.toLowerCase()))
  const scored = catalog.skills
    .filter((s) => s.name !== skill.name)
    .map((s) => {
      const overlap = s.tags.filter((t) => tagSet.has(t.toLowerCase())).length
      const sameCat = s.category === skill.category ? 1 : 0
      return { skill: s, score: overlap * 3 + sameCat * 2 }
    })
    .sort((a, b) => b.score - a.score)
  return scored.slice(0, limit).map((s) => s.skill)
}
