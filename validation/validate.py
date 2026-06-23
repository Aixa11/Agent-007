from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

required_files = [
    "AGENTS.md",
    "agent/rules.md",
    "blueprint/docs/architecture.md",
    "README.md",
    "README.en.md",
    "docs/vision.md",
    "docs/scope.md",
    "docs/roadmap.md",
    "validation/schema/finding.schema.json",
    "examples/oil-pipeline/README.md",
]

required_dirs = [
    "agent",
    "agent/prompts",
    "agent/workflows",
    "blueprint",
    "blueprint/docs",
    "blueprint/modules",
    "blueprint/policies",
    "validation",
    "validation/schema",
    "examples",
    "examples/oil-pipeline",
    "tests",
]

required_prompt_files = [
    "agent/prompts/analyze_infra.md",
    "agent/prompts/improve_incrementally.md",
    "agent/prompts/validate_changes.md",
    "agent/prompts/security_review.md",
    "agent/prompts/architecture_summary.md",
]

required_workflow_files = [
    "agent/workflows/analyze.md",
    "agent/workflows/propose.md",
    "agent/workflows/validate.md",
    "agent/workflows/publish.md",
]

required_module_files = [
    "blueprint/modules/README.md",
    "blueprint/modules/network/README.md",
    "blueprint/modules/security/README.md",
    "blueprint/modules/compute/README.md",
    "blueprint/modules/storage/README.md",
]

required_policy_files = [
    "blueprint/policies/iam-baseline.yaml",
    "blueprint/policies/logging-baseline.yaml",
    "blueprint/policies/encryption-baseline.yaml",
]

issues = []

for rel in required_files:
    if not (ROOT / rel).exists():
        issues.append(f"Missing required file: {rel}")

for rel in required_dirs:
    if not (ROOT / rel).exists():
        issues.append(f"Missing required directory: {rel}")

for rel in required_prompt_files:
    if not (ROOT / rel).exists():
        issues.append(f"Missing prompt file: {rel}")

for rel in required_workflow_files:
    if not (ROOT / rel).exists():
        issues.append(f"Missing workflow file: {rel}")

for rel in required_module_files:
    if not (ROOT / rel).exists():
        issues.append(f"Missing blueprint module file: {rel}")

for rel in required_policy_files:
    if not (ROOT / rel).exists():
        issues.append(f"Missing policy file: {rel}")

tests_dir = ROOT / "tests"
if tests_dir.exists() and not any(tests_dir.iterdir()):
    issues.append("The tests directory exists but does not contain any files.")

agents = ROOT / "AGENTS.md"
if agents.exists():
    content = agents.read_text(encoding="utf-8")
    if "Commands" not in content:
        issues.append("AGENTS.md should include a Commands section.")
    if "Boundaries" not in content:
        issues.append("AGENTS.md should include a Boundaries section.")

rules = ROOT / "agent/rules.md"
if rules.exists():
    content = rules.read_text(encoding="utf-8")
    if "Incremental evolution" not in content:
        issues.append("agent/rules.md should include incremental evolution guidance.")
    if "Data sovereignty" not in content:
        issues.append("agent/rules.md should include data sovereignty guidance.")

if issues:
    print("Validation failed:")
    for issue in issues:
        print(f"- {issue}")
    raise SystemExit(1)

print("Validation passed.")