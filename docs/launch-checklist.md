# Launch Checklist

## Pre-Launch (Week -1)

### Technical
- [ ] `make validate` passes with 0 errors
- [ ] `make test` passes (82/82)
- [ ] `ruff check src/ tests/ scripts/` — clean
- [ ] `mypy src/` — clean
- [ ] `python scripts/audit_skills.py --top 100` — top skills reviewed
- [ ] docs site builds successfully
- [ ] Install script tested (`curl ... | bash`)
- [ ] All 10,000+ skills verified on disk

### Content
- [ ] README: badges, screenshots, metrics — final review
- [ ] Top 50 skills manually audited for quality
- [ ] Top 10 skills have working code examples
- [ ] At least 50 RU translations reviewed as real translations

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

## Month 3 Goals

| Metric | Target |
|--------|--------|
| Stars | 500+ |
| Forks | 50+ |
| Contributors | 25+ |
| Quality score | 75%+ |
| Telegram | 200+ |
| Product Hunt upvotes | 100+ |

## Quick Reference

| Platform | Post | Link |
|----------|------|------|
| Product Hunt | 10,000+ Skills for Claude Code | producthunt.com/posts/claude-skills |
| Habr | Как я создал крупнейшую библиотеку навыков для Claude | habr.com/... |
| Reddit r/ClaudeAI | I built 10K skills for Claude | reddit.com/... |
| Twitter/X | Thread | twitter.com/claude_skills |
| Dev.to | Series (3 articles) | dev.to/claude-skills |
