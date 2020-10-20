import csv
import os

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# print(os.getcwd())

#opening the file
file = open(os.getcwd() + "\Desktop\Term4\questionAnswer.txt", "r")

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
chatbot = ChatBot(
    'PythonBot',
    storage_adapter= 'chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch',
        {
                'import_path': 'chatterbot.logic.BestMatch',
                'default_response': 'I am sorry, but I do not understand. I am still learning.',
                'maximum_similarity_threshold': 0.90
        }   
    ],
    database_uri='sqlite:///database.sqlite3'
    )

#TRAIN THE AI WITH ENGLISH + SPANIS LANGUAGE
trainer_corpus = ChatterBotCorpusTrainer(chatbot)
trainer_corpus.train(
    'chatterbot.corpus.english',
    'chatterbot.corpus.spanish'
)

trainer = ListTrainer(chatbot)
trainer.train(data)

#TALK TO THE AI
print("Talk to the AI or enter 'bye' to quit")
while True:
    userInput = input('User: ')
    if userInput == "bye":
        print('Bot: Goodbye')
        break
    #TODO Code the get querying
    botAnswer = print('Bot: ', chatbot.get_response(userInput))