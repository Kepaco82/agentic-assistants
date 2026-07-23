import subprocess
import sys


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "scripts/agentic.py", *args],
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
    assert "exported assistant" in result.stdout.lower()