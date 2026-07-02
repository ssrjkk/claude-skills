#!/usr/bin/env python3
"""Test skill examples for validity.

This is a placeholder pytest suite. Add actual example
tests based on your skill types.
"""

import json


def load_skills():
    """Load skills from library."""
    with open('skills_library.json', 'r') as f:
        data = json.load(f)
    return data.get('skills', []) + data.get('extended_skills', [])


def test_examples_exist():
    """Test that skills have examples."""
    skills = load_skills()
    skills_without_examples = [
        s for s in skills
        if not s.get('examples') or len(s.get('examples', [])) == 0
    ]
    assert len(skills_without_examples) == 0, \
        f"{len(skills_without_examples)} skills missing examples"


def test_examples_have_output():
    """Test that examples have expected output."""
    skills = load_skills()
    invalid = []
    for skill in skills:
        for i, ex in enumerate(skill.get('examples', [])):
            if 'output' not in ex:
                invalid.append((skill.get('id'), i))
    assert len(invalid) == 0, f"{len(invalid)} examples missing output field"


def test_skills_json_valid():
    """Test that skills_library.json is valid JSON."""
    with open('skills_library.json', 'r') as f:
        data = json.load(f)
    assert 'skills' in data, "Missing 'skills' key"
    assert isinstance(data['skills'], list), "'skills' must be a list"


if __name__ == '__main__':
    import pytest
    pytest.main([__file__, '-v'])
