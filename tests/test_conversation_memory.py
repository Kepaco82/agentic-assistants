from scripts.conversation_memory import ConversationMemory
from scripts.conversation_store import ConversationStore

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

def test_save_and_load_conversation(tmp_path):
    memory = ConversationMemory()

    memory.add_message("user", "Hello")
    memory.add_message("assistant", "Hi!")

    filename = tmp_path / "conversation.json"

    memory.save(filename)

    loaded = ConversationMemory.load(filename)

    assert loaded.get_messages() == memory.get_messages()

def test_create_named_conversation(tmp_path):
    store = ConversationStore(tmp_path)

    conversation = store.create("marketing")

    assert conversation.get_messages() == []

def test_create_named_conversation_saves_file(tmp_path):
    store = ConversationStore(tmp_path)

    store.create("marketing")

    assert (tmp_path / "marketing.json").exists()

def test_load_named_conversation(tmp_path):
    store = ConversationStore(tmp_path)

    conversation = store.create("marketing")
    conversation.add_message("user", "Write a campaign")
    conversation.save(tmp_path / "marketing.json")

    loaded = store.load("marketing")

    assert loaded.get_messages() == [
        {"role": "user", "content": "Write a campaign"}
    ]

def test_list_named_conversations(tmp_path):
    store = ConversationStore(tmp_path)

    store.create("marketing")
    store.create("engineering")

    assert store.list() == ["engineering", "marketing"]

def test_store_creates_missing_directory(tmp_path):
    directory = tmp_path / "conversations"
    store = ConversationStore(directory)

    store.create("marketing")

    assert directory.exists()