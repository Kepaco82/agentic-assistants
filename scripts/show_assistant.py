import sys
from pathlib import Path


def parse_simple_yaml(file_path: Path) -> dict[str, str]:
    metadata = {}

    for line in file_path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()

        if not stripped or stripped.startswith("#"):
            continue

        if ":" not in stripped:
            continue

        key, value = stripped.split(":", 1)
        metadata[key.strip()] = value.strip()

    return metadata


def main():
    if len(sys.argv) != 2:
        print("Usage: python scripts/show_assistant.py <assistant-name>")
        raise SystemExit(1)

    assistant_name = sys.argv[1]
    assistant_path = Path("assistants") / assistant_name
    metadata_path = assistant_path / "assistant.yaml"

    if not assistant_path.exists():
        print(f"Error: Assistant '{assistant_name}' does not exist.")
        raise SystemExit(1)

    if not metadata_path.exists():
        print(f"Error: Assistant '{assistant_name}' has no assistant.yaml file.")
        raise SystemExit(1)

    metadata = parse_simple_yaml(metadata_path)

    print(metadata.get("name", assistant_name.title()))
    print("=" * len(metadata.get("name", assistant_name.title())))
    print(f"ID: {metadata.get('id', 'Unknown')}")
    print(f"Version: {metadata.get('version', 'Unknown')}")
    print(f"Category: {metadata.get('category', 'Unknown')}")
    print(f"Status: {metadata.get('status', 'Unknown')}")
    print(f"Owner: {metadata.get('owner', 'Unknown')}")


if __name__ == "__main__":
    main()