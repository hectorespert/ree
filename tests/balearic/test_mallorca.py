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
        self.assertEqual(response.demand, 480.2)
        self.assertEqual(71.3, response.carbon)
        self.assertEqual(50.9, response.waste)
        self.assertEqual(42.7, response.link['pe_ma'])
        self.assertEqual(-2.7, response.link['ma_me'])
        self.assertEqual(-86.9, response.link['ma_ib'])

    def test_get_all(self):
        responses = self.instance.get_all()
        self.assertIsNotNone(responses)


if __name__ == '__main__':
    unittest.main()
