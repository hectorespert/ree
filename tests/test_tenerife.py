import unittest

from reescraper import Tenerife


class TestTenerife(unittest.TestCase):

    def test_instance(self):
        instance = Tenerife()
        self.assertIsInstance(instance, Tenerife)

if __name__ == '__main__':
    unittest.main()
