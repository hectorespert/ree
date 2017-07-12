import unittest

from reescrapper import DemandHierro
from reescrapper.responses import Demand


class TestDemandHierro(unittest.TestCase):

    def test_instance(self):
        instance = DemandHierro()
        self.assertIsInstance(instance, DemandHierro)

    def test_get(self):
        demand = DemandHierro().get()
        self.assertIsInstance(demand, Demand)

if __name__ == '__main__':
    unittest.main()