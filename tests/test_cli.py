import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
CLI_PATH = PROJECT_ROOT / "scripts" / "agentic.py"


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(CLI_PATH), *args],
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True,
    )


def test_list_command():
    result = run_cli("list")

    assert result.returncode == 0
    assert "executive" in result.stdout.lower()
    assert "engineering" in result.stdout.lower()
    assert "product" in result.stdout.lower()


def test_show_command():
    result = run_cli("show", "executive")

    assert result.returncode == 0
    assert "executive" in result.stdout.lower()


def test_validate_command():
    result = run_cli("validate")

    assert result.returncode == 0


def test_export_command():
    result = run_cli("export", "executive")

    assert result.returncode == 0
    assert (PROJECT_ROOT / "build" / "executive.md").exists()


def test_docs_command():
    result = run_cli("docs")

    assert result.returncode == 0
    assert "Generating assistant documentation" in result.stdout
    assert (PROJECT_ROOT / "docs" / "assistants" / "executive.md").exists()
    assert (PROJECT_ROOT / "docs" / "assistants" / "engineering.md").exists()
    assert (PROJECT_ROOT / "docs" / "assistants" / "product.md").exists()