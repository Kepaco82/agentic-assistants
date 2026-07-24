from scripts.assistant_planner import plan_request


def test_plan_product_request():
    plan = plan_request(
        "We need to prioritize the product roadmap and define engineering requirements."
    )

    assert plan["primary"] == "product"
    assert "engineering" in plan["secondary"]


def test_plan_executive_request():
    plan = plan_request(
        "Leadership needs to prioritize company initiatives for the next six months."
    )

    assert plan["primary"] == "executive"


def test_plan_returns_confidence():
    plan = plan_request(
        "Design a new API for our platform."
    )

    assert isinstance(plan["confidence"], float)


def test_plan_returns_reasoning():
    plan = plan_request(
        "Build a product roadmap."
    )

    assert len(plan["reasoning"]) > 0


def test_unknown_request_returns_none():
    assert plan_request(
        "Rewrite this sentence."
    ) is None