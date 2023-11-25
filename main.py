from chatterbot import ChatBot
from conversation_set_1 import train_chatbot as train_set_1
from conversation_set_2 import train_chatbot as train_set_2
# from conversation_set_3 import train_chatbot as train_set_3

# Create a ChatBot instance
chatbot = ChatBot('Training Example')

# Train using conversation set 1
train_set_1(chatbot)

# Train using conversation set 2
train_set_2(chatbot)

# Train using conversation set 3
# train_set_3(chatbot)

# Example interaction
while True:
    user_input = input("You: ")

    # Get the chatbot's response to the user input
    bot_response = chatbot.get_response(user_input)

    print("Bot:", bot_response)
