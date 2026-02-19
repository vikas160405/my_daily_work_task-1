def get_bot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you?"

    elif "how are you" in user_input:
        return "I'm just a chatbot, but I'm functioning perfectly!"

    elif "your name" in user_input:
        return "I am a Rule-Based Chatbot created by Vikas."

    elif "what is ai" in user_input:
        return "Artificial Intelligence is the simulation of human intelligence in machines."

    elif "python" in user_input:
        return "Python is a popular programming language used in AI and Data Science."

    elif "bye" in user_input:
        return "Goodbye! Have a great day 😊"

    else:
        return "Sorry, I don't understand that. Please try something else."
