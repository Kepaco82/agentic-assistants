import sys

from assistant_registry import list_assistants


def main():
    if len(sys.argv) != 2:
        print("Usage: python scripts/search_assistants.py <query>")
        raise SystemExit(1)

    query = sys.argv[1].strip().lower()
    assistants = list_assistants()

    matches = []

    for assistant in assistants:
        searchable_fields = [
            assistant.get("id", ""),
            assistant.get("name", ""),
            assistant.get("category", ""),
            assistant.get("status", ""),
            assistant.get("description", ""),
            assistant.get("owner", ""),
            assistant.get("tags", ""),
        ]

        searchable_text = " ".join(searchable_fields).lower()

        if query in searchable_text:
            matches.append(assistant)

    print(f"Search Results: {query}")
    print("=" * (16 + len(query)))

    if not matches:
        print("No matching assistants found.")
        return

    for assistant in matches:
        print(f"- {assistant.get('name', 'Unknown')}")
        print(f"  Category: {assistant.get('category', 'Unknown')}")
        print(f"  Description: {assistant.get('description', 'Unknown')}")

    print(f"\nTotal matches: {len(matches)}")


if __name__ == "__main__":
    main()