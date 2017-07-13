import unittest

from reescraper import Response, Menorca


class TestMenorca(unittest.TestCase):

    def setUp(self):
        self.instance = Menorca()

    def test_instance(self):
        self.assertIsInstance(self.instance, Menorca)

    def test_get(self):
        response = self.instance.get()
        if response:
            self.assertIsInstance(response, Response)
        else:
            self.assertIsNone(response)

if __name__ == '__main__':
    unittest.main()
