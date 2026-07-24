from scripts.assistant_registry import build_registry, get_registry_entry


def test_build_registry_contains_expected_assistants() -> None:
    registry = build_registry()

    assert "executive" in registry
    assert "engineering" in registry
    assert "product" in registry


def test_registry_entry_contains_resolved_data() -> None:
    registry = build_registry()
    product = registry["product"]

    assert product["id"] == "product"
    assert product["chain"] == ["executive", "product"]
    assert isinstance(product["metadata"], dict)
    assert isinstance(product["sections"], list)
    assert product["path"] == "assistants\\product" or product["path"] == "assistants/product"


def test_get_registry_entry_returns_assistant() -> None:
    product = get_registry_entry("product")

    assert product is not None
    assert product["id"] == "product"


def test_get_registry_entry_returns_none_for_unknown_assistant() -> None:
    assistant = get_registry_entry("does-not-exist")

    assert assistant is None