.PHONY: validate test catalog quality clean install install-dev help

help:
	@echo "Claude Skills Library — Makefile"
	@echo "  install       pip install -e . (editable mode)"
	@echo "  install-dev   pip install -e .[dev]"
	@echo "  validate      Full validation pipeline"
	@echo "  quality       Quality analysis report"
	@echo "  audit         Audit top 50 skills (quality check)"
	@echo "  test          Run pytest suite"
	@echo "  catalog       Regenerate skills_catalog.json"
	@echo "  stats         Show library statistics"
	@echo "  docs          Build searchable docs site"
	@echo "  clean         Remove Python cache files"

install:
	pip install -e .

install-dev:
	pip install -e ".[dev]"

validate:
	python -m claude_skills.cli validate --dir .claude/skills
	python -m claude_skills.cli quality --dir .claude/skills

quality:
	python -m claude_skills.cli quality --dir .claude/skills --json docs/api/quality-report.json

audit:
	python scripts/audit_skills.py --dir .claude/skills --top 50 --json docs/api/audit-report.json

test:
	python -m pytest tests/ -v --tb=short --cov=src/claude_skills

catalog:
	python -m claude_skills.cli catalog --output skills_catalog.json

stats:
	python -m claude_skills.cli stats

docs:
	python scripts/build_docs.py --dir .claude/skills --output docs/index.html

clean:
	python -c "import pathlib, shutil; [shutil.rmtree(p) for p in pathlib.Path('.').rglob('__pycache__') if p.is_dir()]"
	python -c "import pathlib; [p.unlink() for p in pathlib.Path('.').rglob('*.pyc') if p.is_file()]"

all: validate audit test catalog docs
	@echo "All checks passed!"
