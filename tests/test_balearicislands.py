import unittest

from reescraper import BalearicIslands, Response


class TestCanaryIslands(unittest.TestCase):

    def setUp(self):
        self.instance = BalearicIslands()

    def test_instance(self):
        self.assertIsInstance(self.instance, BalearicIslands)

    def test_get(self):
        response = self.instance.get()
        self.assertIsInstance(response, Response)
        self.assertTrue('pe_ma' in response.link)

    def test_get_all(self):
        responses = self.instance.get_all()
        self.assertIsNotNone(responses)
        for response in responses:
            self.assertIsInstance(response, Response)

if __name__ == '__main__':
    unittest.main()
