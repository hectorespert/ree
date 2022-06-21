import unittest

from arrow import get

from ree import Response, Ibiza


class TestIbiza(unittest.TestCase):

    def setUp(self):
        self.instance = Ibiza()
        self.date = get('2022-06-20').format('YYYY-MM-DD')

    def test_instance(self):
        self.assertIsInstance(self.instance, Ibiza)

    def test_get(self):
        response = self.instance.get(self.date)
        self.assertIsInstance(response, Response)
        self.assertIsNotNone(response.timestamp)
        self.assertEqual(response.demand, 115.6)
        self.assertEqual(response.carbon, 0.0)
        self.assertEqual(response.link['pe_ma'], 0.0)
        self.assertEqual(response.link['ma_me'], 0.0)
        self.assertEqual(86.9, response.link['ma_ib'])

    def test_get_all(self):
        responses = self.instance.get_all()
        self.assertIsNotNone(responses)


if __name__ == '__main__':
    unittest.main()
