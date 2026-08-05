import assistant_registry

from assistant_service import AssistantService


def main():
    service = AssistantService(assistant_registry)
    assistants = service.list_assistants()

    print("Available Assistants")
    print("====================")

    if not assistants:
        print("No assistants with metadata found.")
        return

    for assistant in assistants:
        name = assistant.get("name", "Unknown")
        category = assistant.get("category", "Unknown")
        version = assistant.get("version", "Unknown")
        status = assistant.get("status", "Unknown")

        print(f"- {name}")
        print(f"  Category: {category}")
        print(f"  Version: {version}")
        print(f"  Status: {status}")

    print(f"\nTotal: {len(assistants)}")


if __name__ == "__main__":
    main()