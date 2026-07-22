from pathlib import Path

REQUIRED_FILES = [
    "README.md",
    "persona.md",
    "scope.md",
    "workflow.md",
    "deliverables.md",
    "quality.md",
    "handoffs.md",
    "version.md",
    "assistant.yaml",
]

CANONICAL_ASSISTANTS = [
    "executive",
    "engineering",
    "product",
]


def main():
    assistants_path = Path("assistants")

    print("Agentic Assistants Validation")
    print("=============================")

    failed = False

    for assistant_name in CANONICAL_ASSISTANTS:
        assistant_path = assistants_path / assistant_name

        if not assistant_path.exists():
            failed = True
            print(f"FAIL: {assistant_name}")
            print("  Missing assistant directory")
            continue

        missing_files = []

        for filename in REQUIRED_FILES:
            if not (assistant_path / filename).exists():
                missing_files.append(filename)

        if missing_files:
            failed = True
            print(f"FAIL: {assistant_name}")
            for filename in missing_files:
                print(f"  Missing: {filename}")
        else:
            print(f"PASS: {assistant_name}")

    print()

    if failed:
        print("Validation failed.")
        raise SystemExit(1)

    print("All assistants passed validation.")


if __name__ == "__main__":
    main()