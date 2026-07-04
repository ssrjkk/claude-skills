"use client"

import { useEffect, useState, useRef } from "react"
import Link from "next/link"

function AnimatedCounter({ target, suffix = "" }: { target: number; suffix?: string }) {
  const [count, setCount] = useState(0)
  const ref = useRef<HTMLSpanElement>(null)
  const done = useRef(false)

  useEffect(() => {
    const el = ref.current
    if (!el || done.current) return

    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting && !done.current) {
          done.current = true
          const duration = 1500
          const steps = 30
          const increment = target / steps
          let current = 0
          const timer = setInterval(() => {
            current += increment
            if (current >= target) {
              setCount(target)
              clearInterval(timer)
            } else {
              setCount(Math.floor(current))
            }
          }, duration / steps)
        }
      },
      { threshold: 0.5 },
    )

    observer.observe(el)
    return () => observer.disconnect()
  }, [target])

  return (
    <span ref={ref}>
      {count.toLocaleString()}
      {suffix}
    </span>
  )
}

export function Hero() {
  return (
    <section className="relative overflow-hidden">
      <div className="hero-gradient absolute inset-0" />

      <div className="relative mx-auto max-w-7xl px-4 pb-20 pt-16 sm:px-6 sm:pb-24 sm:pt-20 lg:px-8 lg:pb-32 lg:pt-28">
        <div className="mx-auto max-w-3xl text-center">
          <div className="mb-6 inline-flex items-center gap-2 rounded-full border border-violet-200 bg-violet-50 px-4 py-1.5 text-sm font-medium text-violet-700 dark:border-violet-800 dark:bg-violet-950 dark:text-violet-300">
            <span className="h-2 w-2 rounded-full bg-violet-500 animate-pulse-glow" />
            10,000+ skills for Claude Code
          </div>

          <h1 className="text-4xl font-bold tracking-tight text-zinc-900 sm:text-6xl lg:text-7xl dark:text-zinc-50">
            Make Claude Code
            <br />
            <span className="bg-gradient-to-r from-violet-600 to-cyan-500 bg-clip-text text-transparent">
              10x Better
            </span>
          </h1>

          <p className="mt-6 text-lg leading-8 text-zinc-600 dark:text-zinc-400">
            Battle-tested skills for Kubernetes, databases, frontend, AI/ML, security, and more.
            All bilingual (EN/RU). Install any skill with one command.
          </p>

          <div className="mt-8 flex items-center justify-center gap-4">
            <Link
              href="/skills"
              className="rounded-xl bg-zinc-900 px-6 py-3 text-sm font-semibold text-white shadow-lg transition-all hover:bg-zinc-800 hover:shadow-xl active:scale-95 dark:bg-zinc-100 dark:text-zinc-900 dark:hover:bg-zinc-200"
            >
              Browse Skills
            </Link>
            <code className="rounded-lg border border-zinc-200 bg-white px-4 py-2.5 text-sm text-zinc-700 dark:border-zinc-700 dark:bg-zinc-900 dark:text-zinc-300">
              pip install claude-skills
            </code>
          </div>

          <div className="mt-16 grid grid-cols-3 gap-8 border-t border-zinc-200 pt-10 dark:border-zinc-800">
            <div>
              <div className="text-3xl font-bold text-zinc-900 sm:text-4xl dark:text-zinc-50">
                <AnimatedCounter target={10000} suffix="+" />
              </div>
              <div className="mt-1 text-sm text-zinc-500 dark:text-zinc-400">Skills</div>
            </div>
            <div>
              <div className="text-3xl font-bold text-zinc-900 sm:text-4xl dark:text-zinc-50">
                <AnimatedCounter target={39} />
              </div>
              <div className="mt-1 text-sm text-zinc-500 dark:text-zinc-400">Domains</div>
            </div>
            <div>
              <div className="text-3xl font-bold text-zinc-900 sm:text-4xl dark:text-zinc-50">
                <AnimatedCounter target={100} suffix="%" />
              </div>
              <div className="mt-1 text-sm text-zinc-500 dark:text-zinc-400">Bilingual</div>
            </div>
          </div>
        </div>
      </div>
    </section>
  )
}
