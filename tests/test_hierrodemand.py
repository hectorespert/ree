import unittest

from reescrapper import HierroDemand
from reescrapper.responses import Demand


class TestHierroDemand(unittest.TestCase):

    def test_instance(self):
        instance = HierroDemand()
        self.assertIsInstance(instance, HierroDemand)

    def test_get(self):
        demand = HierroDemand().get()
        self.assertIsInstance(demand, Demand)

if __name__ == '__main__':
    unittest.main()