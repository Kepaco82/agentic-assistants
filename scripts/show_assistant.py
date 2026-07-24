import sys
from typing import Any

from assistant_loader import load_resolved_assistant


LIST_FIELDS = [
    "extends",
    "capabilities",
    "tags",
    "inputs",
    "outputs",
    "dependencies",
]


def print_list_field(label: str, value: Any) -> None:
    print(f"{label}:")

    if not value:
        print("  None")
        return

    if isinstance(value, str):
        value = [value]

    for item in value:
        print(f"  - {item}")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python scripts/show_assistant.py <assistant-name>")
        raise SystemExit(1)

    assistant_name = sys.argv[1]

    try:
        resolved = load_resolved_assistant(assistant_name)
    except ValueError as error:
        print(f"Error: {error}")
        raise SystemExit(1)

    assistant = resolved["metadata"]
    name = assistant.get("name", assistant_name.title())

    print(name)
    print("=" * len(name))
    print(f"ID: {assistant.get('id', 'Unknown')}")
    print(f"Version: {assistant.get('version', 'Unknown')}")
    print(f"Category: {assistant.get('category', 'Unknown')}")
    print(f"Status: {assistant.get('status', 'Unknown')}")
    print(f"Owner: {assistant.get('owner', 'Unknown')}")
    print(f"Description: {assistant.get('description', 'Unknown')}")
    print(f"Visibility: {assistant.get('visibility', 'Unknown')}")
    print(f"Icon: {assistant.get('icon', 'Unknown')}")
    print(f"Color: {assistant.get('color', 'Unknown')}")
    print(f"Entrypoint: {assistant.get('entrypoint', 'Unknown')}")
    print(f"Inheritance Chain: {' -> '.join(resolved['chain'])}")

    for field in LIST_FIELDS:
        label = field.replace("_", " ").title()
        print_list_field(label, assistant.get(field))


if __name__ == "__main__":
    main()