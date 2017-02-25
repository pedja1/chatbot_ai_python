# -*- coding: utf-8 -*-
from chatterbot import ChatBot
import logging

"""
This example shows how to create a chat bot that
will learn responses based on an additional feedback
element from the user.
"""

# Uncomment the following line to enable verbose logging
logging.basicConfig(level=logging.INFO)

# Create a new instance of a ChatBot
bot = ChatBot(
    'Feedback Learning Bot',
    storage_adapter='chatterbot.storage.JsonFileStorageAdapter',
    logic_adapters=[
        {
           'import_path': 'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.0,
            'default_response': 'I am sorry, but I do not understand.'
        }
    ],
    trainer='chatterbot.trainers.ListTrainer',
    # trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
    input_adapter='chatterbot.input.TerminalAdapter',
    output_adapter='chatterbot.output.TerminalAdapter'
)

# bot.train("chatterbot.corpus.english")
bot.train([
    "cao",
    "zdravo"
])
bot.train([
    "Ponuda telefona",
    "ponuda_telefona"
])
bot.train([
    "telefoni",
    "ponuda_telefona"
])
bot.train([
    "mobilni",
    "ponuda_telefona"
])

DEFAULT_SESSION_ID = bot.default_session.id_string

print('Type something to begin...')

# The following loop will execute each time the user enters input
while True:
    try:
        input_statement = bot.input.process_input_statement()
        statement, response, confidence = bot.generate_response(input_statement, DEFAULT_SESSION_ID)

        print(response)

        # Update the conversation history for the bot
        # It is important that this happens last, after the learning step
        bot.conversation_sessions.update(
            bot.default_session.id_string,
            (statement, response,)
        )

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
