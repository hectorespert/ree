import unittest

from reescraper import Fuerteventura


class TestFuerteventura(unittest.TestCase):

    def test_instance(self):
        instance = Fuerteventura()
        self.assertIsInstance(instance, Fuerteventura)

if __name__ == '__main__':
    unittest.main()