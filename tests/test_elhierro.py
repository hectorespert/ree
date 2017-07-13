import unittest

from reescraper import ElHierro, Response


class TestElHierro(unittest.TestCase):

    def setUp(self):
        self.instance = ElHierro()

    def test_instance(self):
        self.assertIsInstance(self.instance, ElHierro)

    def test_get(self):
        response = self.instance.get()
        if response:
            self.assertIsInstance(response, Response)
        else:
            self.assertIsNone(response)

if __name__ == '__main__':
    unittest.main()
