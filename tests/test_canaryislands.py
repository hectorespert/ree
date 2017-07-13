import unittest

from reescraper import CanaryIslands, Response, NoDataException, TimestampException


class TestCanaryIslands(unittest.TestCase):

    def setUp(self):
        self.instance = CanaryIslands()

    def test_instance(self):
        self.assertIsInstance(self.instance, CanaryIslands)

    def test_get(self):
        try:
            response = self.instance.get()
            self.assertIsInstance(response, Response)
        except NoDataException:
            self.assertTrue(True)
        except TimestampException:
            self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
