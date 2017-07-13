import unittest

from reescraper import Gomera


class TestGomera(unittest.TestCase):

    def test_instance(self):
        instance = Gomera()
        self.assertIsInstance(instance, Gomera)

if __name__ == '__main__':
    unittest.main()
