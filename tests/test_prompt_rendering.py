from scripts.assistant_loader import load_resolved_assistant
from scripts.assistant_registry import get_registry_entry


def test_resolved_assistant_includes_rendered_prompt():
    assistant = load_resolved_assistant("product")

    assert "prompt" in assistant
    assert assistant["prompt"]


def test_rendered_prompt_contains_all_sections_in_order():
    assistant = load_resolved_assistant("product")

    expected_prompt = "\n\n".join(
        section["content"]
        for section in assistant["sections"]
    )

    assert assistant["prompt"] == expected_prompt


def test_registry_entry_includes_rendered_prompt():
    assistant = get_registry_entry("product")

    assert assistant is not None
    assert "prompt" in assistant
    assert assistant["prompt"]


def test_registry_prompt_matches_resolved_assistant_prompt():
    resolved = load_resolved_assistant("product")
    registry_entry = get_registry_entry("product")

    assert registry_entry is not None
    assert registry_entry["prompt"] == resolved["prompt"]