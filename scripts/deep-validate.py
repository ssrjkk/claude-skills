import os, sys, glob, re

errors = []
warnings = []
total = 0

EMOJI_SECTIONS = ['🚀 Quick Start', '📋 When to Use', '🔧 Step-by-Step', '📦 Dependencies', '🧪 Examples', '🔗 Resources', '✅ Validation']
PLAIN_SECTIONS = ['Quick Start', 'When to Use', 'Validation']

for sk_path in sorted(glob.glob('.claude/skills/**/SKILL.md', recursive=True)):
    total += 1
    name = os.path.basename(os.path.dirname(sk_path))
    with open(sk_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Parse frontmatter (first two --- only)
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
        errors.append(f'{name}: Malformed frontmatter')
        continue
    
    body = '\n'.join(body_lines).strip()
    
    # Check required sections (plain or emoji variants)
    has_plain = all(s in body for s in PLAIN_SECTIONS)
    has_emoji = all(s in body for s in EMOJI_SECTIONS)
    if not has_plain and not has_emoji:
        missing = [s for s in PLAIN_SECTIONS if s not in body]
        # Check if they use emoji variants
        still_missing = []
        for s in missing:
            emoji_map = {'Quick Start': '🚀 Quick Start', 'When to Use': '📋 When to Use', 'Validation': '✅ Validation'}
            emoji_v = emoji_map.get(s)
            if emoji_v and emoji_v not in body:
                still_missing.append(f'{s} (or {emoji_v})')
            elif not emoji_v:
                still_missing.append(s)
        if still_missing:
            warnings.append(f'{name}: Missing sections: {still_missing}')
    
    # Check body length
    if len(body) < 80:
        warnings.append(f'{name}: Body very short ({len(body)} chars)')
    
    # Check for broken code fences (count only those on their own line)
    fence_lines = [l for l in body_lines if l.strip().startswith('```')]
    if len(fence_lines) % 2 != 0:
        errors.append(f'{name}: Unbalanced code fences ({len(fence_lines)} fences)')
    
    # Check for template placeholders (only flag TODO/FIXME, not {{ }} which is valid template syntax)
    if 'TODO' in body:
        warnings.append(f'{name}: Contains TODO placeholder')
    
    # Check frontmatter fields
    front = '\n'.join(front_lines)
    for field in ['models:', 'tags:', 'category:']:
        if field not in front:
            errors.append(f'{name}: Missing {field.replace(":", "")} in frontmatter')

print(f'=== Deep Validation Results ===')
print(f'Checked: {total} files')
print(f'Errors: {len(errors)}')
print(f'Warnings: {len(warnings)}')

if warnings:
    print(f'\n--- Warnings ---')
    for w in sorted(warnings):
        print(f'  {w}')

if errors:
    print(f'\n--- ERRORS ---')
    for e in sorted(errors):
        print(f'  {e}')
    sys.exit(1)
else:
    print('\nAll skills pass deep validation!')
