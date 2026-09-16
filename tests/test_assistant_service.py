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

def test_service_gets_resolved_assistant():
    class FakeLoader:
        def load_resolved_assistant(self, assistant_id):
            return {
                "metadata": {
                    "id": assistant_id,
                    "name": "Executive Assistant",
                },
                "chain": ["base", assistant_id],
            }

    loader = FakeLoader()
    service = AssistantService(loader)

    assistant = service.get_resolved_assistant("executive")

    assert assistant == {
        "metadata": {
            "id": "executive",
            "name": "Executive Assistant",
        },
        "chain": ["base", "executive"],
    }
