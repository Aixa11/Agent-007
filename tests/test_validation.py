from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent


def test_python_validation_passes():
    result = subprocess.run(
        [sys.executable, str(ROOT / "validation" / "validate.py")],
        capture_output=True,
        text=True,
        cwd=ROOT,
        check=False,
    )
    assert result.returncode == 0, result.stdout + "\n" + result.stderr


def test_schema_file_exists():
    schema = ROOT / "validation" / "schema" / "finding.schema.json"
    assert schema.exists()


def test_validation_report_generator_runs():
    result = subprocess.run(
        [sys.executable, str(ROOT / "validation" / "report-generator.py")],
        capture_output=True,
        text=True,
        cwd=ROOT,
        check=False,
    )
    assert result.returncode == 0, result.stdout + "\n" + result.stderr
    assert (ROOT / "validation" / "audit-report.json").exists()