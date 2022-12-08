import unittest
from SCBot import SCBot
from SCDownloader import SoundCloud


class MyTestCase(unittest.TestCase):

    # Проверка корректности введенной ссылки
    def test_url_checker(self):
        # Album | assert False
        url = 'https://soundcloud.com/metroboomin/sets/heroes-villains-3'
        result, _ = SCBot.url_checker(url)
        self.assertEqual(False, result)

        # Track | assert True
        url = 'https://soundcloud.com/metroboomin/metro-boomin-future-too-many?in=metroboomin/sets/heroes-villains-3'
        result, _ = SCBot.url_checker(url)
        self.assertEqual(True, result)

        # Playlist | assert False
        url = 'https://soundcloud.com/1800tyfontaine/sets/lil-slime'
        result, _ = SCBot.url_checker(url)
        self.assertEqual(False, result)

        # http Track | assert True
        url = 'http://soundcloud.com/metroboomin/metro-boomin-future-too-many?in=metroboomin/sets/heroes-villains-3'
        result, _ = SCBot.url_checker(url)
        self.assertEqual(True, result)

        # http Album | assert False
        url = 'http://soundcloud.com/1800tyfontaine/sets/beautiful-michi-girls'
        result, _ = SCBot.url_checker(url)
        self.assertEqual(False, result)

        # Other links | assert False
        url = 'https://vk.com/feed/'
        result, _ = SCBot.url_checker(url)
        self.assertEqual(False, result)

    # Проверка поиска по ссылки
    def test_searching(self):
        downloader = SoundCloud()

        # Uploader from url: metroboomin, Artist - Metro Boomin
        downloader.search(
            'https://soundcloud.com/metroboomin/metro-boomin-future-too-many?in=metroboomin/sets/heroes'
            '-villains-3')
        self.assertEqual('Metro Boomin', downloader.info['uploader'])

        # Uploader from url: 1800tyfontaine, Artist - TyFontaine
        downloader.search(
            'https://soundcloud.com/1800tyfontaine/skate-prod-bugz-ronin-supah-mario?in=1800tyfontaine'
            '/sets/ascension-deluxe-virtual-1')
        self.assertEqual('TyFontaine', downloader.info['uploader'])

        #  Uploader from url: strick86, Artist - Strick
        downloader.search('https://soundcloud.com/strick86/classy-n-sht')
        self.assertNotEqual('strick86', downloader.info['uploader'])
