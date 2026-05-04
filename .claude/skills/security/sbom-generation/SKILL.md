---
name: sbom-generation
description: Generates Software Bill of Materials (SBOM) for tracking dependencies and vulnerabilities. Use for supply chain security.
category: security
tags: [sbom, supply-chain, security, dependencies]
models: [sonnet, opus]
version: 1.0.0
created: 2026-04-29
---
# SBOM Generation

> Generate Software Bill of Materials for component tracking.

## Quick Start
```bash
# Generate SBOM with Syft
syft dir:. -o cyclonedx-json=sbom.json

# Check SBOM
cat sbom.json | jq '.components[] | .name'
```

## When to Use
- ✅ Supply chain security
- ✅ Compliance requirements (US Executive Order)
- ❌ Not as replacement for dependency scanning

## Step-by-Step Instructions
1. Install Syft or Anchore
2. Generate SBOM for project/image
3. Check structure (CycloneDX, SPDX)
4. Integrate into CI/CD

## Dependencies
```bash
brew install syft
# or
curl -sSfL https://raw.githubusercontent.com/anchore/syft/main/install.sh | sh -s -- -b /usr/local/bin
```

## Examples
Input: `syft dir:.` → Output: JSON with all dependencies list

## Resources
- [SBOM Guide](https://www.cisa.gov/sbom)
- [Examples](./examples/)

## Validation
1. SBOM contains all direct and transitive dependencies
2. Format complies with CycloneDX/SPDX
3. SBOM successfully parsed by tools
