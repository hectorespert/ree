import unittest

from reescraper import DemandGranCanaria


class TestDemandGranCanaria(unittest.TestCase):

    def test_instance(self):
        instance = DemandGranCanaria()
        self.assertIsInstance(instance, DemandGranCanaria)

if __name__ == '__main__':
    unittest.main()