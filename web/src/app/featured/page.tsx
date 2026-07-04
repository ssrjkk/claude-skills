import { loadCatalog } from "@/lib/catalog"
import { SkillGrid } from "../skills/SkillGrid"
import { getCategories } from "@/lib/catalog"

export default async function FeaturedPage() {
  const catalog = await loadCatalog()
  const categories = getCategories(catalog)

  const featuredNames = [
    "react-component-library", "nextjs-fullstack", "fastapi-crud", "docker-compose", "kubernetes-deployment",
    "postgres-query-optimization", "ci-cd-pipeline", "api-security", "ml-pipeline", "react-native-app",
  ]

  const skills = catalog.skills.filter((s) => featuredNames.includes(s.name))

  return (
    <div className="mx-auto max-w-7xl px-4 py-10 sm:px-6 lg:px-8">
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-zinc-900 dark:text-zinc-100">Featured Skills</h1>
        <p className="mt-2 text-zinc-600 dark:text-zinc-400">
          Hand-picked {skills.length} essential skills to get started fast
        </p>
      </div>

      <SkillGrid skills={skills} categories={categories} />
    </div>
  )
}
