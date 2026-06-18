#!/usr/bin/env python3
"""Generate the documentation site from the catalog."""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path


def build_index_html(catalog_path: Path, output_dir: Path) -> str:
    with open(catalog_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    meta = data["metadata"]
    skills = data["skills"]

    by_category: dict[str, list] = {}
    for s in skills:
        by_category.setdefault(s["category"], []).append(s)

    lines = [
        "<!DOCTYPE html>",
        '<html lang="en">',
        "<head>",
        '  <meta charset="UTF-8">',
        '  <meta name="viewport" content="width=device-width, initial-scale=1.0">',
        "  <title>Claude Skills Library</title>",
        '  <link rel="stylesheet" href="style.css">',
        "</head>",
        "<body>",
        '  <div class="container">',
        '    <header>',
        '      <h1>Claude Skills Library</h1>',
        f'      <p class="subtitle">{meta["total_skills"]} skills across {len(meta["domains"])} domains',
        f'      <br>{meta["total_ru"]} Russian translations available</p>',
        "    </header>",
        '    <section id="stats">',
        "      <h2>Statistics</h2>",
        "      <div class=stats-grid>",
        f'        <div class=stat><strong>{meta["total_skills"]}</strong><span>Total Skills</span></div>',
        f'        <div class=stat><strong>{meta["total_ru"]}</strong><span>Russian Translations</span></div>',
        f'        <div class=stat><strong>{len(meta["domains"])}</strong><span>Domains</span></div>',
        f'        <div class=stat><strong>{meta["schema_version"]}</strong><span>Schema Version</span></div>',
        "      </div>",
        "    </section>",
        '    <section id="domains">',
        "      <h2>Domains</h2>",
        '      <div class="domain-list">',
    ]

    for domain in sorted(by_category):
        domain_skills = by_category[domain]
        ru = sum(1 for s in domain_skills if s.get("has_ru"))
        lines.extend([
            f'        <details class="domain">',
            f'          <summary><strong>{domain}</strong> ({len(domain_skills)} skills, {ru} RU)</summary>',
            f'          <ul class="skill-list">',
        ])
        for s in sorted(domain_skills, key=lambda x: x["name"]):
            flags = " 🇷🇺" if s.get("has_ru") else ""
            tags = ", ".join(s.get("tags", [])[:3])
            lines.append(f'            <li><code>{s["name"]}</code>{flags}<br><small>{tags}</small></li>')
        lines.extend([
            "          </ul>",
            "        </details>",
        ])

    lines.extend([
        "      </div>",
        "    </section>",
        "    <footer>",
        f"      <p>Generated on {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}</p>",
        '      <p><a href="https://github.com/ssrjkk/claude-skills">GitHub</a></p>',
        "    </footer>",
        "  </div>",
        "</body>",
        "</html>",
    ])

    html = "\n".join(lines)
    (output_dir / "index.html").write_text(html, encoding="utf-8")
    print(f"Index written to {output_dir / 'index.html'}")
    return html


def build_style_css(output_dir: Path) -> None:
    css = """* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  line-height: 1.6;
  color: #1a1a2e;
  background: #f8f9fa;
  padding: 2rem;
}

.container {
  max-width: 1000px;
  margin: 0 auto;
}

header {
  text-align: center;
  margin-bottom: 3rem;
}

header h1 {
  font-size: 2.5rem;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin-bottom: 0.5rem;
}

.subtitle {
  color: #666;
  font-size: 1.1rem;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 1.5rem;
  margin: 1.5rem 0;
}

.stat {
  background: white;
  border-radius: 12px;
  padding: 1.5rem;
  text-align: center;
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}

.stat strong {
  display: block;
  font-size: 2rem;
  color: #667eea;
}

.stat span {
  color: #666;
  font-size: 0.9rem;
}

h2 {
  margin: 2rem 0 1rem;
  font-size: 1.5rem;
  color: #1a1a2e;
}

.domain-list details {
  background: white;
  border-radius: 8px;
  margin-bottom: 0.75rem;
  box-shadow: 0 1px 4px rgba(0,0,0,0.04);
  overflow: hidden;
}

.domain-list summary {
  padding: 1rem 1.5rem;
  cursor: pointer;
  font-size: 1.05rem;
  transition: background 0.2s;
}

.domain-list summary:hover {
  background: #f0f0ff;
}

.skill-list {
  list-style: none;
  padding: 0.5rem 1.5rem 1rem;
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 0.5rem;
}

.skill-list li {
  padding: 0.35rem 0.5rem;
  font-size: 0.9rem;
}

.skill-list code {
  color: #667eea;
  font-size: 0.85rem;
}

.skill-list small {
  color: #999;
  display: block;
}

footer {
  margin-top: 3rem;
  text-align: center;
  color: #999;
  font-size: 0.9rem;
}

footer a {
  color: #667eea;
  text-decoration: none;
}
"""
    (output_dir / "style.css").write_text(css, encoding="utf-8")
    print(f"Stylesheet written to {output_dir / 'style.css'}")


def main() -> int:
    import argparse
    parser = argparse.ArgumentParser(description="Build documentation site")
    parser.add_argument("--catalog", default="skills_catalog.json", help="Path to catalog JSON")
    parser.add_argument("--output-dir", default="docs", help="Output directory")
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    api_dir = output_dir / "api"
    api_dir.mkdir(parents=True, exist_ok=True)

    build_index_html(Path(args.catalog), output_dir)
    build_style_css(output_dir)

    print(f"Documentation built in {output_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
