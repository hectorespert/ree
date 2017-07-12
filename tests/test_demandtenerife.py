import unittest

from reescraper import DemandTenerife


class TestDemandTenerife(unittest.TestCase):

    def test_instance(self):
        instance = DemandTenerife()
        self.assertIsInstance(instance, DemandTenerife)

if __name__ == '__main__':
    unittest.main()
