import { loadCatalog } from "@/lib/catalog"
import { Hero } from "@/components/Hero"
import { SkillCard } from "@/components/SkillCard"

export default async function Home() {
  const catalog = await loadCatalog()
  const featuredNames = [
    "react-component-library", "nextjs-fullstack", "fastapi-crud", "docker-compose", "kubernetes-deployment",
    "postgres-query-optimization", "ci-cd-pipeline", "api-security", "ml-pipeline", "react-native-app",
    "typescript-basics", "python-testing",
  ]
  const topSkills = catalog.skills.filter((s) => featuredNames.includes(s.name)).length
    ? catalog.skills.filter((s) => featuredNames.includes(s.name))
    : catalog.skills.slice(0, 12)

  return (
    <>
      <Hero />

      <section className="border-t border-zinc-200 bg-white py-16 dark:border-zinc-800 dark:bg-zinc-950">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
          <div className="mb-10 text-center">
            <h2 className="text-2xl font-bold text-zinc-900 dark:text-zinc-100">
              Featured Skills
            </h2>
            <p className="mt-2 text-zinc-600 dark:text-zinc-400">
              A selection from {catalog.metadata.total_skills.toLocaleString()} skills across{" "}
              {catalog.metadata.domains.length} domains
            </p>
          </div>

          <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
            {topSkills.map((skill) => (
              <SkillCard key={skill.name} skill={skill} />
            ))}
          </div>
          <div className="mt-8 text-center">
            <a
              href="/featured"
              className="inline-flex items-center gap-1.5 rounded-lg bg-zinc-900 px-5 py-2.5 text-sm font-medium text-white transition-colors hover:bg-zinc-800 dark:bg-zinc-100 dark:text-zinc-900 dark:hover:bg-zinc-200"
            >
              View all featured skills
              <svg className="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7"/></svg>
            </a>
          </div>
        </div>
      </section>

      <section className="border-t border-zinc-200 bg-zinc-50 py-16 dark:border-zinc-800 dark:bg-zinc-900">
        <div className="mx-auto max-w-4xl px-4 text-center sm:px-6 lg:px-8">
          <h2 className="text-2xl font-bold text-zinc-900 dark:text-zinc-100">
            One Command to Install
          </h2>
          <p className="mt-3 text-zinc-600 dark:text-zinc-400">
            Install any skill directly from the CLI. No config files, no manual setup.
          </p>
          <div className="mt-6 rounded-xl bg-zinc-950 p-6 text-left dark:bg-black">
            <pre className="text-sm text-zinc-300">
              <code>{`# Install a skill
claude-skills install k8s-debugger

# Search the catalog
claude-skills search kubernetes

# Generate your own skill
claude-skills generate "Debug PostgreSQL slow queries"`}</code>
            </pre>
          </div>
        </div>
      </section>
    </>
  )
}
