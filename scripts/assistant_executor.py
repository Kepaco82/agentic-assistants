from typing import Any

from scripts.assistant_orchestrator import orchestrate_request
from scripts.assistant_registry import build_registry


def build_step_input(
    request: str,
    previous_outputs: list[dict[str, Any]],
) -> str:
    """
    Build the input sent to the current assistant.

    The original request is always included. Outputs from earlier
    assistants are added in workflow order.
    """
    parts = [
        "Original request:",
        request,
    ]

    if previous_outputs:
        parts.extend(
            [
                "",
                "Previous assistant outputs:",
            ]
        )

        for output in previous_outputs:
            assistant_id = output["assistant_id"]
            text = output.get("text", "")

            parts.extend(
                [
                    "",
                    f"{assistant_id}:",
                    text,
                ]
            )

    parts.extend(
        [
            "",
            "Provide your contribution based on your assigned role.",
        ]
    )

    return "\n".join(parts)


def execute_request(
    request: str,
    llm_client: Any | None = None,
    registry: dict[str, dict[str, Any]] | None = None,
):
    """
    Plan and execute an assistant workflow.

    When an LLM client is supplied, every assistant in the workflow
    generates a response. Without an LLM client, the executor returns
    planned placeholder steps for backward compatibility and testing.
    """
    plan = orchestrate_request(request)

    if plan is None:
        return None

    if registry is None:
        registry = build_registry()

    shared_context = {
        "original_request": request,
        "previous_outputs": [],
    }

    steps = []

    for assistant_id in plan["workflow"]:
        assistant = registry.get(assistant_id)

        if assistant is None:
            raise ValueError(
                f"Assistant is missing from registry: {assistant_id}"
            )

        step_input_text = build_step_input(
            request=request,
            previous_outputs=shared_context["previous_outputs"],
        )

        step_input = {
            "request": request,
            "shared_context": {
                "original_request": request,
                "previous_outputs": list(
                    shared_context["previous_outputs"]
                ),
            },
            "input_text": step_input_text,
        }

        if llm_client is None:
            step_output = {
                "assistant_id": assistant_id,
                "status": "planned",
                "message": (
                    f"{assistant_id} assistant execution is prepared "
                    "but no LLM client was supplied."
                ),
            }
        else:
            prompt = assistant.get("prompt")

            if not isinstance(prompt, str) or not prompt.strip():
                raise ValueError(
                    f"Assistant prompt is missing: {assistant_id}"
                )

            llm_result = llm_client.generate(
                instructions=prompt,
                input_text=step_input_text,
            )

            step_output = {
                "assistant_id": assistant_id,
                "status": "completed",
                "text": llm_result["text"],
                "request_id": llm_result.get("request_id"),
            }

        steps.append(
            {
                "assistant_id": assistant_id,
                "input": step_input,
                "output": step_output,
            }
        )

        shared_context["previous_outputs"].append(step_output)

    final_output = steps[-1]["output"]

    final_response = (
        final_output.get("text")
        or final_output.get("message")
    )

    return {
        "request": request,
        "primary": plan["primary"],
        "secondary": plan["secondary"],
        "workflow": plan["workflow"],
        "confidence": plan["confidence"],
        "reasoning": plan["reasoning"],
        "shared_context": shared_context,
        "steps": steps,
        "final_response": final_response,
    }