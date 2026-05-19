import os, json, sys, glob

errors = []
warnings = []
counts = {'ok': 0, 'error': 0}

for sk_path in sorted(glob.glob('.claude/skills/**/SKILL.md', recursive=True)):
    name = os.path.basename(os.path.dirname(sk_path))
    with open(sk_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if not content.startswith('---'):
        errors.append(f'{sk_path}: Missing opening frontmatter ---')
        counts['error'] += 1
        continue
    
    lines = content.split('\n')
    front_lines = []
    body_lines = []
    found_first = False
    found_second = False
    for line in lines:
        if line.strip() == '---' and not found_first:
            found_first = True; continue
        if line.strip() == '---' and found_first and not found_second:
            found_second = True; continue
        if not found_second:
            front_lines.append(line)
        else:
            body_lines.append(line)
    
    if not found_second:
        errors.append(f'{sk_path}: Malformed frontmatter')
        counts['error'] += 1
        continue
    
    front = '\n'.join(front_lines).strip()
    body = '\n'.join(body_lines).strip()
    
    fields = {}
    for line in front.split('\n'):
        if ':' in line:
            key, _, val = line.partition(':')
            fields[key.strip()] = val.strip()
    
    required = ['name', 'description', 'category', 'tags', 'models', 'version']
    missing = [f for f in required if f not in fields]
    if missing:
        errors.append(f'{sk_path}: Missing fields: {missing}')
        counts['error'] += 1
        continue
    
    dir_name = os.path.basename(os.path.dirname(sk_path))
    if dir_name != fields['name']:
        warnings.append(f'{sk_path}: Dir "{dir_name}" != name "{fields["name"]}"')
    
    cat_path = sk_path.replace('\\', '/').split('/')[2]
    cat_fm = fields.get('category', '')
    path_parts = sk_path.replace('\\', '/').split('/')
    if len(path_parts) >= 4 and path_parts[2] != cat_fm:
        warnings.append(f'{sk_path}: Path category "{path_parts[2]}" != frontmatter "{cat_fm}"')
    
    if len(body) < 50:
        warnings.append(f'{sk_path}: Body too short ({len(body)} chars)')
    
    # Validate tags: name, version, models are strings
    for key in ('tags', 'models'):
        val = fields.get(key, '')
        if not (val.startswith('[') and val.endswith(']')):
            errors.append(f'{sk_path}: {key} should be [list] format')
            counts['error'] += 1
            continue
    
    counts['ok'] += 1

print(f'=== Validation ===')
print(f'OK: {counts["ok"]}, Errors: {counts["error"]}, Warnings: {len(warnings)}')

if warnings:
    print(f'\nWarnings:')
    for w in warnings:
        print(f'  {w}')

if errors:
    print(f'\nERRORS:')
    for e in errors:
        print(f'  {e}')
    sys.exit(1)
else:
    print('\nAll files valid!')
