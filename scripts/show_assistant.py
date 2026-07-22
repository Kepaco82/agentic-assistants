import sys

from assistant_registry import load_assistant


def main():
    if len(sys.argv) != 2:
        print("Usage: python scripts/show_assistant.py <assistant-name>")
        raise SystemExit(1)

    assistant_name = sys.argv[1]
    assistant = load_assistant(assistant_name)

    if assistant is None:
        print(
            f"Error: Assistant '{assistant_name}' was not found "
            "or has no valid assistant.yaml file."
        )
        raise SystemExit(1)

    name = assistant.get("name", assistant_name.title())

    print(name)
    print("=" * len(name))
    print(f"ID: {assistant.get('id', 'Unknown')}")
    print(f"Version: {assistant.get('version', 'Unknown')}")
    print(f"Category: {assistant.get('category', 'Unknown')}")
    print(f"Status: {assistant.get('status', 'Unknown')}")
    print(f"Owner: {assistant.get('owner', 'Unknown')}")
    print(f"Description: {assistant.get('description', 'Unknown')}")
    print(f"Entrypoint: {assistant.get('entrypoint', 'Unknown')}")


if __name__ == "__main__":
    main()