from scripts.assistant_orchestrator import orchestrate_request


def test_orchestrator_returns_execution_plan():
    plan = orchestrate_request(
        "We need to prioritize the product roadmap and define engineering requirements."
    )

    assert plan["primary"] == "product"
    assert "engineering" in plan["workflow"]


def test_workflow_starts_with_primary():
    plan = orchestrate_request(
        "Build a product roadmap."
    )

    assert plan["workflow"][0] == "product"


def test_workflow_has_no_duplicates():
    plan = orchestrate_request(
        "Engineering needs engineering support for the product roadmap."
    )

    assert len(plan["workflow"]) == len(set(plan["workflow"]))


def test_unknown_request_returns_none():
    assert orchestrate_request(
        "Rewrite this sentence."
    ) is None


def test_execution_order_is_preserved():
    plan = orchestrate_request(
        "Leadership needs a product roadmap with engineering implementation."
    )

    assert plan["workflow"] == [
        "executive",
        "product",
        "engineering",
    ]