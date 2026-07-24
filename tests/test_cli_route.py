import subprocess
import sys


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "scripts/agentic.py", *args],
        capture_output=True,
        text=True,
    )


def test_route_command_routes_product_request():
    result = run_cli(
        "route",
        "We need to prioritize our product roadmap.",
    )

    assert result.returncode == 0
    assert "Assistant: product" in result.stdout
    assert "Matched terms:" in result.stdout


def test_route_command_handles_no_match():
    result = run_cli(
        "route",
        "Please rewrite this sentence.",
    )

    assert result.returncode == 0
    assert "No matching assistant found." in result.stdout