import unittest
from unittest import TestCase
from main import from_russia, unique_values, max_volume


class TestCountry(TestCase):
    geo_logs = [
        {'visit1': ['Москва', 'Россия']},
        {'visit2': ['Дели', 'Индия']},
        {'visit3': ['Владимир', 'Россия']},
        {'visit4': ['Лиссабон', 'Португалия']},
        {'visit5': ['Париж', 'Франция']},
        {'visit6': ['Лиссабон', 'Португалия']},
        {'visit7': ['Тула', 'Россия']},
        {'visit8': ['Тула', 'Россия']},
        {'visit9': ['Курск', 'Россия']},
        {'visit10': ['Архангельск', 'Россия']}
    ]
    def test_have_result(self):
        result = from_russia(self.geo_logs)
        expected = 0
        self.assertNotEqual(len(result), expected)

    def test_have_russia(self):
        result = len(from_russia(self.geo_logs))
        expected = 6
        self.assertEqual(result, expected)



class TestUniqueValues(TestCase):
    ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}

    def test_sum_values(self):
        result = unique_values(self.ids)
        expected = [98, 35, 15, 213, 54, 119]
        self.assertEqual(result, expected)

    def test_len_values(self):
        result = len(unique_values(self.ids))
        expected = 6
        self.assertEqual(result, expected)

class MaxVolume(TestCase):
    stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
    def test_max_volume_key(self):
        result = max_volume(self.stats)
        expected = 'yandex'
        self.assertEqual(result, expected)

    def test_max_volume_value(self):
        result = max_volume(self.stats)
        expected = 'ok'
        self.assertNotEqual(result, expected)


