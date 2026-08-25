"""
Training script for the ChatBot.
Run this script whenever you add new training data in data/conversations.json
or want to train on corpus datasets.

Usage:
    python src/train.py
"""

import json
import os
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

# Database path (relative to project root)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "database.sqlite3")
DATA_PATH = os.path.join(BASE_DIR, "data", "conversations.json")


def train_bot():
    print("=" * 50)
    print("🤖 Initializing ChatBot for Training...")
    print("=" * 50)

    bot = ChatBot(
        "Craig",
        storage_adapter="chatterbot.storage.SQLStorageAdapter",
        database_uri=f"sqlite:///{DB_PATH}",
    )

    # 1. Train on built-in English Corpus
    print("\n📚 [Step 1/2] Training on standard English corpus...")
    corpus_trainer = ChatterBotCorpusTrainer(bot)
    corpus_trainer.train(
        "chatterbot.corpus.english.greetings",
        "chatterbot.corpus.english.conversations",
    )

    # 2. Train on custom data from data/conversations.json
    print("\n📝 [Step 2/2] Training on custom conversations (data/conversations.json)...")
    if os.path.exists(DATA_PATH):
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            custom_data = json.load(f)

        list_trainer = ListTrainer(bot)
        for conversation in custom_data:
            list_trainer.train(conversation)
        print(f"✅ Successfully trained {len(custom_data)} custom conversation pairs.")
    else:
        print(f"⚠️ Custom data file not found at {DATA_PATH}. Skipping.")

    print("\n🎉 Training completed successfully! You can now run `python src/bot.py` to chat.")
    print("=" * 50)


if __name__ == "__main__":
    train_bot()

