import os, json, glob, ast

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

skills = []
for sk_path in sorted(glob.glob('.claude/skills/**/SKILL.md', recursive=True)):
    meta = parse_frontmatter(sk_path)
    if 'name' not in meta:
        continue
    
    path = sk_path.replace('.claude/skills/', '').replace('\\', '/').replace('/SKILL.md', '')
    cat = meta.get('category', 'qa')
    
    skills.append({
        'name': meta['name'],
        'description': meta.get('description', ''),
        'category': cat,
        'tags': meta.get('tags', []),
        'models': meta.get('models', []),
        'version': meta.get('version', '1.0.0'),
        'path': f'.claude/skills/{path}'
    })

data = {
    'metadata': {
        'schema_version': '2.0',
        'generated_at': '2026-05-14T12:00:00Z',
        'total_skills': len(skills),
        'domains': sorted(set(s['category'] for s in skills))
    },
    'skills': skills
}

with open('skills_catalog.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Catalog updated: {len(skills)} skills across {len(data['metadata']['domains'])} domains")
print(f"Domains: {sorted(set(s['category'] for s in skills))}")
