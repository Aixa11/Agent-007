from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def test_agents_contains_required_sections():
    content = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    assert "Purpose" in content
    assert "Commands" in content
    assert "Boundaries" in content
    assert "Git workflow" in content


def test_rules_contain_core_principles():
    content = (ROOT / "agent" / "rules.md").read_text(encoding="utf-8")
    assert "Security by default" in content
    assert "Incremental evolution" in content
    assert "Data sovereignty" in content
    assert "Mandatory validation" in content
    assert "Historical compatibility" in content


def test_prompts_exist():
    prompt_dir = ROOT / "agent" / "prompts"
    expected = [
        "analyze_infra.md",
        "improve_incrementally.md",
        "validate_changes.md",
        "security_review.md",
        "architecture_summary.md",
    ]
    for name in expected:
        assert (prompt_dir / name).exists(), name


def test_workflows_exist():
    workflow_dir = ROOT / "agent" / "workflows"
    expected = [
        "analyze.md",
        "propose.md",
        "validate.md",
        "publish.md",
    ]
    for name in expected:
        assert (workflow_dir / name).exists(), name