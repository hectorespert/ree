import unittest

from reescrapper import TenerifeGeneration
from reescrapper.responses import Generation


class TestTenerifeGeneration(unittest.TestCase):

    def test_instance(self):
        instance = TenerifeGeneration()
        self.assertIsInstance(instance, TenerifeGeneration)

    def test_get(self):
        demand = TenerifeGeneration().get()
        self.assertIsInstance(demand, Generation)

if __name__ == '__main__':
    unittest.main()
