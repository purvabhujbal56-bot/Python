print("Chatbot: Hello! I am your chatbot.")
print("Chatbot: Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "hello" or user == "hii":
        print("Chatbot: Hello! How can I help you?")

    elif user == "how are you":
        print("Chatbot: I am fine. Thank you!")

    elif user == "what is your name":
        print("Chatbot: My name is Python Chatbot.")

    elif user == "what is python":
        print("Chatbot: Python is a high-level programming language.")

    elif user == "who created python":
        print("Chatbot: Python was created by Guido van Rossum.")

    elif user == "what is ai":
        print("Chatbot: AI stands for Artificial Intelligence.")

    elif user == "thank you" or user == "thanks":
        print("Chatbot: You're welcome!")

    elif user == "bye" or user == "by":
        print("Chatbot: Goodbye! Have a nice day.")
        break

    else:
        print("Chatbot: Sorry, I don't understand that.")