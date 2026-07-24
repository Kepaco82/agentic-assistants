from pathlib import Path
from typing import Any

from assistant_registry import load_assistant


PROMPT_FILES = [
    "persona.md",
    "scope.md",
    "workflow.md",
    "deliverables.md",
    "quality.md",
    "handoffs.md",
]


def resolve_assistant_chain(
    assistant_id: str,
    resolved: list[str] | None = None,
    active: list[str] | None = None,
) -> list[str]:
    """
    Return assistant IDs in inheritance order.

    Parent assistants are returned before child assistants.
    Circular inheritance raises ValueError.
    """
    if resolved is None:
        resolved = []

    if active is None:
        active = []

    if assistant_id in active:
        cycle = " -> ".join(active + [assistant_id])
        raise ValueError(f"Circular assistant inheritance detected: {cycle}")

    if assistant_id in resolved:
        return resolved

    assistant = load_assistant(assistant_id)

    if not assistant:
        raise ValueError(f"Assistant not found: {assistant_id}")

    active.append(assistant_id)

    parents = assistant.get("extends", [])

    if isinstance(parents, str):
        parents = [parents]

    for parent_id in parents:
        resolve_assistant_chain(
            assistant_id=parent_id,
            resolved=resolved,
            active=active,
        )

    active.pop()
    resolved.append(assistant_id)

    return resolved


def load_resolved_assistant(assistant_id: str) -> dict[str, Any]:
    """
    Load an assistant and resolve its inherited assistants.

    Returns:
        {
            "id": str,
            "metadata": dict,
            "chain": list[str],
            "sections": list[dict],
        }
    """
    chain = resolve_assistant_chain(assistant_id)

    metadata = load_assistant(assistant_id)

    if not metadata:
        raise ValueError(f"Assistant not found: {assistant_id}")

    sections: list[dict[str, str]] = []

    for current_id in chain:
        assistant_path = Path("assistants") / current_id

        for filename in PROMPT_FILES:
            file_path = assistant_path / filename

            if not file_path.exists():
                continue

            content = file_path.read_text(encoding="utf-8").strip()

            if not content:
                continue

            sections.append(
                {
                    "assistant_id": current_id,
                    "filename": filename,
                    "content": content,
                }
            )

    return {
        "id": assistant_id,
        "metadata": metadata,
        "chain": chain,
        "sections": sections,
    }