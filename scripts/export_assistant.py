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


def build_prompt(assistant_id: str) -> str:
    assistant = load_assistant(assistant_id)

    if not assistant:
        raise ValueError(f"Assistant not found: {assistant_id}")

    assistant_path = Path("assistants") / assistant_id
    sections = []

    sections.append(f"# {assistant.get('name', assistant_id)}")

    description = str(assistant.get("description", "")).strip()

    if description:
        sections.append(description)

    for filename in PROMPT_FILES:
        file_path = assistant_path / filename

        if not file_path.exists():
            continue

        content = file_path.read_text(encoding="utf-8").strip()

        if content:
            sections.append(content)

    return "\n\n".join(sections) + "\n"


def main():
    if len(sys.argv) != 2:
        print("Usage: python scripts/export_assistant.py <assistant-id>")
        raise SystemExit(1)

    assistant_id = sys.argv[1]

    try:
        content = build_prompt(assistant_id)
    except ValueError as error:
        print(error)
        raise SystemExit(1)

    build_path = Path("build")
    build_path.mkdir(exist_ok=True)

    output_path = build_path / f"{assistant_id}.md"
    output_path.write_text(content, encoding="utf-8")

    print(f"Exported assistant: {assistant_id}")
    print(f"Output: {output_path}")


if __name__ == "__main__":
    main()