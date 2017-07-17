import unittest

from reescraper import IberianPeninsula, Response


class TestCanaryIslands(unittest.TestCase):

    def setUp(self):
        self.instance = IberianPeninsula()

    def test_instance(self):
        self.assertIsInstance(self.instance, IberianPeninsula)

    def test_get(self):
        response = self.instance.get()
        self.assertIsInstance(response, Response)
        self.assertTrue('pe_ma' in response.link)
        self.assertTrue('int' in response.link)

if __name__ == '__main__':
    unittest.main()
