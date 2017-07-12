import unittest

from reescraper import GenerationHierro


class TestGenerationHierro(unittest.TestCase):

    def test_instance(self):
        instance = GenerationHierro()
        self.assertIsInstance(instance, GenerationHierro)

if __name__ == '__main__':
    unittest.main()
