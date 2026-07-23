from pathlib import Path

from assistant_registry import parse_simple_yaml


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

REQUIRED_METADATA_FIELDS = [
    "id",
    "name",
    "version",
    "category",
    "status",
    "owner",
    "description",
    "entrypoint",
]

CANONICAL_ASSISTANTS = [
    "executive",
    "engineering",
    "product",
]


def validate_metadata(
    assistant_name: str,
    assistant_path: Path,
) -> list[str]:
    errors = []
    metadata_path = assistant_path / "assistant.yaml"

    try:
        metadata = parse_simple_yaml(metadata_path)
    except Exception as error:
        return [f"Unable to read assistant.yaml: {error}"]

    for field in REQUIRED_METADATA_FIELDS:
        value = metadata.get(field)

        if value is None or str(value).strip() == "":
            errors.append(f"Missing metadata field: {field}")

    metadata_id = str(metadata.get("id", "")).strip()

    if metadata_id and metadata_id != assistant_name:
        errors.append(
            f"Metadata id '{metadata_id}' does not match folder "
            f"name '{assistant_name}'"
        )

    entrypoint = str(metadata.get("entrypoint", "")).strip()

    if entrypoint and not (assistant_path / entrypoint).exists():
        errors.append(f"Entrypoint does not exist: {entrypoint}")

    return errors


def main():
    assistants_path = Path("assistants")

    print("Agentic Assistants Validation")
    print("=============================")

    failed = False

    for assistant_name in CANONICAL_ASSISTANTS:
        assistant_path = assistants_path / assistant_name
        errors = []

        if not assistant_path.exists():
            errors.append("Missing assistant directory")
        else:
            for filename in REQUIRED_FILES:
                file_path = assistant_path / filename

                if not file_path.exists():
                    errors.append(f"Missing file: {filename}")
                elif file_path.stat().st_size == 0:
                    errors.append(f"Empty file: {filename}")

            if (assistant_path / "assistant.yaml").exists():
                errors.extend(
                    validate_metadata(
                        assistant_name,
                        assistant_path,
                    )
                )

        if errors:
            failed = True
            print(f"FAIL: {assistant_name}")

            for error in errors:
                print(f"  {error}")
        else:
            print(f"PASS: {assistant_name}")

    print()

    if failed:
        print("Validation failed.")
        raise SystemExit(1)

    print("All assistants passed validation.")


if __name__ == "__main__":
    main()