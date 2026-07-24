from typing import Any

from .assistant_registry import build_registry


ROUTING_TERMS: dict[str, list[str]] = {
    "product": [
        "product",
        "roadmap",
        "prd",
        "feature",
        "acceptance criteria",
        "user story",
        "discovery",
        "requirements",
    ],
    "engineering": [
        "engineering",
        "architecture",
        "software",
        "database",
        "api",
        "infrastructure",
        "security",
        "devops",
        "code",
    ],
    "executive": [
        "executive",
        "leadership",
        "strategy",
        "prioritize",
        "prioritization",
        "company",
        "initiative",
        "operations",
        "six months",
    ],
}


def route_request(request: str) -> dict[str, Any] | None:
    """
    Route a user request to the best matching assistant.
    """
    normalized_request = request.lower()
    registry = build_registry()

    best_match: dict[str, Any] | None = None

    for assistant_id, terms in ROUTING_TERMS.items():
        if assistant_id not in registry:
            continue

        matched_terms = [
            term for term in terms if term in normalized_request
        ]

        score = len(matched_terms)

        if score == 0:
            continue

        if best_match is None or score > best_match["score"]:
            best_match = {
                "assistant_id": assistant_id,
                "score": score,
                "matched_terms": matched_terms,
            }

    return best_match