from chatterbot.trainers import ListTrainer

def train_chatbot(chatbot):
    trainer = ListTrainer(chatbot)

    trainer.train([
        "Hi there!",
        "Hello",
        # Add more conversations for training set 1
    ])
