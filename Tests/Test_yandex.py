import unittest
from unittest import TestCase
from yandex import create_folder

class TestYandex(TestCase):
    def test_answer_code(self):
        result = create_folder()
        expected = 201
        self.assertEqual(result, expected)

    def test_ansver_not_error(self):
        result = create_folder()
        expected = 404
        self.assertNotEqual(result, expected)
        