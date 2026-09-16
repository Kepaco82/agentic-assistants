class AssistantService:
    def __init__(self, registry):
        self.registry = registry

    def list_assistants(self):
        return self.registry.list_assistants()

    def get_assistant(self, assistant_id):
        return self.registry.load_assistant(assistant_id)

    def get_resolved_assistant(self, assistant_id):
        return self.registry.load_resolved_assistant(assistant_id)