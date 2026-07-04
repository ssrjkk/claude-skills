# How We Score 10,000+ AI Skills — Quality Scoring System Deep Dive

## Why Quality Scoring?
With 10,000+ skills across 39 domains, you can't manually review every one. We needed an automated quality scoring system that reflects real-world usefulness.

## The Five Dimensions

Each skill is scored on 5 dimensions (0–100), weighted into an overall score:

### 1. Completeness (25%)
Does the skill have all required sections? We check for Quick Start, When to Use, Step-by-Step instructions, Validation criteria, and code examples. Skills missing critical sections lose points.

### 2. Depth (25%)
Is the content substantial? We measure total content length, section depth, and coverage of edge cases. A skill with 200+ words of real content scores higher than one with minimal explanations.

### 3. Code Quality (20%)
Are the code examples well-formed? We check for proper syntax, realistic examples (not placeholder), and language-appropriate patterns. Skills with working, production-quality code score highest.

### 4. Freshness (15%)
Is the skill up to date? We consider the `updated` timestamp and version number. Skills updated within the last 3 months score highest; skills older than 12 months lose points.

### 5. Bilingual (15%)
Are both language versions present and consistent? Skills with both EN and RU translations score higher. We also check that translations are substantial (not just machine-translated stubs).

## Overall Grade

```
A (90-100): Production-ready, bilingual, comprehensive
B (75-89): Good quality, may lack depth or recent updates
C (50-74): Functional but needs improvement
D (25-49): Significant gaps
F (0-24): Minimal content
```

## Validation Pipeline
Before scoring, each skill passes through the validation pipeline:
1. Frontmatter validation (required fields, valid category, proper tags)
2. Body validation (minimum length, no TODO/FIXME patterns)
3. Structural validation (required sections present)
4. Anti-pattern detection (placeholder names, broken references)

The full pipeline validates all 10,000+ skills in **7.8 seconds** (~1,282 skills/second).

## Results
- Current average quality score: 59% (C grade)
- Top 10% of skills score A or B
- Bottom 20% need significant improvement
- Continuous improvement via CI/CD pipeline

## Links
- GitHub: https://github.com/ssrjkk/claude-skills
- Quality report: https://ssrjkk.github.io/claude-skills/
