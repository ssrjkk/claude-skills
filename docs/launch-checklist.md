# Launch Checklist

## Pre-Launch (Week -1) ✓

### Technical ✓
- [x] `make validate` passes with 0 errors
- [x] `make test` passes (82/82)
- [x] `ruff check src/ tests/ scripts/` — clean
- [x] `mypy src/` — clean
- [x] `python scripts/audit_skills.py --top 100` — top skills reviewed
- [x] Docs site builds successfully (Next.js 16, 10006 pages)
- [x] Install script tested (`curl ... | bash`)
- [x] All 10,000+ skills verified on disk
- [x] GitHub Action created (`action.yml`, `Dockerfile`, `entrypoint.sh`)
- [x] VS Code Extension created (`vscode-extension/`)
- [x] Next.js site built and working (10K+ static pages)
- [x] Quality report generated

### Content ✓
- [x] README: badges, screenshots, metrics — final review
- [x] Top 50 skills manually curated in `featured/featured-skills.json`
- [x] Top 50 skills picked across 15 core domains
- [x] 50 curated skills available on /featured page

### Launch Content ✓
- [x] Product Hunt draft (`docs/producthunt-draft.md`)
- [x] Habr article (Russian, `docs/habr-draft.md`)
- [x] Twitter/X thread (`docs/twitter-thread.md`)
- [x] Reddit r/ClaudeAI post (`docs/launch/reddit-claudeai.md`)
- [x] Reddit r/programming post (`docs/launch/reddit-programming.md`)
- [x] Reddit r/Python post (`docs/launch/reddit-python.md`)
- [x] Dev.to Architecture article (`docs/launch/devto-architecture.md`)
- [x] Dev.to Quality Scoring article (`docs/launch/devto-quality.md`)
- [x] Dev.to Contributing article (`docs/launch/devto-contribute.md`)
- [x] Marketing plan with metrics (`docs/marketing-plan.md`)

### Community
- [ ] Telegram group created: [t.me/claude_skills](https://t.me/claude_skills)
- [ ] Twitter/X account: [@claude_skills](https://twitter.com/claude_skills)
- [ ] Dev.to profile set up
- [ ] GitHub Sponsors enabled (optional)

### Analytics
- [ ] Site analytics (Plausible/Umami) added to docs
- [ ] GitHub traffic insights enabled
- [ ] Install tracking (curl | bash → unique count)

---

## Launch Day — Monday

### 00:01 PST — Product Hunt
- [ ] Submit to Product Hunt
- [ ] Maker comment: "I built this because..."
- [ ] First 10 upvotes from community
- [ ] Respond to every comment within 1 hour

### 10:00 UTC — Habr
- [ ] Publish: "Как я создал крупнейшую библиотеку навыков для Claude"
- [ ] Cross-post to VC.ru

### 14:00 UTC — Reddit
- [ ] r/ClaudeAI: "I built 10,000+ skills for Claude Code — here's the story"
- [ ] r/programming: "Open source library of 10K structured AI skills"
- [ ] r/Python: "Claude Skills SDK — validate 10K AI prompts"

### Twitter/X Thread
```
I spent months building 10,000+ skills for Claude Code...

1/ The problem: Every time I asked Claude to write tests, I got generic output
2/ The solution: Structured skills with YAML frontmatter, EN+RU
3/ The result: 60% faster test writing, 40% better code quality
...
```

### Dev.to
- [ ] Article 1: "Top 10 Claude Skills for API Testing"

---

## Week 1 (Post-Launch)

- [ ] Monitor issues, respond < 24h
- [ ] Monitor social mentions
- [ ] Fix any bugs found
- [ ] Publish "Week 1 Update" on Dev.to

### Day 2: Dev.to Article 2
- "Automating Code Review with Claude Skills"

### Day 3: Dev.to Article 3
- "How to Create Your Own Claude Skill"

### Day 4: Twitter thread
- "Top 5 Claude Skills I use every day"

### Day 5: Reddit follow-up
- "I launched my Claude Skills library this week — here are the results"

---

## Week 2

- [ ] Analyze launch metrics
- [ ] Fix top reported issues
- [ ] Add top requested skills
- [ ] Send thank-you messages to early supporters
- [ ] Plan month 2 roadmap

---

## Month 1 Goals

| Metric | Target | Actual |
|--------|--------|--------|
| GitHub Stars | 100+ | |
| Forks | 10+ | |
| Contributors | 5+ | |
| Telegram members | 50+ | |
| Issues resolved | All incoming | |
| Quality score | 65%+ (from 59%) | |
| Product components | 4/4 (CLI, Action, Extension, SDK) | ✓ |
| Launch posts | 8/8 ready | ✓ |

## Month 3 Goals

| Metric | Target |
|--------|--------|
| Stars | 500+ |
| Forks | 50+ |
| Contributors | 25+ |
| Quality score | 75%+ |
| Telegram | 200+ |
| Product Hunt upvotes | 100+ |
| VS Code Marketplace | Published |
| GitHub Marketplace | Published |

## Quick Reference

| Platform | Post | File |
|----------|------|------|
| Product Hunt | Claude Skills — 10,000+ bilingual skills | `docs/producthunt-draft.md` |
| Habr | Как я создал крупнейшую библиотеку навыков для Claude | `docs/habr-draft.md` |
| Reddit r/ClaudeAI | I built 10,000+ structured skills for Claude Code | `docs/launch/reddit-claudeai.md` |
| Reddit r/programming | Open source library of 10K structured AI prompts | `docs/launch/reddit-programming.md` |
| Reddit r/Python | Claude Skills SDK — validate and score 10K+ AI prompts | `docs/launch/reddit-python.md` |
| Twitter/X | Thread (10 tweets) | `docs/twitter-thread.md` |
| Dev.to #1 | Building a Bilingual AI Skills Library — Architecture | `docs/launch/devto-architecture.md` |
| Dev.to #2 | Quality Scoring System Deep Dive | `docs/launch/devto-quality.md` |
| Dev.to #3 | How to Contribute | `docs/launch/devto-contribute.md` |

## Product Components

| Component | Status | Path |
|-----------|--------|------|
| Python CLI | ✓ | `src/claude_skills/cli.py` |
| Python SDK | ✓ | `src/claude_skills/` |
| TypeScript SDK | ✓ | `ts-sdk/` |
| GitHub Action | ✓ | `action.yml`, `Dockerfile` |
| VS Code Extension | ✓ | `vscode-extension/` |
| Next.js Site | ✓ | `web/` (10K+ pages) |
| Featured Skills | ✓ | `featured/featured-skills.json` |
| Install Script | ✓ | `install.sh` |
