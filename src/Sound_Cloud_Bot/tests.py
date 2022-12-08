import unittest
from SCBot import SCBot


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
