.PHONY: validate test clean catalog

# Validate all skills
validate:
	python scripts/validate-all.py
	python scripts/deep-validate.py

# Run tests
test:
	pytest scripts/test_examples.py -v

# Regenerate catalog from SKILL.md files
catalog:
	python scripts/generate-catalog.py

# Clean Python cache
clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true

# Full validation pipeline
all: validate test catalog
	@echo "All checks passed!"
