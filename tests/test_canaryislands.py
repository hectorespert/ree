import unittest

from reescraper import CanaryIslands


class TestCanaryIslands(unittest.TestCase):

    def test_instance(self):
        instance = CanaryIslands()
        self.assertIsInstance(instance, CanaryIslands)

if __name__ == '__main__':
    unittest.main()
