import unittest

from arrow import get

from ree import LanzaroteFuerteventura, Response


class TestLanzaroteFuerteventura(unittest.TestCase):

    def setUp(self):
        self.instance = LanzaroteFuerteventura()
        self.date = get('2022-06-20').format('YYYY-MM-DD')

    def test_instance(self):
        self.assertIsInstance(self.instance, LanzaroteFuerteventura)

    def test_get(self):
        response = self.instance.get(self.date)
        self.assertIsInstance(response, Response)
        self.assertIsNotNone(response.timestamp)
        self.assertEqual(130.1, response.demand)

    def test_get_all(self):
        responses = self.instance.get_all()
        self.assertIsNotNone(responses)


if __name__ == '__main__':
    unittest.main()
