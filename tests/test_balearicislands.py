import unittest

from arrow import get

from ree import BalearicIslands, Response


class TestBalearicIslands(unittest.TestCase):

    def setUp(self):
        self.instance = BalearicIslands()
        self.date = get('2022-06-10').format('YYYY-MM-DD')

    def test_instance(self):
        self.assertIsInstance(self.instance, BalearicIslands)

    def test_get(self):
        response = self.instance.get(self.date)
        self.assertIsInstance(response, Response)
        self.assertEqual(546.8, response.demand)
        self.assertTrue('pe_ma' in response.link)

    def test_get_all(self):
        responses = self.instance.get_all()
        self.assertIsNotNone(responses)
        for response in responses:
            self.assertIsInstance(response, Response)


if __name__ == '__main__':
    unittest.main()
