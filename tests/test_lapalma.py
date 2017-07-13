import unittest

from reescraper import LaPalma


class TestLaPalma(unittest.TestCase):

    def test_instance(self):
        instance = LaPalma()
        self.assertIsInstance(instance, LaPalma)

if __name__ == '__main__':
    unittest.main()
