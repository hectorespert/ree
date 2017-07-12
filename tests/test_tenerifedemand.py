import unittest

from reescrapper import TenerifeDemand
from reescrapper.responses import Demand


class TestTenerifeDemand(unittest.TestCase):

    def test_instance(self):
        instance = TenerifeDemand()
        self.assertIsInstance(instance, TenerifeDemand)

    def test_get(self):
        demand = TenerifeDemand().get()
        self.assertIsInstance(demand, Demand)

if __name__ == '__main__':
    unittest.main()
