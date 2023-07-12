import unittest

from arrow import get

from ree import Ceuta, Response


class TestCeuta(unittest.TestCase):
    def setUp(self):
        self.instance = Ceuta()
        self.date = get("2022-06-20").format("YYYY-MM-DD")

    def test_instance(self):
        self.assertIsInstance(self.instance, Ceuta)

    def test_get(self):
        response = self.instance.get(self.date)
        self.assertIsInstance(response, Response)
        self.assertIsNotNone(response.timestamp)
        self.assertEqual(response.demand, 18.9)
        self.assertEqual(response.diesel, 19.83)

    def test_get_all(self):
        responses = self.instance.get_all()
        self.assertIsNotNone(responses)


if __name__ == "__main__":
    unittest.main()
