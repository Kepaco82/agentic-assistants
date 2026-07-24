import json


class ConversationMemory:
    def __init__(self):
        self._messages = []

    def add_message(self, role, content):
        self._messages.append(
            {
                "role": role,
                "content": content,
            }
        )

    def get_messages(self):
        return list(self._messages)

    def clear(self):
        self._messages = []

    def save(self, filename):
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(self._messages, file)

    @classmethod
    def load(cls, filename):
        memory = cls()

        with open(filename, "r", encoding="utf-8") as file:
            memory._messages = json.load(file)

        return memory