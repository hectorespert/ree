import unittest

from reescraper import ElHierro


class TestElHierro(unittest.TestCase):

    def test_instance(self):
        instance = ElHierro()
        self.assertIsInstance(instance, ElHierro)

if __name__ == '__main__':
    unittest.main()
