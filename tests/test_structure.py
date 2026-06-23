from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def test_root_files_exist():
    expected = [
        "README.md",
        "README.en.md",
        "AGENTS.md",
    ]
    for name in expected:
        assert (ROOT / name).exists(), name


def test_core_directories_exist():
    expected = [
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
        "docs",
    ]
    for rel in expected:
        assert (ROOT / rel).exists(), rel


def test_blueprint_modules_exist():
    expected = [
        "README.md",
        "network/README.md",
        "security/README.md",
        "compute/README.md",
        "storage/README.md",
    ]
    base = ROOT / "blueprint" / "modules"
    for rel in expected:
        assert (base / rel).exists(), rel


def test_policy_files_exist():
    expected = [
        "iam-baseline.yaml",
        "logging-baseline.yaml",
        "encryption-baseline.yaml",
    ]
    base = ROOT / "blueprint" / "policies"
    for name in expected:
        assert (base / name).exists(), name


def test_example_contains_input_and_output():
    example = ROOT / "examples" / "oil-pipeline"
    assert (example / "README.md").exists()
    assert (example / "input" / "main.tf").exists()
    assert (example / "output" / "main.tf").exists()