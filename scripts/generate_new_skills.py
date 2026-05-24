#!/usr/bin/env python3
"""
Generate new Claude Skills based on templates.

Usage:
  python3 generate_new_skills.py --domain data-engineering --count 150
  python3 generate_new_skills.py --domains "backend,frontend" --count 300
"""

import json
import sys
import argparse
from datetime import datetime

SKILL_TEMPLATES = {
    "data-engineering": [
        {"tool": "spark", "ops": ["partitioning", "caching", "memory-tuning", "shuffle-optimization"]},
        {"tool": "airflow", "ops": ["dag-design", "sensors", "dynamic-tasks", "backfill"]},
        {"tool": "dbt", "ops": ["testing", "documentation", "lineage", "deployment"]},
        {"tool": "kafka", "ops": ["partitioning", "consumer-groups", "schema-registry", "monitoring"]},
        {"tool": "delta-lake", "ops": ["schema-evolution", "time-travel", "optimization", "partitioning"]},
        {"tool": "feature-store", "ops": ["design", "engineering", "versioning", "lineage"]},
    ],
    "observability": [
        {"tool": "jaeger", "ops": ["setup", "sampling", "instrumentation", "analysis"]},
        {"tool": "prometheus", "ops": ["scrape-config", "custom-metrics", "alerting", "tuning"]},
        {"tool": "grafana", "ops": ["dashboard-design", "templating", "alerting", "data-source"]},
        {"tool": "elk", "ops": ["indexing", "retention", "parsing", "performance"]},
        {"tool": "loki", "ops": ["label-strategy", "tenancy", "retention", "scaling"]},
        {"tool": "apm", "ops": ["instrumentation", "sampling", "dashboards", "baselines"]},
    ],
    "mlops": [
        {"tool": "mlflow", "ops": ["model-registry", "experiment-tracking", "deployment", "versioning"]},
        {"tool": "feast", "ops": ["feature-store-design", "offline-store", "online-store", "freshness"]},
        {"tool": "kserve", "ops": ["deployment", "traffic-splitting", "canary", "inference"]},
        {"tool": "bentoml", "ops": ["model-serving", "api-design", "containerization", "optimization"]},
        {"tool": "model-monitoring", "ops": ["drift-detection", "performance-tracking", "retraining", "alerts"]},
    ],
    "prompting": [
        {"concept": "few-shot", "ops": ["optimization", "example-selection", "format-consistency"]},
        {"concept": "chain-of-thought", "ops": ["design", "step-by-step", "verification", "complex-tasks"]},
        {"concept": "rag", "ops": ["pipeline-design", "chunking", "embedding", "retrieval", "reranking"]},
        {"concept": "structured-output", "ops": ["json-schema", "xml-parsing", "validation", "constraints"]},
        {"concept": "fine-tuning", "ops": ["dataset-prep", "lora", "instruction-tuning", "evaluation"]},
    ],
    "security": [
        {"tool": "threat-modeling", "ops": ["stride", "attack-trees", "risk-assessment", "mitigation"]},
        {"tool": "sast", "ops": ["tool-integration", "scanning", "remediation", "ci-cd"]},
        {"tool": "secrets-mgmt", "ops": ["vault-setup", "rotation", "access-policies", "audit"]},
        {"tool": "supply-chain", "ops": ["sbom-generation", "dependency-scanning", "artifact-signing", "provenance"]},
        {"tool": "api-security", "ops": ["rate-limiting", "token-mgmt", "authentication", "authorization"]},
    ],
    "backend": [
        {"framework": "fastapi", "ops": ["routing", "middleware", "dependency-injection", "validation"]},
        {"framework": "django", "ops": ["models", "views", "serializers", "authentication"]},
        {"framework": "express", "ops": ["routing", "middleware", "error-handling", "validation"]},
        {"framework": "spring-boot", "ops": ["rest-controllers", "dependency-injection", "jpa", "security"]},
    ],
}

def generate_skill(template, index):
    """Generate a single skill from template"""
    
    if 'tool' in template:
        tool = template['tool']
        op = template['ops'][index % len(template['ops'])]
        name = f"{template.get('domain', 'backend')}-{tool}-{op}".replace('_', '-')
        description = f"Implements {op.replace('-', ' ')} with {tool.capitalize()}. Handles key aspects and best practices. Use for optimized {tool.replace('-', ' ')} workflows."
        tags = [tool, op, "optimization", "production-ready"]
    else:
        concept = template.get('concept', 'prompting')
        op = template['ops'][index % len(template['ops'])]
        name = f"prompting-{concept}-{op}".replace('_', '-')
        description = f"Implements {op.replace('-', ' ')} using {concept.replace('-', ' ')} technique. Improves Claude's reasoning and accuracy. Use for complex problem-solving."
        tags = [concept, op, "prompting", "claude"]
    
    return {
        "name": name,
        "description": description,
        "category": template.get('domain') or template.get('category', 'backend'),
        "tags": "[" + ", ".join(tags) + "]",
        "models": "[claude-opus, claude-3-5-sonnet]",
        "version": "2.0.0",
        "path": f".claude/skills/{template.get('domain', 'backend')}/{name}"
    }

def main():
    parser = argparse.ArgumentParser(description='Generate new Claude Skills')
    parser.add_argument('--domain', type=str, help='Single domain')
    parser.add_argument('--domains', type=str, help='Multiple domains (comma-separated)')
    parser.add_argument('--count', type=int, default=150, help='Number of skills to generate')
    parser.add_argument('--output', type=str, default='new_skills.json', help='Output filename')
    
    args = parser.parse_args()
    
    domains = []
    if args.domain:
        domains = [args.domain]
    elif args.domains:
        domains = [d.strip() for d in args.domains.split(',')]
    else:
        print("Error: Specify --domain or --domains")
        sys.exit(1)
    
    # Collect templates for requested domains
    templates = []
    for domain in domains:
        if domain in SKILL_TEMPLATES:
            templates.extend(SKILL_TEMPLATES[domain])
        else:
            print(f"Warning: Domain '{domain}' not found in templates")
    
    if not templates:
        print("Error: No templates found for requested domains")
        sys.exit(1)
    
    # Generate skills
    print(f"Generating {args.count} skills for {', '.join(domains)}...")
    skills = []
    for i in range(args.count):
        template = templates[i % len(templates)]
        skill = generate_skill(template, i)
        skills.append(skill)
    
    # Write output
    output = {
        "metadata": {
            "generated_at": datetime.now().isoformat(),
            "count": len(skills),
            "domains": domains
        },
        "skills": skills
    }
    
    with open(args.output, 'w') as f:
        json.dump(output, f, indent=2)
    
    print(f"✅ Generated {len(skills)} skills")
    print(f"✅ Wrote {args.output}")

if __name__ == '__main__':
    main()
