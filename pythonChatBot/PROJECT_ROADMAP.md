# 🤖 Python ChatBot: Project Guide & Expansion Roadmap

This document outlines everything you can build, train, and expand using this Python ChatBot project—from simple rule-based assistants to modern AI-powered applications.

---

## 📑 Table of Contents
1. [Current Architecture & Immediate Fixes](#1-current-architecture--immediate-fixes)
2. [Level 1: Custom Training & Corpus Expansion (ChatterBot)](#2-level-1-custom-training--corpus-expansion-chatterbot)
3. [Level 2: User Interfaces & Platforms](#3-level-2-user-interfaces--platforms)
4. [Level 3: Tool Use & External APIs](#4-level-3-tool-use--external-apis)
5. [Level 4: Modern AI Upgrades (RAG & Local LLMs)](#5-level-4-modern-ai-upgrades-rag--local-llms)
6. [5 Concrete Project Blueprints](#6-5-concrete-project-blueprints)
7. [Recommended Folder Structure](#7-recommended-folder-structure)
8. [Step-by-Step Next Steps](#8-step-by-step-next-steps)

---

## 1. Current Architecture & Immediate Fixes

### What You Currently Have
- **Core Library**: `ChatterBot` with `SQLStorageAdapter` (saving chat history and learned patterns to `database.sqlite3`).
- **Interaction**: Command-line loop with exit conditions (`quit`, `bye`, `see you soon otter`, etc.).

### Immediate Quick Fixes & Improvements
1. **Move `src/` out of `venv/`**:
   Currently, your `src/bot.py` is inside `venv/`. Virtual environment folders (`venv/`) should only contain installed libraries and python binaries. Move your source code to the project root:
   ```bash
   mkdir -p src
   mv venv/src/bot.py src/bot.py
   ```
2. **Separate Training from Inference**:
   Currently, `trainer = ChatterBotCorpusTrainer(chatbot)` sits at the bottom of `bot.py` after the `while True` loop. Separating training into `train.py` and chat into `bot.py` (or `app.py`) will make your bot start much faster.

---

## 2. Level 1: Custom Training & Corpus Expansion (ChatterBot)

You can train your chatbot on custom conversational datasets, specialized domain FAQs, or custom logic.

### A. ListTrainer (Custom Conversations & FAQs)
Train the bot on specific question-and-answer pairs:
```python
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Craig", database_uri="sqlite:///database.sqlite3")
trainer = ListTrainer(chatbot)

# Train on custom dialogs
trainer.train([
    "What are your opening hours?",
    "We are open Monday through Friday from 9 AM to 6 PM.",
    "Where are you located?",
    "We are located in Nairobi, Kenya.",
    "How can I contact support?",
    "You can email support@example.com or call +254 700 000 000."
])
```

### B. CorpusTrainer (Pre-built & Custom YAML Datasets)
Train the bot on standard English corpora or your own YAML corpus:
```python
from chatterbot.trainers import ChatterBotCorpusTrainer

trainer = ChatterBotCorpusTrainer(chatbot)

# Train on built-in corpora
trainer.train(
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations",
    "chatterbot.corpus.english.ai"
)

# Or train on a custom YAML file in your data folder:
# trainer.train("./data/custom_training_data.yml")
```

### C. Logic Adapters
Add specialized adapters for automatic math calculations, best-match thresholds, and default fallback responses:
```python
chatbot = ChatBot(
    "Craig",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_uri="sqlite:///database.sqlite3",
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.MathematicalEvaluation"
        },
        {
            "import_path": "chatterbot.logic.TimeLogicAdapter"
        },
        {
            "import_path": "chatterbot.logic.BestMatch",
            "default_response": "I am sorry, but I do not understand yet. Could you rephrase?",
            "maximum_similarity_threshold": 0.70
        }
    ]
)
```

---

## 3. Level 2: User Interfaces & Platforms

Move beyond the terminal interface by deploying your chatbot across different mediums:

| UI / Platform | Best For | Technology |
| :--- | :--- | :--- |
| **Streamlit Web UI** | Rapid prototyping & demos | `pip install streamlit` |
| **Gradio Web UI** | Clean shareable web links | `pip install gradio` |
| **FastAPI / Flask + HTML** | Production-grade web app & REST API | `pip install fastapi uvicorn` |
| **Telegram Bot** | Real-time mobile & desktop messaging | `pip install python-telegram-bot` |
| **Discord Bot** | Gaming & community server integration | `pip install discord.py` |
| **Voice Assistant** | Voice in / Speech out | `SpeechRecognition` + `pyttsx3` / `gTTS` |

### Example: Quick Web UI with Streamlit (`web_app.py`)
```python
import streamlit as st
from chatterbot import ChatBot

st.set_page_config(page_title="Craig ChatBot", page_icon="🤖")
st.title("🤖 Chat with Craig")

@st.cache_resource
def load_bot():
    return ChatBot("Craig", database_uri="sqlite:///database.sqlite3")

bot = load_bot()

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("Say something..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    response = str(bot.get_response(prompt))
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.write(response)
```

---

## 4. Level 3: Tool Use & External APIs

Give the chatbot the ability to take actions and fetch live data:

1. **Weather Assistant**: Connect to OpenWeatherMap API to answer questions like *"What's the weather in Nairobi?"*.
2. **Wikipedia / Web Search**: Fetch summaries for general knowledge queries using `wikipedia` or `duckduckgo-search`.
3. **Database Querying**: Query SQLite databases to answer business questions (e.g., inventory counts, sales stats).
4. **Email / Notification Sender**: Trigger emails or reminders when specific commands are received.

---

## 5. Level 4: Modern AI Upgrades (RAG & Local LLMs)

If you want to evolve this into a state-of-the-art AI assistant:

### A. Local Offline LLMs (via Ollama)
Run models like **Llama 3**, **Mistral**, or **Gemma** 100% locally on your machine with zero API cost:
- Install Ollama (`curl -fsSL https://ollama.com/install.sh | sh`)
- Use the `ollama` Python client:
```python
import ollama

response = ollama.chat(
    model="llama3.2:1b",
    messages=[{"role": "user", "content": "Explain how photosynthesis works in simple terms."}]
)
print(response["message"]["content"])
```

### B. Document Q&A (RAG - Retrieval-Augmented Generation)
Allow the chatbot to read your own PDFs, markdown documents, notes, or CSVs and answer questions based strictly on your files:
- **Stack**: `LangChain` / `LlamaIndex` + `ChromaDB` / `FAISS` + Local Embeddings (`sentence-transformers`).

---

## 6. 5 Concrete Project Blueprints

Here are 5 project blueprints you can choose from based on your learning goals:

### Project 1: IT Helpdesk & FAQ Support Bot
- **Goal**: Resolve common tech issues (password reset, VPN setup, wifi connection).
- **Core Features**: ListTrainer dataset with troubleshooting trees, fallback escalation to support email.
- **Deliverable**: Web UI with quick question buttons.

### Project 2: Interactive Study Buddy / Quiz Tutor
- **Goal**: Help students revise topics (Python programming, Biology, History).
- **Core Features**: Bot asks multiple choice questions, checks user answers, tracks score, and explains mistakes.
- **Deliverable**: Telegram Bot or Streamlit app.

### Project 3: Personal Finance & Expense Tracker Bot
- **Goal**: Log daily expenses via chat (e.g., *"Spent 15 on lunch"*).
- **Core Features**: Regex/NLP entity extraction for amounts and categories, SQLite storage, monthly spending summaries.
- **Deliverable**: Telegram or Command-line Bot.

### Project 4: Customer Order & Booking Bot
- **Goal**: Simulate ordering from a restaurant or booking an appointment.
- **Core Features**: Multi-step state management (selecting items -> confirming address -> calculating total).
- **Deliverable**: Flask/FastAPI REST API with a simple web frontend.

### Project 5: Smart Document Assistant (RAG)
- **Goal**: Ask questions to your study notes, resumes, or code documentation.
- **Core Features**: Embeddings + Vector search + Local LLM response synthesis.
- **Deliverable**: Gradio UI with PDF upload support.

---

## 7. Recommended Folder Structure

A clean, modular structure for your repository:

```text
pythonChatBot/
├── data/
│   ├── custom_corpus/         # YAML training files for ChatterBot
│   │   ├── greetings.yml
│   │   └── helpdesk.yml
│   └── faq_data.json          # Q&A pairs for ListTrainer
├── src/
│   ├── __init__.py
│   ├── bot.py                 # Core chatbot setup & logic adapters
│   ├── train.py               # Script to train and update database
│   ├── handlers/              # Custom logic handlers (math, APIs, etc.)
│   │   └── tools.py
│   └── ui/                    # UI interfaces
│       ├── cli.py             # Terminal interface
│       ├── streamlit_app.py   # Web interface
│       └── telegram_bot.py    # Telegram interface
├── tests/
│   └── test_bot.py            # Unit tests for responses
├── .gitignore                 # Ignore venv, .sqlite3 files, logs
├── database.sqlite3           # Trained database (auto-generated)
├── requirements.txt           # Project dependencies
└── README.md                  # Project overview & instructions
```

---

## 8. Step-by-Step Next Steps

1. **Clean up project structure**:
   - Move `src/` to project root.
   - Add `.gitignore` to avoid committing virtualenv and cache files.
   - Create `requirements.txt`.
2. **Refactor training**:
   - Create `src/train.py` for dataset loading and corpus training.
   - Keep `src/bot.py` lightweight for serving responses.
3. **Pick a Project Blueprint**:
   - Choose one of the 5 blueprints above (e.g., IT Support Bot or Study Tutor).
   - Create your custom training dataset in `data/`.
4. **Add an Interface**:
   - Build a quick web UI using Streamlit or integrate a Telegram bot.

