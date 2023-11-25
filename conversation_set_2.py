from chatterbot.trainers import ListTrainer

def train_chatbot(chatbot):
    trainer = ListTrainer(chatbot)

    trainer.train([
        "How are you?",
        "I am good.",
        "That is good to hear.",
        "Thank you",
        "You are welcome.",
        # Add more conversations for training set 2
    ])
