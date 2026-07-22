from pathlib import Path


ASSISTANTS_DIR = Path("assistants")


def parse_simple_yaml(file_path: Path) -> dict[str, str]:
    metadata: dict[str, str] = {}

    for line in file_path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()

        if not stripped or stripped.startswith("#"):
            continue

        if ":" not in stripped:
            continue

        key, value = stripped.split(":", 1)
        metadata[key.strip()] = value.strip()

    return metadata


def load_assistant(assistant_id: str) -> dict[str, str] | None:
    assistant_path = ASSISTANTS_DIR / assistant_id
    metadata_path = assistant_path / "assistant.yaml"

    if not assistant_path.is_dir():
        return None

    if not metadata_path.exists():
        return None

    metadata = parse_simple_yaml(metadata_path)
    metadata["path"] = str(assistant_path)

    return metadata


def list_assistants() -> list[dict[str, str]]:
    assistants: list[dict[str, str]] = []

    if not ASSISTANTS_DIR.exists():
        return assistants

    for assistant_path in sorted(ASSISTANTS_DIR.iterdir()):
        if not assistant_path.is_dir():
            continue

        metadata = load_assistant(assistant_path.name)

        if metadata is not None:
            assistants.append(metadata)

    return assistants