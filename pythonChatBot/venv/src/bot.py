from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("chatpot")

exit_conditions = ["exit", "quit", "goodbye", "bye" , "see you later", "see you soon", "see you soon giraffe", "see you soon lion", "see you soon tiger", "see you soon zebra", "see you soon kangaroo", "see you soon panda", "see you soon koala", "see you soon sloth", "see you soon otter", "see you soon penguin", "see you soon dolphin" ,"q"]


trainer = ListTrainer(chatbot)
trainer.train([
    "Hello",
    "Hi there!",
    "How are you?",
    "I'm doing well, thank you.",
    "What's your name?",
    "My name is ChatBot.",
    "What can you do?",
    "I can chat with you and answer your questions.",
    "Goodbye",
    "Goodbye! Have a great day!"
])
trainer.train([
    "What is your favorite color?",
    "I like blue.",
    "What is your favorite food?",
    "I like pizza.",
    "What is your favorite movie?",
    "I like The Matrix.",
    "What is your favorite book?",
    "I like 1984 by George Orwell.",
    "What is your favorite sport?",
    "I like soccer.",
    "What is your favorite animal?",
    "I like dogs.",
])
while True:
    query = input("> ")
    if query in exit_conditions:
        print("ChatBot: Goodbye!")
        break
    response = chatbot.get_response(query)
    print(f"ChatBot: {response}")