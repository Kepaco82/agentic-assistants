from scripts.assistant_orchestrator import orchestrate_request


def execute_request(request: str):
    plan = orchestrate_request(request)

    if plan is None:
        return None

    shared_context = {
        "original_request": request,
        "previous_outputs": [],
    }

    steps = []

    for assistant_id in plan["workflow"]:
        step_input = {
            "request": request,
            "shared_context": shared_context.copy(),
        }

        step_output = {
            "assistant_id": assistant_id,
            "status": "planned",
            "message": (
                f"{assistant_id} assistant execution is prepared "
                "but not yet connected to an LLM."
            ),
        }

        steps.append(
            {
                "assistant_id": assistant_id,
                "input": step_input,
                "output": step_output,
            }
        )

        shared_context["previous_outputs"].append(step_output)

    return {
        "request": request,
        "primary": plan["primary"],
        "secondary": plan["secondary"],
        "workflow": plan["workflow"],
        "confidence": plan["confidence"],
        "reasoning": plan["reasoning"],
        "shared_context": shared_context,
        "steps": steps,
    }