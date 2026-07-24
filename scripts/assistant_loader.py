from copy import deepcopy
from pathlib import Path
from typing import Any

try:
    from .assistant_registry import load_assistant
except ImportError:
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
        raise ValueError(
            f"Circular assistant inheritance detected: {cycle}"
        )

    if assistant_id in resolved:
        return resolved

    assistant = load_assistant(assistant_id)

    if not assistant:
        raise ValueError(
            f"Assistant not found: {assistant_id}"
        )

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


def merge_metadata(
    chain: list[str],
) -> dict[str, Any]:
    """
    Merge metadata from parent assistants into the child assistant.

    Rules:
    - Parents are merged first.
    - Child scalar values override parent scalar values.
    - List values are combined without duplicates.
    - Internal path values are not inherited.
    """
    merged: dict[str, Any] = {}

    for current_id in chain:
        metadata = load_assistant(current_id)

        if not metadata:
            raise ValueError(
                f"Assistant not found: {current_id}"
            )

        for key, value in metadata.items():
            if key == "path":
                continue

            if isinstance(value, list):
                existing = merged.get(key, [])

                if not isinstance(existing, list):
                    existing = []

                merged[key] = list(
                    dict.fromkeys(
                        existing + deepcopy(value)
                    )
                )
            else:
                merged[key] = deepcopy(value)

    child_metadata = load_assistant(chain[-1])

    if child_metadata and "path" in child_metadata:
        merged["path"] = child_metadata["path"]

    return merged


def load_resolved_assistant(
    assistant_id: str,
) -> dict[str, Any]:
    """
    Load an assistant and resolve inherited metadata,
    prompt sections, and the final rendered prompt.
    """
    chain = resolve_assistant_chain(assistant_id)
    metadata = merge_metadata(chain)

    sections: list[dict[str, str]] = []

    for current_id in chain:
        assistant_path = (
            Path("assistants") / current_id
        )

        for filename in PROMPT_FILES:
            file_path = assistant_path / filename

            if not file_path.exists():
                continue

            content = file_path.read_text(
                encoding="utf-8"
            ).strip()

            if not content:
                continue

            sections.append(
                {
                    "assistant_id": current_id,
                    "filename": filename,
                    "content": content,
                }
            )

    prompt = "\n\n".join(
        section["content"]
        for section in sections
    )

    return {
        "id": assistant_id,
        "metadata": metadata,
        "chain": chain,
        "sections": sections,
        "prompt": prompt,
    }