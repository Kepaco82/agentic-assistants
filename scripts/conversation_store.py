from scripts.conversation_memory import ConversationMemory


class ConversationStore:
    def __init__(self, directory):
        self.directory = directory
        self.directory.mkdir(parents=True, exist_ok=True)

    def create(self, name):
        conversation = ConversationMemory()
        conversation.save(self.directory / f"{name}.json")
        return conversation

    def load(self, name):
        return ConversationMemory.load(
            self.directory / f"{name}.json"
        )

    def list(self):
        return sorted(
            path.stem
            for path in self.directory.glob("*.json")
        )