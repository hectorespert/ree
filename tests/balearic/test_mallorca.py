import unittest

from arrow import get

from ree import Response, Mallorca


class TestMallorca(unittest.TestCase):

    def setUp(self):
        self.instance = Mallorca()
        self.date = get('2022-06-20').format('YYYY-MM-DD')

    def test_instance(self):
        self.assertIsInstance(self.instance, Mallorca)

    def test_get(self):
        response = self.instance.get(self.date)
        self.assertIsInstance(response, Response)
        self.assertIsNotNone(response.timestamp)
        self.assertEqual(response.demand, 688.2)
        self.assertEqual(response.carbon, 70.6)
        self.assertEqual(response.waste, 49.8)
        self.assertEqual(response.link['pe_ma'], 41.8)
        self.assertEqual(response.link['ma_me'], -5.6)
        self.assertEqual(response.link['ma_ib'], -91.5)

    def test_get_all(self):
        responses = self.instance.get_all()
        self.assertIsNotNone(responses)


if __name__ == '__main__':
    unittest.main()
