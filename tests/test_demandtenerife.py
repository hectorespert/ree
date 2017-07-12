import unittest

from reescrapper import DemandTenerife
from reescrapper.responses import Demand


class TestDemandTenerife(unittest.TestCase):

    def test_instance(self):
        instance = DemandTenerife()
        self.assertIsInstance(instance, DemandTenerife)

    def test_get(self):
        demand = DemandTenerife().get()
        self.assertIsInstance(demand, Demand)

if __name__ == '__main__':
    unittest.main()
