import telebot
import os


class SCBot:

    def __init__(self):
        self.token = os.environ['BOTTOKEN']
        self.bot = telebot.TeleBot(token=self.token)

        # Ответы бота
        @self.bot.message_handler(content_types=['text'])
        def chatting(message):

            if message.text.lower() == 'привет':
                self.bot.send_message(message.from_user.id, 'Привет!')
