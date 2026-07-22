from assistant_registry import list_assistants, load_assistant


def main():
    executive = load_assistant("executive")

    if executive is None:
        print("FAIL: Could not load executive assistant.")
        raise SystemExit(1)

    print("Loaded assistant:")
    print(f"Name: {executive.get('name', 'Unknown')}")
    print(f"ID: {executive.get('id', 'Unknown')}")
    print(f"Category: {executive.get('category', 'Unknown')}")

    assistants = list_assistants()

    print(f"\nRegistry total: {len(assistants)}")

    for assistant in assistants:
        print(f"- {assistant.get('name', 'Unknown')}")


if __name__ == "__main__":
    main()