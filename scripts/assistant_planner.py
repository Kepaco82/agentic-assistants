from typing import Any

from .assistant_router import ROUTING_TERMS


def plan_request(request: str) -> dict[str, Any] | None:
    """
    Build a simple multi-assistant plan for a user request.
    """
    normalized_request = request.lower()
    matches: list[dict[str, Any]] = []

    for assistant_id, terms in ROUTING_TERMS.items():
        matched_terms = [
            term for term in terms if term in normalized_request
        ]

        if not matched_terms:
            continue

        matches.append(
            {
                "assistant_id": assistant_id,
                "score": len(matched_terms),
                "matched_terms": matched_terms,
            }
        )

    if not matches:
        return None

    matches.sort(
        key=lambda item: item["score"],
        reverse=True,
    )

    primary = matches[0]
    secondary = [
        item["assistant_id"]
        for item in matches[1:]
    ]

    total_possible_matches = sum(
        len(terms) for terms in ROUTING_TERMS.values()
    )

    confidence = round(
        primary["score"] / total_possible_matches,
        2,
    )

    reasoning = [
        f"{item['assistant_id']} matched: "
        f"{', '.join(item['matched_terms'])}"
        for item in matches
    ]

    return {
        "primary": primary["assistant_id"],
        "secondary": secondary,
        "confidence": confidence,
        "reasoning": reasoning,
    }