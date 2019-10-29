from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

# Create chat bot
bot = ChatBot('Test')

conv = open('chat.txt', 'r').readlines()

bot.set_trainer(ListTrainer)
bot.train(conv)

while True:
    request = input('You: ')
    response = bot.get_response(request)

    print('Bot: ', response)