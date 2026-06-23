from datetime import datetime, timezone
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "validation" / "audit-report.json"

def load_status() -> dict:
    status = {
        "project": "Secure Architect Agent",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "status": "ok",
        "checks": [],
    }

    checks = [
        ("AGENTS.md", (ROOT / "AGENTS.md").exists()),
        ("agent/rules.md", (ROOT / "agent/rules.md").exists()),
        ("blueprint/docs/architecture.md", (ROOT / "blueprint/docs/architecture.md").exists()),
        ("validation/schema/finding.schema.json", (ROOT / "validation/schema/finding.schema.json").exists()),
        ("examples/oil-pipeline/README.md", (ROOT / "examples/oil-pipeline/README.md").exists()),
    ]

    for name, passed in checks:
        status["checks"].append(
            {
                "name": name,
                "passed": passed,
            }
        )
        if not passed:
            status["status"] = "fail"

    return status

def main() -> int:
    report = load_status()
    OUTPUT.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"Wrote {OUTPUT}")
    return 0 if report["status"] == "ok" else 1

if __name__ == "__main__":
    raise SystemExit(main())