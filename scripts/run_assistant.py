import sys
from pathlib import Path

from assistant_registry import load_assistant


PROMPT_FILES = [
    "persona.md",
    "scope.md",
    "workflow.md",
    "deliverables.md",
    "quality.md",
    "handoffs.md",
]


def main():
    if len(sys.argv) != 2:
        print("Usage: python scripts/run_assistant.py <assistant-id>")
        raise SystemExit(1)

    assistant_id = sys.argv[1]
    assistant = load_assistant(assistant_id)

    if not assistant:
        print(f"Assistant not found: {assistant_id}")
        raise SystemExit(1)

    assistant_path = Path("assistants") / assistant_id

    print(f"# {assistant.get('name', assistant_id)}")
    print()

    description = assistant.get("description")

    if description:
        print(description)
        print()

    for filename in PROMPT_FILES:
        file_path = assistant_path / filename

        if not file_path.exists():
            continue

        content = file_path.read_text(encoding="utf-8").strip()

        if not content:
            continue

        print(content)
        print()


if __name__ == "__main__":
    main()