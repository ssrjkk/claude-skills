import { loadCatalog, getCategories } from "@/lib/catalog"
import { SkillGrid } from "./SkillGrid"

export default async function SkillsPage() {
  const catalog = await loadCatalog()
  const categories = getCategories(catalog)

  return (
    <div className="mx-auto max-w-7xl px-4 py-10 sm:px-6 lg:px-8">
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-zinc-900 dark:text-zinc-100">
          Skills Catalog
        </h1>
        <p className="mt-2 text-zinc-600 dark:text-zinc-400">
          {catalog.metadata.total_skills.toLocaleString()} skills across {categories.length} domains
        </p>
      </div>

      <SkillGrid
        skills={catalog.skills}
        categories={categories}
      />
    </div>
  )
}
