/** Core types for Claude Skills Library */

export interface Skill {
  name: string
  description: string
  category: string
  tags: string[]
  models: string[]
  version: string
  path: string
  languages: string[]
  hasRu: boolean
  created?: string
  updated?: string
}

export interface CatalogMetadata {
  schemaVersion: string
  generatedAt: string
  totalSkills: number
  totalRu: number
  domains: string[]
  bilingual: boolean
}

export interface Catalog {
  metadata: CatalogMetadata
  skills: Skill[]
}

export interface ValidationIssue {
  skillPath: string
  severity: "error" | "warning" | "info"
  code: string
  message: string
  line?: number
}

export interface QualityScore {
  completeness: number
  depth: number
  codeQuality: number
  freshness: number
  bilingual: number
}

export function overallScore(score: QualityScore): number {
  const weights = { completeness: 0.25, depth: 0.25, codeQuality: 0.2, freshness: 0.15, bilingual: 0.15 }
  return Object.entries(weights).reduce((sum, [key, w]) => sum + (score as any)[key] * w, 0)
}

export function grade(score: number): string {
  if (score >= 90) return "A"
  if (score >= 80) return "B"
  if (score >= 65) return "C"
  if (score >= 50) return "D"
  return "F"
}

const VALID_CATEGORIES = new Set([
  "ai", "ar-vr", "backend", "block", "blockchain", "ci-cd-setup", "cloud",
  "communications", "data", "database", "database-migration", "design", "desktop",
  "devops", "ecommerce", "education", "embedded", "energy", "engineering",
  "finance", "frontend", "gamedev", "geospatial", "healthcare", "hr", "iot",
  "media", "mobile", "networking", "os-admin", "payments", "product", "qa",
  "scientific", "security", "supply-chain", "sustainability", "test-reporting",
  "api-testing",
])

export function getValidCategories(): string[] {
  return [...VALID_CATEGORIES].sort()
}

export function isValidCategory(cat: string): boolean {
  return VALID_CATEGORIES.has(cat)
}

export function byCategory(skills: Skill[]): Record<string, Skill[]> {
  const result: Record<string, Skill[]> = {}
  for (const s of skills) {
    (result[s.category] ??= []).push(s)
  }
  return result
}

export function byTag(skills: Skill[]): Record<string, Skill[]> {
  const result: Record<string, Skill[]> = {}
  for (const s of skills) {
    for (const tag of s.tags) {
      (result[tag] ??= []).push(s)
    }
  }
  return result
}

export function search(skills: Skill[], query: string): Skill[] {
  const q = query.toLowerCase()
  return skills.filter(
    (s) =>
      s.name.toLowerCase().includes(q) ||
      s.description.toLowerCase().includes(q) ||
      s.tags.some((t) => t.toLowerCase().includes(q)) ||
      s.category.toLowerCase().includes(q)
  )
}
