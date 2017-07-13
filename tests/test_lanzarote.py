import unittest

from reescraper import Lanzarote


class TestLanzarote(unittest.TestCase):

    def test_instance(self):
        instance = Lanzarote()
        self.assertIsInstance(instance, Lanzarote)

if __name__ == '__main__':
    unittest.main()
