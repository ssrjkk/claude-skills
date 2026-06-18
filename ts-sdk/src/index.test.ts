import { describe, it, expect } from "vitest"
import { byCategory, byTag, search, isValidCategory, overallScore, grade } from "./index"

const mockSkills = [
  { name: "test-skill", description: "A test skill", category: "qa", tags: ["testing", "qa"], models: ["sonnet"], version: "1.0", path: "", languages: ["en"], hasRu: false },
  { name: "dev-skill", description: "Dev skill", category: "devops", tags: ["devops", "ci"], models: ["opus"], version: "1.0", path: "", languages: ["en", "ru"], hasRu: true },
]

describe("byCategory", () => {
  it("groups skills by category", () => {
    const grouped = byCategory(mockSkills)
    expect(grouped["qa"]).toHaveLength(1)
    expect(grouped["devops"]).toHaveLength(1)
  })
})

describe("byTag", () => {
  it("groups skills by tag", () => {
    const grouped = byTag(mockSkills)
    expect(grouped["testing"]).toHaveLength(1)
    expect(grouped["devops"]).toHaveLength(1)
  })
})

describe("search", () => {
  it("finds skills by name", () => {
    expect(search(mockSkills, "test")).toHaveLength(1)
  })
  it("finds skills by description", () => {
    expect(search(mockSkills, "dev")).toHaveLength(1)
  })
})

describe("isValidCategory", () => {
  it("validates known categories", () => {
    expect(isValidCategory("qa")).toBe(true)
    expect(isValidCategory("invalid")).toBe(false)
  })
})

describe("overallScore", () => {
  it("calculates weighted score", () => {
    const score = overallScore({ completeness: 100, depth: 80, codeQuality: 60, freshness: 40, bilingual: 20 })
    expect(score).toBeGreaterThan(0)
    expect(score).toBeLessThanOrEqual(100)
  })
})

describe("grade", () => {
  it("returns correct grades", () => {
    expect(grade(95)).toBe("A")
    expect(grade(85)).toBe("B")
    expect(grade(70)).toBe("C")
    expect(grade(55)).toBe("D")
    expect(grade(30)).toBe("F")
  })
})
