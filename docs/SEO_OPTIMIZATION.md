# SEO & Organic Growth Strategy

## Keyword Strategy

### Tier 1: High Volume, High Intent
```
"Claude AI skills" (1.2K searches/month) → Meta description optimized
"AI prompt library" (890 searches/month)
"developer prompt engineering" (650 searches/month)
"Python development skills" (5.2K searches/month)
"React best practices" (8.9K searches/month)
```

### Tier 2: Mid Volume, Specific
```
"FastAPI testing patterns" (320 searches/month)
"Kubernetes debugging guide" (180 searches/month)
"PostgreSQL optimization" (450 searches/month)
"TypeScript advanced patterns" (240 searches/month)
```

### Tier 3: Long Tail, High Conversion
```
"How to debug slow Kubernetes pods"
"PostgreSQL query optimization secrets"
"React hooks performance optimization"
"FastAPI async best practices"
```

## Technical SEO

### Page Structure (Each Skill)
```html
<h1>Skill Name: Python FastAPI API Development</h1>
<meta name="description" content="80-char optimized description with keywords">
<meta property="og:title" content="[Skill] - Claude Skills">
<meta property="og:description" content="Brief description">

<article>
  <h2>Quick Start</h2>
  <h3>Prerequisites</h3>
  <h3>Implementation</h3>
  <h3>Testing</h3>
</article>

<aside>
  <!-- Related skills -->
  <a href="/skills/backend/fastapi-crud">Related: CRUD operations</a>
</aside>

<!-- JSON-LD Schema -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "[Skill Name]",
  "author": {"@type": "Organization", "name": "Claude Skills"},
  "datePublished": "2026-07-25",
  "keywords": "[comma-separated keywords]"
}
</script>
```

### Site Architecture
```
/                           (Domain home)
/skills                     (Skill directory)
  /skills/{domain}          (Domain listing)
    /skills/{domain}/{name} (Individual skill) ← SEO target
/blog                       (Blog articles)
/docs                       (Documentation)
/leaderboard               (Public leaderboard)
```

## Content Strategy

### Blog Posts (2x/week)

**Week 1: Listicle**
```markdown
# Top 10 FastAPI Skills Every Backend Developer Should Know

1. [Skill 1] - Description and link
2. [Skill 2] - Description and link
...
10. [Skill 10] - Description and link

Keywords: FastAPI, backend, Python, development, skills
Internal links: 8-10 to relevant skills
```

**Week 2: How-To**
```markdown
# How to Debug Slow PostgreSQL Queries (3-Step Guide)

## Step 1: Identify the Problem
## Step 2: Use EXPLAIN ANALYZE
## Step 3: Optimize Your Query

Includes: Related skill links, code examples
Keywords: PostgreSQL, debugging, optimization, performance
```

**Week 3: Case Study**
```markdown
# How We Improved Code Quality 40% Using Claude Skills

Company: [Name]
Result: [Quantified outcome]
Skills Used: [Links to skills]

Keywords: Case study, productivity, development, tools
```

### Guest Posts (10+/month)
**Platforms:**
- Dev.to (2K+ followers, high SEO)
- Medium (large reach)
- Hashnode (developer audience)
- CSS-Tricks (frontend)
- LogRocket (frontend + DevOps)

**Strategy:**
- Link back to relevant skills
- Establish authority
- Drive referral traffic
- Build backlinks

## Link Building

### Earned Links
```
1. Product Hunt post (400+ links typically)
2. HackerNews coverage (1K+ links)
3. Reddit mentions (100+ subreddits)
4. Dev tool directories (20+ links)
5. GitHub awesome lists (15+ lists)
```

### Built Links
```
1. GitHub topic pages (claude, ai-skills)
2. Dev.to articles (internal links)
3. Blog posts (10+ per post)
4. Technical documentation (5+ per doc)
5. LinkedIn articles (personal branding)
```

## Local SEO (for specific regions)

### Russian Market
```
Keywords: "Claude скиллы", "AI промпты"
Telegram: Community in Russian
Habr.com: Russian tech community
VC.ru: Russian startup news
```

### Asian Markets
```
Keywords: Localized Chinese, Japanese, Korean
Wechat: Partnerships with Chinese devs
Zhihu: Chinese Stack Overflow
Youtube: Localized videos
```

## Monitoring & Analytics

### Tools Setup
```
Google Search Console
  - Monitor impressions, CTR, rankings
  - Track search performance by skill
  - Fix crawl errors

Google Analytics 4
  - Track organic traffic
  - User journeys to conversion
  - Engagement metrics

Ahrefs/Semrush
  - Competitor analysis
  - Backlink profile
  - Keyword opportunities
```

### Monthly SEO Report
```
📊 SEO Metrics (Month X)

Organic Traffic: 8,234 visitors (↑23% vs last month)
Average Position: 12.4 (↑ 1.2)
Clicks: 342 (↑45%)
CTR: 3.2% (↑0.3%)
Top Keywords: 
  1. "claude ai skills" - Position 8
  2. "fastapi testing" - Position 14
  3. "python patterns" - Position 11

Top Performing Skills:
  1. react-component - 234 organic visits
  2. fastapi-crud - 189 organic visits
  3. pytest-patterns - 156 organic visits
```

## Expected Growth

| Month | Organic Traffic | Keywords Ranking | Domain Authority |
|-------|-----------------|------------------|------------------|
| Month 1 | 300 | 5 (top 50) | 12 |
| Month 3 | 4.2K | 25 (top 50) | 18 |
| Month 6 | 18K | 80 (top 50) | 24 |
| Month 12 | 89K | 200+ (top 50) | 32+ |

## Quick Wins (Do First)

```
✅ Optimize existing skill pages (1 week)
   - Add meta descriptions
   - Improve H2/H3 structure
   - Add internal links

✅ Create 3 pillar blog posts (2 weeks)
   - "Complete [Framework] Guide"
   - Target high-volume keywords
   - Link to 20+ skills

✅ Set up Google Search Console (1 day)
   - Submit sitemap
   - Monitor crawl errors
   - Track search performance

✅ Start guest posting (ongoing)
   - 2 Dev.to posts/month
   - 1 Medium article/month
   - 1 Hashnode article/month
```
