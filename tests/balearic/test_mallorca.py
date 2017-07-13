import unittest

from reescraper import Response, Mallorca


class TestElHierro(unittest.TestCase):

    def setUp(self):
        self.instance = Mallorca()

    def test_instance(self):
        self.assertIsInstance(self.instance, Mallorca)

    def test_get(self):
        response = self.instance.get()
        if response:
            self.assertIsInstance(response, Response)
        else:
            self.assertIsNone(response)

if __name__ == '__main__':
    unittest.main()