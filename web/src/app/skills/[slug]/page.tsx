import { notFound } from "next/navigation"
import { loadCatalog, getSkillBySlug, getRelatedSkills } from "@/lib/catalog"
import { SkillContent } from "./SkillContent"
import { SkillCard } from "@/components/SkillCard"

export async function generateStaticParams() {
  const catalog = await loadCatalog()
  return catalog.skills.map((skill) => ({ slug: skill.name }))
}

export default async function SkillPage({
  params,
}: {
  params: Promise<{ slug: string }>
}) {
  const { slug } = await params
  const catalog = await loadCatalog()
  const skill = getSkillBySlug(catalog, slug)

  if (!skill) {
    notFound()
  }

  const related = getRelatedSkills(catalog, skill)

  return (
    <div className="mx-auto max-w-4xl px-4 py-10 sm:px-6 lg:px-8">
      <SkillContent skill={skill} />

      {related.length > 0 && (
        <section className="mt-16 border-t border-zinc-200 pt-10 dark:border-zinc-800">
          <h2 className="mb-6 text-xl font-bold text-zinc-900 dark:text-zinc-100">
            Related Skills
          </h2>
          <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
            {related.map((s) => (
              <SkillCard key={s.name} skill={s} />
            ))}
          </div>
        </section>
      )}
    </div>
  )
}
