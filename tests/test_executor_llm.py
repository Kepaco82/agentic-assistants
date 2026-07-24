from scripts.assistant_executor import execute_request

from unittest.mock import patch

class FakeLLMClient:
    def __init__(self):
        self.calls = []

    def generate(
        self,
        instructions: str,
        input_text: str,
    ) -> dict[str, str]:
        call_number = len(self.calls) + 1

        self.calls.append(
            {
                "instructions": instructions,
                "input_text": input_text,
            }
        )

        return {
            "text": f"Assistant response {call_number}",
            "request_id": f"req_{call_number}",
        }


def build_test_registry():
    return {
        "executive": {
            "id": "executive",
            "prompt": "You are the executive assistant.",
        },
        "product": {
            "id": "product",
            "prompt": "You are the product assistant.",
        },
        "engineering": {
            "id": "engineering",
            "prompt": "You are the engineering assistant.",
        },
    }


def test_executor_calls_llm_for_each_workflow_step():
    fake_llm = FakeLLMClient()

    result = execute_request(
        "We need to prioritize the roadmap and estimate engineering work.",
        llm_client=fake_llm,
        registry=build_test_registry(),
    )

    assert result is not None
    assert len(fake_llm.calls) == len(result["workflow"])
    assert len(result["steps"]) == len(result["workflow"])


def test_executor_uses_assistant_prompt_as_instructions():
    fake_llm = FakeLLMClient()
    registry = build_test_registry()

    result = execute_request(
        "We need to prioritize the roadmap and estimate engineering work.",
        llm_client=fake_llm,
        registry=registry,
    )

    assert result is not None

    for index, assistant_id in enumerate(result["workflow"]):
        assert fake_llm.calls[index]["instructions"] == (
            registry[assistant_id]["prompt"]
        )


def test_executor_stores_real_llm_output():
    fake_llm = FakeLLMClient()

    result = execute_request(
        "We need to prioritize the roadmap and estimate engineering work.",
        llm_client=fake_llm,
        registry=build_test_registry(),
    )

    assert result is not None
    assert result["steps"][0]["output"]["text"] == (
        "Assistant response 1"
    )
    assert result["steps"][0]["output"]["request_id"] == "req_1"
    assert result["steps"][0]["output"]["status"] == "completed"


def test_executor_passes_previous_outputs_to_next_assistant():
    fake_llm = FakeLLMClient()

    result = execute_request(
        "We need to prioritize the roadmap and estimate engineering work.",
        llm_client=fake_llm,
        registry=build_test_registry(),
    )

    assert result is not None
    assert len(fake_llm.calls) >= 2

    second_input = fake_llm.calls[1]["input_text"]

    assert "Assistant response 1" in second_input


def test_executor_returns_final_response():
    fake_llm = FakeLLMClient()

    result = execute_request(
        "We need to prioritize the roadmap and estimate engineering work.",
        llm_client=fake_llm,
        registry=build_test_registry(),
    )

    assert result is not None
    assert result["final_response"] == (
        f"Assistant response {len(result['workflow'])}"
    )
