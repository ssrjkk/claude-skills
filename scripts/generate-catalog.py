import os, json, glob, ast
from datetime import datetime as dt

def parse_frontmatter(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    lines = content.split('\n')
    meta = {}
    in_front = False
    front_closed = False
    for line in lines:
        if front_closed:
            break
        if line.strip() == '---':
            if not in_front:
                in_front = True
            else:
                front_closed = True
            continue
        if in_front and ':' in line:
            key, _, value = line.partition(':')
            key = key.strip()
            value = value.strip()
            if value.startswith('['):
                try:
                    value = ast.literal_eval(value)
                except:
                    pass
            meta[key] = value
    return meta

BASE = '.claude/skills'
skills_index = {}
ru_skills = []

for sk_path in sorted(glob.glob(f'{BASE}/**/SKILL.md', recursive=True)):
    meta = parse_frontmatter(sk_path)
    if 'name' not in meta:
        continue
    path = sk_path.replace('\\', '/').replace(f'{BASE}/', '').replace('/SKILL.md', '')
    cat = meta.get('category', 'qa')
    name = meta['name']
    
    # Check if RU version exists
    ru_path = sk_path.replace('SKILL.md', 'SKILL.ru.md')
    has_ru = os.path.exists(ru_path)
    
    entry = {
        'name': name,
        'description': meta.get('description', ''),
        'category': cat,
        'tags': meta.get('tags', []),
        'models': meta.get('models', []),
        'version': meta.get('version', '1.0.0'),
        'path': f'{BASE}/{path}',
        'languages': ['en'],
        'has_ru': has_ru,
    }
    if has_ru:
        entry['languages'].append('ru')
    
    skills_index[name] = entry

# Parse RU skills separately
for ru_path in sorted(glob.glob(f'{BASE}/**/SKILL.ru.md', recursive=True)):
    meta = parse_frontmatter(ru_path)
    if 'name' not in meta:
        continue
    path = ru_path.replace('\\', '/').replace(f'{BASE}/', '').replace('/SKILL.ru.md', '')
    ru_skills.append({
        'name': meta['name'],
        'description': meta.get('description', ''),
        'category': meta.get('category', 'qa'),
        'tags': meta.get('tags', []),
        'original': meta.get('original', meta['name']),
        'path': f'{BASE}/{path}',
    })

skills_list = sorted(skills_index.values(), key=lambda x: x['name'])
domains = sorted(set(s['category'] for s in skills_list))

now = dt.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
data = {
    'metadata': {
        'schema_version': '3.0',
        'generated_at': now,
        'total_skills': len(skills_list),
        'total_ru': len(ru_skills),
        'domains': domains,
        'bilingual': True,
    },
    'skills': skills_list,
}

with open('skills_catalog.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Catalog updated: {len(skills_list)} EN skills, {len(ru_skills)} RU skills")
print(f"Domains: {len(domains)} — {', '.join(domains)}")
print(f"Bilingual: YES — {len([s for s in skills_list if s['has_ru']])} skills have RU translation")
