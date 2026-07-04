"use client"

import { useState } from "react"
import type { Skill } from "@/lib/catalog"
import { CodePreview } from "@/components/CodePreview"

const CATEGORY_EMOJIS: Record<string, string> = {
  ai: "🤖", backend: "⚙️", frontend: "🎨", devops: "🚀",
  security: "🔒", database: "🗄️", qa: "🧪", mobile: "📱",
  cloud: "☁️", data: "📊", blockchain: "⛓️", design: "🎯",
  gamedev: "🎮", iot: "📡", networking: "🌐", "ar-vr": "🥽",
}

export function SkillContent({ skill }: { skill: Skill }) {
  const [copied, setCopied] = useState(false)
  const installCmd = `claude-skills install ${skill.name}`

  async function copyInstall() {
    try {
      await navigator.clipboard.writeText(installCmd)
      setCopied(true)
      setTimeout(() => setCopied(false), 2000)
    } catch {
      // clipboard not available
    }
  }

  const emoji = CATEGORY_EMOJIS[skill.category] || "📋"

  return (
    <article>
      <div className="mb-8">
        <div className="mb-3 flex items-center gap-2 text-sm text-zinc-500 dark:text-zinc-400">
          <span>
            {emoji} {skill.category}
          </span>
          <span>·</span>
          <span>v{skill.version}</span>
          {skill.has_ru && (
            <>
              <span>·</span>
              <span className="rounded bg-zinc-100 px-2 py-0.5 text-[11px] font-medium text-zinc-500 dark:bg-zinc-800 dark:text-zinc-400">
                EN + RU
              </span>
            </>
          )}
        </div>

        <h1 className="text-3xl font-bold text-zinc-900 dark:text-zinc-100">
          {skill.name}
        </h1>
        <p className="mt-3 text-lg text-zinc-600 dark:text-zinc-400">
          {skill.description}
        </p>

        <div className="mt-4 flex flex-wrap gap-2">
          {skill.tags.map((tag) => (
            <span
              key={tag}
              className="rounded-lg bg-zinc-100 px-3 py-1 text-sm font-medium text-zinc-600 dark:bg-zinc-800 dark:text-zinc-400"
            >
              {tag}
            </span>
          ))}
        </div>
      </div>

      <div className="mb-10 flex items-center gap-3 rounded-xl border border-zinc-200 bg-white p-4 dark:border-zinc-700 dark:bg-zinc-900">
        <code className="flex-1 text-sm text-zinc-700 dark:text-zinc-300">{installCmd}</code>
        <button
          onClick={copyInstall}
          className="rounded-lg bg-zinc-900 px-4 py-2 text-sm font-medium text-white transition-all hover:bg-zinc-800 active:scale-95 dark:bg-zinc-100 dark:text-zinc-900 dark:hover:bg-zinc-200"
        >
          {copied ? "Copied!" : "Copy Install"}
        </button>
      </div>

      <div className="prose prose-zinc max-w-none dark:prose-invert">
        <h2>Quick Start</h2>
        <CodePreview code={installCmd} />
        <p>
          After installing, the skill will be available in your{" "}
          <code>.claude/skills/{skill.category}/{skill.name}/</code> directory.
          Claude Code will automatically detect and use it.
        </p>

        <h2>Details</h2>
        <ul>
          <li><strong>Category:</strong> {skill.category}</li>
          <li><strong>Version:</strong> {skill.version}</li>
          <li><strong>Languages:</strong> {skill.languages.join(", ").toUpperCase()}</li>
          <li>
            <strong>Models:</strong>{" "}
            {Array.isArray(skill.models)
              ? skill.models.join(", ")
              : String(skill.models)}
          </li>
          {skill.created && (
            <li><strong>Created:</strong> {skill.created}</li>
          )}
          {skill.updated && (
            <li><strong>Updated:</strong> {skill.updated}</li>
          )}
        </ul>

        {skill.tags.length > 0 && (
          <>
            <h2>Tags</h2>
            <div className="flex flex-wrap gap-2 not-prose">
              {skill.tags.map((tag) => (
                <span
                  key={tag}
                  className="rounded-lg bg-violet-50 px-3 py-1 text-sm font-medium text-violet-700 dark:bg-violet-950 dark:text-violet-300"
                >
                  #{tag}
                </span>
              ))}
            </div>
          </>
        )}
      </div>
    </article>
  )
}
