import csv
import os

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# print(os.getcwd())

#opening the file
file = open(os.getcwd() + "\Desktop\data1.txt", "r")

#declaring variable
data = []

#reading the file
while True:
    csv_reader = csv.reader(file, delimiter=',')
    #reading and saving data to the list
    for row in csv_reader:
        data.extend(row)
    break
#print(data)

#CREATE THE AI OBJECT
chatbot = ChatBot('BrisbaneBot')

#TRAIN THE AI WITH ENGLISH + SPANIS LANGUAGE
trainer_corpus = ChatterBotCorpusTrainer(chatbot)
trainer_corpus.train(
    'chatterbot.corpus.english',
    'chatterbot.corpus.spanish'
)

#TALK TO THE AI
print("Talk to the AI or enter 'bye' to quit")
while True:
    userInput = input('User: ')
    if userInput == "bye":
        print('Bot: Goodbye')
        break
    #TODO Code the get querying
    botAnswer = print('Bot: ', chatbot.get_response(userInput))