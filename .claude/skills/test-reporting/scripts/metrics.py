import json
from pathlib import Path

def collect_metrics(results_dir):
    metrics = {"total": 0, "passed": 0, "failed": 0}
    for result_file in Path(results_dir).glob("*.json"):
        data = json.loads(result_file.read_text())
        metrics["total"] += 1
        if data["status"] == "passed":
            metrics["passed"] += 1
        else:
            metrics["failed"] += 1
    return metrics
