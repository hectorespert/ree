import unittest

from reescraper import GenerationGranCanaria


class TestGenerationHierro(unittest.TestCase):

    def test_instance(self):
        instance = GenerationGranCanaria()
        self.assertIsInstance(instance, GenerationGranCanaria)

if __name__ == '__main__':
    unittest.main()