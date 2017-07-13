import unittest

from reescraper import GranCanaria


class TestGranCanaria(unittest.TestCase):

    def test_instance(self):
        instance = GranCanaria()
        self.assertIsInstance(instance, GranCanaria)

if __name__ == '__main__':
    unittest.main()