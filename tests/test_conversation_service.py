from scripts.conversation_service import ConversationService
from scripts.conversation_store import ConversationStore


def test_service_lists_conversations(tmp_path):
    store = ConversationStore(tmp_path)
    service = ConversationService(store)

    store.create("marketing")
    store.create("engineering")

    assert service.list_conversations() == [
        "engineering",
        "marketing",
    ]

def test_service_creates_conversation(tmp_path):
    store = ConversationStore(tmp_path)
    service = ConversationService(store)

    conversation = service.create_conversation("marketing")

    assert conversation.get_messages() == []
    assert (tmp_path / "marketing.json").exists()

def test_service_loads_conversation(tmp_path):
    store = ConversationStore(tmp_path)
    service = ConversationService(store)

    conversation = store.create("marketing")
    conversation.add_message("user", "Hello")
    conversation.save(tmp_path / "marketing.json")

    loaded = service.load_conversation("marketing")

    assert loaded.get_messages() == [
        {"role": "user", "content": "Hello"}
    ]

def test_service_deletes_conversation(tmp_path):
    store = ConversationStore(tmp_path)
    service = ConversationService(store)

    store.create("marketing")

    service.delete_conversation("marketing")

    assert not (tmp_path / "marketing.json").exists()

def test_service_renames_conversation(tmp_path):
    store = ConversationStore(tmp_path)
    service = ConversationService(store)

    store.create("marketing")

    service.rename_conversation(
        "marketing",
        "sales",
    )

    assert not (tmp_path / "marketing.json").exists()
    assert (tmp_path / "sales.json").exists()