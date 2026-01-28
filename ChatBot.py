def chatbot():
    print("Chatbot: Hello! I am your virtual assistant. Type 'exit' to end the conversation.\n")

    while True:
        user = input("You: ").strip().lower()

        # Greetings
        if user in ["hello", "hi", "hey"]:
            print("Chatbot: Hello!")

        elif user in ["good morning", "morning"]:
            print("Chatbot: Good morning. I hope you have a productive day.")

        elif user in ["good afternoon", "afternoon"]:
            print("Chatbot: Good afternoon. How can I help you?")

        elif user in ["good evening", "evening"]:
            print("Chatbot: Good evening. How may I assist you?")

        # Well-being
        elif user in ["how are you", "how are you doing"]:
            print("Chatbot: I am doing well, thank you for asking. How about you?")

        elif user in ["are you okay", "are you fine"]:
            print("Chatbot: Yes, I am absolutely fine. Thank you for your concern.")

        elif user in ["how is your day", "how is your day going"]:
            print("Chatbot: My day is going smoothly. I hope yours is as well.")

        # Identity & role
        elif user in ["who are you", "what are you"]:
            print("Chatbot: I am a rule-based virtual assistant designed to help you.")

        elif user in ["what can you do", "what do you do"]:
            print("Chatbot: I can assist you with general questions and daily conversations.")

        # Help & assistance
        elif user in ["can you help me", "help me"]:
            print("Chatbot: Certainly. Please describe your issue.")

        elif user in ["i need help", "i need some help"]:
            print("Chatbot: I am here to help. Please explain your concern.")

        elif user in ["can you assist me", "assist me"]:
            print("Chatbot: Of course. What kind of assistance do you need?")

        elif user in ["i have a question", "i want to ask something"]:
            print("Chatbot: Please go ahead. I am listening.")

        elif user in ["can you explain", "explain something"]:
            print("Chatbot: I will try my best to explain it clearly.")

        # Politeness & appreciation
        elif user in ["thank you", "thanks", "thanks a lot"]:
            print("Chatbot: You're welcome. I'm glad I could help.")

        elif user in ["i appreciate it", "much appreciated"]:
            print("Chatbot: I'm happy to be of assistance.")

        elif user in ["well done", "good job"]:
            print("Chatbot: Thank you. I appreciate your feedback.")

        # Opinions / general talk
        elif user in ["what do you think", "your opinion"]:
            print("Chatbot: I try to provide neutral and helpful responses.")

        elif user in ["is everything okay", "everything okay"]:
            print("Chatbot: Yes, everything is functioning as expected.")

        # Availability
        elif user in ["are you available", "can we talk"]:
            print("Chatbot: Yes, I am available to assist you.")

        elif user in ["are you busy"]:
            print("Chatbot: I am always available to help you.")

        # Ending conversation
        elif user in ["bye", "goodbye", "exit", "quit", "see you later"]:
            print("Chatbot: Thank you for the conversation. Have a great day.")
            break

        # Unknown input
        else:
            print("Chatbot: I'm sorry, I did not fully understand that. Could you please rephrase?")

# Start chatbot
chatbot()
