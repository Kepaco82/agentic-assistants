import sys

from scripts import agentic


class FakeLLMClient:
    pass


def test_execute_command_runs_workflow(monkeypatch, capsys):
    expected_result = {
        "workflow": ["product", "engineering"],
        "final_response": "Prioritize the roadmap by customer value and effort.",
    }

    calls = {}

    def fake_execute_request(
        request: str,
        llm_client=None,
    ):
        calls["request"] = request
        calls["llm_client"] = llm_client
        return expected_result

    monkeypatch.setattr(
        agentic,
        "LLMClient",
        FakeLLMClient,
        raising=False,
    )
    monkeypatch.setattr(
        agentic,
        "execute_request",
        fake_execute_request,
        raising=False,
    )
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "agentic",
            "execute",
            "Help us prioritize the product roadmap.",
        ],
    )

    agentic.main()

    output = capsys.readouterr().out

    assert calls["request"] == (
        "Help us prioritize the product roadmap."
    )
    assert isinstance(calls["llm_client"], FakeLLMClient)
    assert "Workflow: product -> engineering" in output
    assert (
        "Prioritize the roadmap by customer value and effort."
        in output
    )