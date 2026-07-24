from scripts.conversation_memory import ConversationMemory


def test_memory_stores_messages():
    memory = ConversationMemory()

    memory.add_message("user", "Hello")
    memory.add_message("assistant", "Hi there")

    assert memory.get_messages() == [
        {"role": "user", "content": "Hello"},
        {"role": "assistant", "content": "Hi there"},
    ]

def test_memory_can_be_cleared():
    memory = ConversationMemory()

    memory.add_message("user", "Hello")
    memory.clear()

    assert memory.get_messages() == []