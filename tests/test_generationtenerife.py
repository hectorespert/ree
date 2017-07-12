import unittest

from reescrapper import GenerationTenerife
from reescrapper.responses import Generation


class TestGenerationTenerife(unittest.TestCase):

    def test_instance(self):
        instance = GenerationTenerife()
        self.assertIsInstance(instance, GenerationTenerife)

    def test_get(self):
        demand = GenerationTenerife().get()
        self.assertIsInstance(demand, Generation)

if __name__ == '__main__':
    unittest.main()
