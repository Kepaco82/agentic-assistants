from typing import Any

from .assistant_planner import plan_request


EXECUTION_PRIORITY = [
    "executive",
    "product",
    "engineering",
]


def orchestrate_request(request: str) -> dict[str, Any] | None:
    """
    Convert a planned request into an ordered assistant workflow.
    """
    plan = plan_request(request)

    if plan is None:
        return None

    selected_assistants = {
        plan["primary"],
        *plan["secondary"],
    }

    workflow = [
        assistant_id
        for assistant_id in EXECUTION_PRIORITY
        if assistant_id in selected_assistants
    ]

    for assistant_id in selected_assistants:
        if assistant_id not in workflow:
            workflow.append(assistant_id)

    return {
        "primary": plan["primary"],
        "secondary": plan["secondary"],
        "confidence": plan["confidence"],
        "reasoning": plan["reasoning"],
        "workflow": workflow,
    }