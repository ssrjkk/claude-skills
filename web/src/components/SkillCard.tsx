import Link from "next/link"
import type { Skill } from "@/lib/catalog"

export function SkillCard({ skill }: { skill: Skill }) {
  return (
    <Link
      href={`/skills/${skill.name}`}
      className="group block rounded-xl border border-zinc-200 bg-white p-5 transition-all hover:border-violet-200 hover:shadow-lg hover:shadow-violet-100 dark:border-zinc-800 dark:bg-zinc-900 dark:hover:border-violet-800 dark:hover:shadow-violet-950"
    >
      <div className="flex items-start justify-between gap-3">
        <h3 className="font-semibold text-zinc-900 group-hover:text-violet-600 dark:text-zinc-100 dark:group-hover:text-violet-400">
          {skill.name}
        </h3>
        {skill.has_ru && (
          <span className="shrink-0 rounded bg-zinc-100 px-2 py-0.5 text-[11px] font-medium text-zinc-500 dark:bg-zinc-800 dark:text-zinc-400">
            RU
          </span>
        )}
      </div>
      <p className="mt-1.5 line-clamp-2 text-sm text-zinc-600 dark:text-zinc-400">
        {skill.description}
      </p>
      <div className="mt-3 flex flex-wrap gap-1.5">
        {skill.tags.slice(0, 3).map((tag) => (
          <span
            key={tag}
            className="rounded-md bg-zinc-100 px-2 py-0.5 text-[11px] font-medium text-zinc-600 dark:bg-zinc-800 dark:text-zinc-400"
          >
            {tag}
          </span>
        ))}
      </div>
    </Link>
  )
}
