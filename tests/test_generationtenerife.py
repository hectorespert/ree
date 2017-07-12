import unittest

from reescraper import GenerationTenerife


class TestGenerationTenerife(unittest.TestCase):

    def test_instance(self):
        instance = GenerationTenerife()
        self.assertIsInstance(instance, GenerationTenerife)

if __name__ == '__main__':
    unittest.main()
