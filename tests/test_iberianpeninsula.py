import unittest

from arrow import get

from ree import IberianPeninsula, Response


class TestIberianPeninsula(unittest.TestCase):

    def setUp(self):
        self.instance = IberianPeninsula()
        self.date = get('2022-06-20').format('YYYY-MM-DD')

    def test_instance(self):
        self.assertIsInstance(self.instance, IberianPeninsula)

    def test_get(self):
        response = self.instance.get(self.date)
        self.assertIsInstance(response, Response)
        self.assertEqual(24646, response.demand)
        self.assertTrue('pe_ma' in response.link)
        self.assertTrue('int' in response.link)


if __name__ == '__main__':
    unittest.main()
