import sys
from pathlib import Path

from scripts.assistant_registry import list_assistants, load_assistant


def generate_assistant_doc(assistant_id: str) -> Path:
    assistant = load_assistant(assistant_id)

    if not assistant:
        raise ValueError(f"Assistant not found: {assistant_id}")

    docs_dir = Path("docs") / "assistants"
    docs_dir.mkdir(parents=True, exist_ok=True)

    output_path = docs_dir / f"{assistant_id}.md"

    content = [
        f"# {assistant.get('name', assistant_id)}",
        "",
        assistant.get("description", ""),
        "",
        "## Metadata",
        "",
        f"- ID: `{assistant.get('id', assistant_id)}`",
        f"- Version: `{assistant.get('version', 'unknown')}`",
        f"- Category: `{assistant.get('category', 'unknown')}`",
        f"- Status: `{assistant.get('status', 'unknown')}`",
        f"- Owner: `{assistant.get('owner', 'unknown')}`",
        f"- Entrypoint: `{assistant.get('entrypoint', 'unknown')}`",
        "",
    ]

    output_path.write_text("\n".join(content), encoding="utf-8")
    return output_path


def main():
    assistants = list_assistants()

    if not assistants:
        print("No assistants found.")
        raise SystemExit(1)

    print("Generating assistant documentation...")

    for assistant in assistants:
        assistant_id = assistant.get("id")

        if not assistant_id:
            print("Assistant metadata is missing an id.")
            raise SystemExit(1)

        try:
            output_path = generate_assistant_doc(assistant_id)
            print(f"Generated: {output_path}")
        except ValueError as error:
            print(error)
            raise SystemExit(1)


if __name__ == "__main__":
    main()