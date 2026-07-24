from pathlib import Path
from typing import Any


ASSISTANTS_DIR = Path("assistants")


def parse_simple_yaml(file_path: Path) -> dict[str, Any]:
    metadata: dict[str, Any] = {}
    current_list_key: str | None = None

    for line in file_path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()

        if not stripped or stripped.startswith("#"):
            continue

        if stripped.startswith("- ") and current_list_key:
            metadata[current_list_key].append(stripped[2:].strip())
            continue

        if ":" not in stripped:
            continue

        key, value = stripped.split(":", 1)
        key = key.strip()
        value = value.strip()

        if value:
            metadata[key] = value
            current_list_key = None
        else:
            metadata[key] = []
            current_list_key = key

    return metadata


def load_assistant(assistant_id: str) -> dict[str, Any] | None:
    assistant_path = ASSISTANTS_DIR / assistant_id
    metadata_path = assistant_path / "assistant.yaml"

    if not assistant_path.is_dir():
        return None

    if not metadata_path.exists():
        return None

    metadata = parse_simple_yaml(metadata_path)
    metadata["path"] = str(assistant_path)

    return metadata


def list_assistants() -> list[dict[str, Any]]:
    assistants: list[dict[str, Any]] = []

    if not ASSISTANTS_DIR.exists():
        return assistants

    for assistant_path in sorted(ASSISTANTS_DIR.iterdir()):
        if not assistant_path.is_dir():
            continue

        metadata = load_assistant(assistant_path.name)

        if metadata is not None:
            assistants.append(metadata)

    return assistants


def build_registry() -> dict[str, dict[str, Any]]:
    """
    Build a central registry of all assistants.

    Each registry entry includes resolved metadata, inheritance chain,
    prompt sections, and the assistant path.
    """
    from assistant_loader import load_resolved_assistant

    registry: dict[str, dict[str, Any]] = {}

    for assistant in list_assistants():
        assistant_id = assistant.get("id")

        if not isinstance(assistant_id, str) or not assistant_id:
            continue

        resolved = load_resolved_assistant(assistant_id)

        registry[assistant_id] = {
            "id": assistant_id,
            "metadata": resolved["metadata"],
            "chain": resolved["chain"],
            "sections": resolved["sections"],
            "path": assistant.get("path"),
        }

    return registry


def get_registry_entry(
    assistant_id: str,
    registry: dict[str, dict[str, Any]] | None = None,
) -> dict[str, Any] | None:
    """
    Return one assistant from the central registry.
    """
    if registry is None:
        registry = build_registry()

    return registry.get(assistant_id)