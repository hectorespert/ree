import unittest

from ree import CanaryIslands, Response


class TestCanaryIslands(unittest.TestCase):

    def setUp(self):
        self.instance = CanaryIslands()

    def test_instance(self):
        self.assertIsInstance(self.instance, CanaryIslands)

    def test_get(self):
        response = self.instance.get()
        self.assertIsInstance(response, Response)


if __name__ == '__main__':
    unittest.main()
