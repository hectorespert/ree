import unittest

from arrow import get

from ree import Response, ElHierro


class TestElHierro(unittest.TestCase):

    def setUp(self):
        self.instance = ElHierro()
        self.date = get('2022-06-19').format('YYYY-MM-DD')

    def test_instance(self):
        self.assertIsInstance(self.instance, ElHierro)

    def test_get(self):
        response = self.instance.get(self.date)
        self.assertIsInstance(response, Response)
        self.assertIsNotNone(response.timestamp)
        self.assertEqual(response.demand, 4.7)
        self.assertEqual(response.hydraulic, 2.8)
        self.assertEqual(response.wind, 0.0)
        self.assertEqual(response.vapor, 0.0)
        self.assertEqual(response.diesel, 1.9)

    def test_get_all(self):
        responses = self.instance.get_all()
        self.assertIsNotNone(responses)


if __name__ == '__main__':
    unittest.main()
