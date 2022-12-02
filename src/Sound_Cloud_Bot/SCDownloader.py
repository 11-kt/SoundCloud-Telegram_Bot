import os
import youtube_dl


class SoundCloud:

    def __init__(self):
        self.ydl_opts = {
            'proxy': f'socks5://{os.environ["PROXYCONF"]}'
        }

        # Словарь с инфой из json
        self.info = None

        # Недопустимые символы
        self.escape_symbols = ['\\', '|', '/', '+', '.', '|', '?', '\"', ':', '*', '<', '>']

    # Поиск по url
    def search(self, url: str):
        with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
            self.info = ydl.extract_info(url, download=False)