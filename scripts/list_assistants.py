from pathlib import Path


def format_name(folder_name: str) -> str:
    return folder_name.replace("-", " ").title()


def main():
    assistants_path = Path("assistants")

    if not assistants_path.exists():
        print("Error: assistants directory not found.")
        raise SystemExit(1)

    assistant_names = sorted(
        path.name
        for path in assistants_path.iterdir()
        if path.is_dir()
    )

    print("Available Assistants")
    print("====================")

    if not assistant_names:
        print("No assistants found.")
        return

    for assistant_name in assistant_names:
        print(f"- {format_name(assistant_name)}")

    print(f"\nTotal: {len(assistant_names)}")


if __name__ == "__main__":
    main()