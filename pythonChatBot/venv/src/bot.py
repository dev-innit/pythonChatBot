from chatterbot import ChatBot
# from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot(
    "Craig",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_uri="sqlite:///database.sqlite3",)


exit_conditions = ["exit", "quit", "goodbye", "bye" , "see you later", "see you soon",  "see you soon otter", "see you soon penguin", "see you soon dolphin" ,"q"]


while True:
    query = input("> ")
    if query in exit_conditions:
        print("ChatBot: Goodbye!")
        break
    response = chatbot.get_response(query)
    print(f"ChatBot: {response}")
trainer = ChatterBotCorpusTrainer(chatbot)