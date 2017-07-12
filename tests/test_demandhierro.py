import unittest

from reescraper import DemandHierro


class TestDemandHierro(unittest.TestCase):

    def test_instance(self):
        instance = DemandHierro()
        self.assertIsInstance(instance, DemandHierro)

if __name__ == '__main__':
    unittest.main()