"""
Main ChatBot runtime.
Run this script to chat with the bot in your terminal.

Usage:
    python src/bot.py
"""

import os
import sys
from chatterbot import ChatBot

# Database path (relative to project root)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "database.sqlite3")


def create_chatbot():
    return ChatBot(
        "Craig",
        storage_adapter="chatterbot.storage.SQLStorageAdapter",
        database_uri=f"sqlite:///{DB_PATH}",
        logic_adapters=[
            {
                "import_path": "chatterbot.logic.BestMatch",
                "default_response": "I'm not sure I understand yet. Could you try rephrasing or asking another question?",
                "maximum_similarity_threshold": 0.65,
            },
        ],
        read_only=True,
    )


def start_chat():
    print("=" * 55)
    print("🤖 ChatBot 'Craig' is ready! (Type 'quit' or 'exit' to leave)")
    print("💡 Tip: Try asking about Python, Git, HTTP codes, or databases!")
    print("=" * 55)

    chatbot = create_chatbot()
    exit_conditions = {
        "exit", "quit", "goodbye", "bye", "q",
        "see you later", "see you soon",
        "see you soon otter", "see you soon penguin", "see you soon dolphin",
    }

    while True:
        try:
            query = input("\nYou: ").strip()

            # Skip empty inputs
            if not query:
                continue

            # Check exit conditions (case-insensitive)
            if query.lower() in exit_conditions:
                print("ChatBot: Goodbye! Have a great day! 👋")
                break

            response = chatbot.get_response(query)
            print(f"ChatBot: {response}")

        except (KeyboardInterrupt, EOFError):
            print("\nChatBot: Goodbye! 👋")
            sys.exit(0)


if __name__ == "__main__":
    start_chat()