from __future__ import annotations

import time
from pathlib import Path
import argparse

from claude_skills.validator import ValidationPipeline


def cmd_validate(args: argparse.Namespace) -> int:
    skills_dir = Path(args.dir)
    pipeline = ValidationPipeline(skills_dir)

    start = time.time()
    results = pipeline.run_all()
    elapsed = time.time() - start

    report = pipeline.report(results)

    print(f"\nValidation complete: {report['total']} files in {elapsed:.2f}s")
    print(f"  Errors:   {report['errors']}")
    print(f"  Warnings: {report['warnings']}")
    print(f"  Info:     {report['info']}")

    if report["error_details"]:
        print("\nErrors:")
        for e in report["error_details"][:15]:
            print(f"  {e}")
    if report["warning_details"]:
        print("\nWarnings (first 15):")
        for w in report["warning_details"][:15]:
            print(f"  {w}")

    if getattr(args, "strict", False) and report["warnings"] > 0:
        return 1

    return 1 if report["errors"] > 0 else 0
