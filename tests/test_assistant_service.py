from scripts.assistant_service import AssistantService


class FakeRegistry:
    def list_assistants(self):
        return [
            {"assistant_id": "executive"},
            {"assistant_id": "engineering"},
        ]


def test_service_lists_assistants():
    registry = FakeRegistry()
    service = AssistantService(registry)

    assistants = service.list_assistants()

    assert assistants == [
        {"assistant_id": "executive"},
        {"assistant_id": "engineering"},
    ]

def test_service_gets_assistant():
    class FakeRegistry:
        def load_assistant(self, assistant_id):
            return {
                "assistant_id": assistant_id,
                "name": "Executive Assistant",
            }

    registry = FakeRegistry()
    service = AssistantService(registry)

    assistant = service.get_assistant("executive")

    assert assistant == {
        "assistant_id": "executive",
        "name": "Executive Assistant",
    }