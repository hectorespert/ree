import unittest

from reescraper import GranCanaria, Response


class TestGranCanaria(unittest.TestCase):

    def setUp(self):
        self.instance = GranCanaria()

    def test_instance(self):
        self.assertIsInstance(self.instance, GranCanaria)

    def test_get(self):
        response = self.instance.get()
        if response:
            self.assertIsInstance(response, Response)
        else:
            self.assertIsNone(response)

if __name__ == '__main__':
    unittest.main()
