import telebot
import os
from SCDownloader import SoundCloud


class SCBot:

    def __init__(self):
        self.token = os.environ['BOTTOKEN']
        self.bot = telebot.TeleBot(token=self.token)
        self.downloader = SoundCloud()

        # Ответы бота
        @self.bot.message_handler(content_types=['text'])
        def chatting(message):

            is_dwn, is_true_url = self.url_checker(message.text)

            if message.text.lower() == 'привет':
                self.hello_word(message)

            elif is_dwn and is_true_url:
                self.url = message.text

            elif ~is_dwn and is_true_url:
                self.bot.send_message(message.from_user.id, 'Некорректная ссылка на трек!')
                self.bot.send_message(message.from_user.id, 'Возможно это ссылка на артиста, плейлист или альбом')

            else:
                self.bot.send_message(message.from_user.id, "Для начала нужно поздороваться")

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

    # Поиск трека
    def dwn_track(self, message):
        self.downloader.search(url=message.text)

    # Выбор формата загрузки
    def pick_format(self, message):
        formats = []
        markup = telebot.types.InlineKeyboardMarkup()
        for i in range(len(self.downloader.info['formats'])):
            type_file_name = self.downloader.info['formats'][i]['format_id']
            formats.append(type_file_name)
            markup.add(telebot.types.InlineKeyboardButton(type_file_name, callback_data=type_file_name))

        self.bot.send_message(message.chat.id, text='Выберите формат:\n\t- hls_mp3_128, hls_opus_64 '
                                                    '- стриминговый формат, \n\t  нужно самостоятельно конвертировать '
                                                    '(например в VLC \n\t  плеере)'
                                                    '\n\t- http_mp3_128 - .mp3 файл', reply_markup=markup)
