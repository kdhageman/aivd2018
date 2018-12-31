from unittest import TestCase

from opdracht3.main import word_value

class TestWordValue(TestCase):
    def test_normal(self):
        d = {
            'a': 3,
            'b': 2,
            'c': 1
        }
        word = 'abc'
        v = word_value(word, d)
        self.assertEqual(v, 321)

    def test_long(self):
        d = {
            'a': 3,
            'b': 2,
            'c': 1
        }
        word = 'abcabcacbca'
        v = word_value(word, d)
        self.assertEqual(v, 32132131213)