import json
from collections import defaultdict

with open('skills_catalog.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

by_domain = defaultdict(list)
for s in data['skills']:
    by_domain[s['category']].append(s['name'])

print(f'Total: {data["metadata"]["total_skills"]} skills, {len(by_domain)} domains')
for d in sorted(by_domain):
    print(f'\n  {d} ({len(by_domain[d])}):')
    for n in sorted(by_domain[d]):
        print(f'    - {n}')
