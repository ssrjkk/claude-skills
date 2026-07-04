export function Footer() {
  return (
    <footer className="border-t border-zinc-200 bg-white dark:border-zinc-800 dark:bg-zinc-950">
      <div className="mx-auto max-w-7xl px-4 py-8 sm:px-6 lg:px-8">
        <div className="flex flex-col items-center justify-between gap-4 sm:flex-row">
          <p className="text-sm text-zinc-500 dark:text-zinc-400">
            Built by{" "}
            <a
              href="https://github.com/ssrjkk"
              target="_blank"
              rel="noopener noreferrer"
              className="font-medium text-zinc-700 hover:text-zinc-900 dark:text-zinc-300 dark:hover:text-zinc-100"
            >
              ssrjkk
            </a>
          </p>
          <div className="flex items-center gap-6 text-sm text-zinc-500 dark:text-zinc-400">
            <a
              href="https://github.com/ssrjkk/claude-skills"
              target="_blank"
              rel="noopener noreferrer"
              className="transition-colors hover:text-zinc-900 dark:hover:text-zinc-100"
            >
              GitHub
            </a>
            <span>MIT License</span>
          </div>
        </div>
      </div>
    </footer>
  )
}
