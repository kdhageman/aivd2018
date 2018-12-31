from unittest import TestCase

from opdracht4.main import to_word


class TestToWord(TestCase):
    def test_normal(self):
        arr = [8, 5, 12, 12, 15, 23, 15, 18, 12, 4]
        w = to_word(arr)
        self.assertEqual(w, "helloworld")