# 🤖 Python Study Flashcard ChatBot

A versatile Python chatbot built with **ChatterBot** and SQLite storage. It is pre-configured as a **Study Flashcard Assistant** for testing programming and computer science concepts, and is easily customizable with your own training datasets.

---

## 📁 Project Structure

```text
pythonChatBot/
├── data/
│   └── conversations.json   # Customizable Q&A training pairs (Flashcards)
├── src/
│   ├── bot.py               # Main chatbot runtime & interactive terminal UI
│   └── train.py             # Dedicated training script (Corpus + Custom JSON)
├── .gitignore               # Ignores venv, database, and cache files
├── database.sqlite3         # SQLite database storing learned responses
├── PROJECT_ROADMAP.md       # Comprehensive expansion guide & blueprints
├── README.md                # Project documentation
└── requirements.txt         # Project dependencies
```

---

## ⚡ Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Train the Bot
Train the bot on both the English conversational corpus and custom flashcards from `data/conversations.json`:
```bash
python src/train.py
```

### 3. Chat with the Bot
Launch the interactive terminal session:
```bash
python src/bot.py
```

---

## 🎓 How to Add More Knowledge
To add new questions or study topics:
1. Open [`data/conversations.json`](./pythonChatBot/data/conversations.json).
2. Add your `["Question", "Answer"]` pair to the list.
3. Re-run `python src/train.py`.

---

## 🚀 Further Expansion & Blueprints
For ideas on adding Web UIs (Streamlit/Gradio), Telegram bots, tool integrations, or local LLMs/RAG, see:
👉 **[PROJECT_ROADMAP.md](./pythonChatBot/PROJECT_ROADMAP.md)**
