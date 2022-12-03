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

    # Проверка корректности введенной ссылки
    @staticmethod
    def url_checker(message):
        mes_list = message.split('/')
        ignore_pages = ['sets', 'you', 'discover', 'albums']
        is_url = 0

        if (mes_list[0] == 'https:' or mes_list[0] == 'http:') and mes_list[2] == 'soundcloud.com':
            is_url = 1
            if mes_list[3] in ignore_pages or len(mes_list) < 5 or mes_list[4] in ignore_pages:
                return False, is_url
            else:
                return True, is_url
        return False, is_url
