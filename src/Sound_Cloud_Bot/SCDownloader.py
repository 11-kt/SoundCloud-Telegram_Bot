import os
import youtube_dl
import requests
from StringBuilder import StringBuilder


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

        # Скачивание выбранного формата
        def download(self, track_format):
            i = 0
            for element in self.info['formats']:
                if element['format_id'] == track_format:
                    break
                else:
                    i += 1

            response = requests.get(url=self.info['formats'][i]['url'], stream=False,
                                    headers=self.info['formats'][i]['http_headers'])

            file_name = StringBuilder()
            for element in self.info['title']:
                if element in self.escape_symbols:
                    file_name.append('_')
                else:
                    file_name.append(element)

            with open(f"{file_name.to_string()}.mp3", 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)

            return f'{file_name.to_string()}.mp3'
