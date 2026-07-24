import sys

from assistant_loader import load_resolved_assistant


def main():
    if len(sys.argv) != 2:
        print("Usage: python scripts/run_assistant.py <assistant-id>")
        raise SystemExit(1)

    assistant_id = sys.argv[1]

    try:
        resolved = load_resolved_assistant(assistant_id)
    except ValueError as error:
        print(error)
        raise SystemExit(1)

    metadata = resolved["metadata"]

    print(f"# {metadata.get('name', assistant_id)}")
    print()

    description = metadata.get("description")

    if description:
        print(description)
        print()

    for section in resolved["sections"]:
        print(section["content"])
        print()


if __name__ == "__main__":
    main()