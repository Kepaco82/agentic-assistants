"""Validate the file structure of canonical assistants."""

from pathlib import Path
import sys


REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
ASSISTANTS_DIRECTORY = REPOSITORY_ROOT / "assistants"

CANONICAL_ASSISTANTS = (
    "executive",
    "engineering",
    "product",
)

REQUIRED_FILES = (
    "README.md",
    "persona.md",
    "scope.md",
    "workflow.md",
    "deliverables.md",
    "quality.md",
    "handoffs.md",
    "version.md",
)


def validate_assistant(assistant_name: str) -> list[str]:
    """Return a list of validation errors for one assistant."""

    assistant_directory = ASSISTANTS_DIRECTORY / assistant_name
    errors: list[str] = []

    if not assistant_directory.is_dir():
        return [f"Missing assistant directory: {assistant_directory}"]

    for filename in REQUIRED_FILES:
        file_path = assistant_directory / filename

        if not file_path.is_file():
            errors.append(
                f"{assistant_name}: missing required file '{filename}'"
            )

    return errors


def main() -> int:
    """Run repository structure validation."""

    all_errors: list[str] = []

    print("Checking canonical assistant structure...\n")

    for assistant_name in CANONICAL_ASSISTANTS:
        errors = validate_assistant(assistant_name)

        if errors:
            print(f"FAIL: {assistant_name}")
            all_errors.extend(errors)
        else:
            print(f"PASS: {assistant_name}")

    if all_errors:
        print("\nValidation failed:\n")

        for error in all_errors:
            print(f"- {error}")

        return 1

    print("\nAll canonical assistants have the required structure.")
    return 0


if __name__ == "__main__":
    sys.exit(main())