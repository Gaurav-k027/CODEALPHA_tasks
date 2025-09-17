def chatbot():
    print("Chatbot: Hello! I am your simple chatbot.")
    print("Type 'bye' anytime to exit.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hello", "hi", "hey"]:
            print("Chatbot: Hi there! How can I help you?")
        elif user_input == "how are you":
            print("Chatbot: I'm doing great, thanks for asking! How about you?")
        elif user_input in ["i am fine", "i'm fine", "good", "great"]:
            print("Chatbot: That's nice to hear!")
        elif user_input in ["what is your name", "who are you"]:
            print("Chatbot: I'm a simple rule-based chatbot created in Python.")
        elif user_input in ["tell me a joke", "joke"]:
            print("Chatbot: Why don't programmers like nature? Too many bugs!")
        elif user_input in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye! Have a nice day.")
            break
        else:
            print("Chatbot: Hmm... I don't understand that. Try asking something else.")

chatbot()
