from scripts.assistant_executor import execute_request


def test_executor_returns_execution_result():
    result = execute_request(
        "We need to prioritize the roadmap and estimate engineering work."
    )

    assert result is not None
    assert result["request"] == (
        "We need to prioritize the roadmap and estimate engineering work."
    )
    assert result["workflow"]
    assert result["steps"]


def test_executor_preserves_workflow_order():
    result = execute_request(
        "We need to prioritize the roadmap and estimate engineering work."
    )

    step_assistants = [
        step["assistant_id"]
        for step in result["steps"]
    ]

    assert step_assistants == result["workflow"]


def test_executor_creates_shared_context():
    result = execute_request(
        "We need to prioritize the roadmap and estimate engineering work."
    )

    assert "shared_context" in result
    assert result["shared_context"]["original_request"] == (
        "We need to prioritize the roadmap and estimate engineering work."
    )


def test_executor_steps_include_input_and_output():
    result = execute_request(
        "We need to prioritize the roadmap and estimate engineering work."
    )

    for step in result["steps"]:
        assert "assistant_id" in step
        assert "input" in step
        assert "output" in step


def test_executor_returns_none_for_unknown_request():
    result = execute_request(
        "Purple clouds silently discuss invisible spoons."
    )

    assert result is None