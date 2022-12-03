import telebot
import os


class SCBot:

    def __init__(self):
        self.token = os.environ['BOTTOKEN']
        self.bot = telebot.TeleBot(token=self.token)
        self.url = None

        # Ответы бота
        @self.bot.message_handler(content_types=['text'])
        def chatting(message):

            if message.text.lower() == 'привет':
                self.hello_word(message)

            else:
                self.url = message.text

    # Приветствие
    def hello_word(self, message):
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton('LiL Uzi Vert',
                                                      url='https://soundcloud.com/liluzivert/moment-of-clarity'))
        self.bot.send_message(message.from_user.id, 'Привет!')
        self.bot.send_message(message.from_user.id, 'Чтобы мной воспользоваться, пожалуйста, отправь ссылку '
                                                    'на трек!')
        self.bot.send_message(message.from_user.id, 'Например:\nhttps://soundcloud.com/liluzivert/moment-of-clarity',
                              reply_markup=markup)
