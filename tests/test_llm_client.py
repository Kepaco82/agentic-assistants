from types import SimpleNamespace

import pytest

from scripts.llm_client import LLMClient


class FakeResponses:
    def __init__(self):
        self.calls = []

    def create(self, **kwargs):
        self.calls.append(kwargs)
        return SimpleNamespace(
            output_text="This is the generated response.",
            _request_id="req_test_123",
        )


class FakeOpenAIClient:
    def __init__(self):
        self.responses = FakeResponses()


def test_generate_returns_output_text():
    fake_client = FakeOpenAIClient()
    llm = LLMClient(
        client=fake_client,
        model="test-model",
    )

    result = llm.generate(
        instructions="You are a product assistant.",
        input_text="Prioritize the roadmap.",
    )

    assert result["text"] == "This is the generated response."


def test_generate_passes_model_instructions_and_input():
    fake_client = FakeOpenAIClient()
    llm = LLMClient(
        client=fake_client,
        model="test-model",
    )

    llm.generate(
        instructions="You are an engineering assistant.",
        input_text="Estimate the implementation effort.",
    )

    call = fake_client.responses.calls[0]

    assert call["model"] == "test-model"
    assert call["instructions"] == (
        "You are an engineering assistant."
    )
    assert call["input"] == (
        "Estimate the implementation effort."
    )


def test_generate_returns_request_id():
    fake_client = FakeOpenAIClient()
    llm = LLMClient(
        client=fake_client,
        model="test-model",
    )

    result = llm.generate(
        instructions="Test instructions.",
        input_text="Test input.",
    )

    assert result["request_id"] == "req_test_123"


def test_missing_api_key_raises_clear_error(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)

    with pytest.raises(
        ValueError,
        match="OPENAI_API_KEY is not configured",
    ):
        LLMClient()