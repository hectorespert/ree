import unittest

from arrow import get

from ree import Response, Menorca


class TestMenorca(unittest.TestCase):

    def setUp(self):
        self.instance = Menorca()
        self.date = get('2022-06-19').format('YYYY-MM-DD')

    def test_instance(self):
        self.assertIsInstance(self.instance, Menorca)

    def test_get(self):
        response = self.instance.get(self.date)
        self.assertIsInstance(response, Response)
        self.assertIsNotNone(response.timestamp)
        self.assertEqual(response.demand, 50.8)
        self.assertEqual(response.carbon, 0.0)
        self.assertEqual(response.link['pe_ma'], 0.0)
        self.assertEqual(response.link['ma_me'], 15.4)
        self.assertEqual(response.link['ma_ib'], 0.0)

    def test_get_all(self):
        responses = self.instance.get_all()
        self.assertIsNotNone(responses)


if __name__ == '__main__':
    unittest.main()
