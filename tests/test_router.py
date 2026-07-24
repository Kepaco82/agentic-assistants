from scripts.assistant_router import route_request


def test_routes_product_request() -> None:
    result = route_request("Create a product roadmap and PRD for a new feature.")

    assert result is not None
    assert result["assistant_id"] == "product"


def test_routes_engineering_request() -> None:
    result = route_request(
        "Design the software architecture and database for this application."
    )

    assert result is not None
    assert result["assistant_id"] == "engineering"


def test_routes_executive_request() -> None:
    result = route_request(
        "Help leadership prioritize company initiatives for the next six months."
    )

    assert result is not None
    assert result["assistant_id"] == "executive"


def test_returns_routing_details() -> None:
    result = route_request("Write acceptance criteria for a product feature.")

    assert result is not None
    assert isinstance(result["score"], int)
    assert isinstance(result["matched_terms"], list)


def test_returns_none_when_no_assistant_matches() -> None:
    result = route_request("Purple clouds drift quietly over the ocean.")

    assert result is None