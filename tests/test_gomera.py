import unittest

from reescraper import Gomera, Response


class TestGomera(unittest.TestCase):

    def setUp(self):
        self.instance = Gomera()

    def test_instance(self):
        self.assertIsInstance(self.instance, Gomera)

    def test_get(self):
        response = self.instance.get()
        if response:
            self.assertIsInstance(response, Response)
        else:
            self.assertIsNone(response)

if __name__ == '__main__':
    unittest.main()
