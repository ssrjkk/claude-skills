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

    print(f"Validation complete: {report['total']} files in {elapsed:.2f}s")
    print(f"  Errors:   {report['errors']}")
    print(f"  Warnings: {report['warnings']}")
    print(f"  Info:     {report['info']}")

    if report["error_details"]:
        print("\nErrors:")
        for e in report["error_details"][:10]:
            print(f"  {e}")
    if report["warning_details"]:
        print("\nWarnings (first 10):")
        for w in report["warning_details"][:10]:
            print(f"  {w}")

    return 1 if report["errors"] > 0 else 0
