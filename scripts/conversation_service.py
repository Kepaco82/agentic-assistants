class ConversationService:
    def __init__(self, store):
        self.store = store

    def list_conversations(self):
        return self.store.list()

    def create_conversation(self, name):
        return self.store.create(name)

    def load_conversation(self, name):
        return self.store.load(name)

    def delete_conversation(self, name):
        self.store.delete(name)

    def rename_conversation(self, old_name, new_name):
        self.store.rename(old_name, new_name)