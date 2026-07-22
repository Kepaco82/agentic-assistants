from pathlib import Path
import sys


REQUIRED_FILES = [
    "README.md",
    "persona.md",
    "scope.md",
    "workflow.md",
    "deliverables.md",
    "quality.md",
    "handoffs.md",
    "version.md",
]


def main():
    if len(sys.argv) != 2:
        print("Usage: python scripts/create_assistant.py <assistant-name>")
        sys.exit(1)

    assistant_name = sys.argv[1]
    assistant_path = Path("assistants") / assistant_name

    if assistant_path.exists():
        print(f"Error: Assistant '{assistant_name}' already exists.")
        sys.exit(1)

    assistant_path.mkdir(parents=True)

    for filename in REQUIRED_FILES:
        file_path = assistant_path / filename

        if not file_path.exists():
            file_path.write_text(f"# {filename.replace('.md', '')}\n")

    print(f"Created assistant: {assistant_name}")


if __name__ == "__main__":
    main()