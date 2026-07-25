# Contributor Rewards & Recognition

## 🏆 Badge System

Earn prestigious badges by contributing quality skills and translations:

| Badge | Requirement | Benefit |
|-------|-------------|---------|
| **⭐ Top Contributor** | 10+ merged skills (avg score 65%+) | Featured on README, monthly newsletter |
| **🎯 Active Contributor** | 5+ merged skills | Listed in Hall of Fame |
| **✅ Verified Skill Author** | 1 skill passes all quality checks | GitHub badge on profile |
| **🌍 Translator** | 5+ quality Russian translations | Translator badge, recognition |
| **🐛 Bug Hunter** | 3+ confirmed critical bugs fixed | Recognition in CHANGELOG |
| **📚 Documentation Master** | 10+ doc improvements merged | Listed as Doc Contributor |
| **🔥 Trending Skill Creator** | Skill gets 100+ downloads | Trending badge, featured on site |

## 💰 Monthly Recognition

**Top 3 Contributors** each month:
- Featured blog post: "Meet the contributor"
- Monthly prize pool: $100 (Pro plan credits or merchandise)
- Guaranteed feature announcement on Twitter/X

**Example:** "ssrjkk and 5 others just shipped 23 new skills this month. Here are the best..."

## 🎁 Milestone Rewards

| Milestone | Reward |
|-----------|--------|
| 100 merged skills | $50 store credit + merchandise |
| 500 merged skills | Lifetime Pro access + speaking opportunity |
| 1,000 merged skills | Co-maintainer role, revenue share (if monetized) |

## 📊 Contribution Leaderboard

Real-time leaderboard on `/leaderboard`:
- **All-time contributors** (by merged skills)
- **This month** (by activity)
- **Rising stars** (fastest growth)
- **Quality leaders** (highest avg score)

Track on GitHub: `/contributors`

---

## How to Earn Badges

### Skill Contribution Flow
```bash
1. Fork the repo
2. Create skill in .claude/skills/{domain}/{name}/SKILL.md
3. Include Russian translation (SKILL.ru.md)
4. Run `make validate` (must pass)
5. Open PR with description
6. CI runs quality checks automatically
7. Maintainer review (48h)
8. Merged ✅ → Badge awarded automatically

# Earn badge by hitting thresholds
# System tracks: merged_count, avg_quality_score, translation_quality
```

### Translation Contribution
```bash
1. Pick a skill needing translation
2. Create SKILL.ru.md with professional translation
3. Submit PR
4. Native Russian speaker reviews
5. Merged ✅ → Translation badge
```

---

## Integration with GitHub

### Automated Badge Assignment
Bot automatically awards badges via:
- GitHub profile badge (via profile README)
- Repository contributor card
- Leaderboard ranking

```markdown
<!-- Auto-generated in contributor's profile README -->
## Badges
![Claude Skills Top Contributor](https://img.shields.io/badge/Claude%20Skills-Top%20Contributor-gold)
![Verified Skill Author](https://img.shields.io/badge/Claude%20Skills-Verified%20Author-blue)
```

---

## Announcement Template

When contributor gets first badge:
```markdown
🎉 **Welcome to the Hall of Fame!**

@contributor just earned the **Verified Skill Author** badge for their skill:
[skill-name](link) — 72% quality score

[Follow @contributor](github) to see what they build next!
```

---

## FAQ

**Q: When do I get a badge?**
A: Automatically when merged skills hit the threshold. Check `/badges` to see your progress.

**Q: Can I get multiple badges?**
A: Yes! Contributors often earn 3-5 different badges. Top contributors have 10+.

**Q: Is there a way to track my progress?**
A: Yes. Visit `/profile/{username}` to see your stats, badges, and ranking.
