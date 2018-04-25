import unittest

from pkg_resources import resource_string
from requests import Session
from requests_mock import Adapter, ANY

from ree import CanaryIslands, Response


class TestCanaryIslands(unittest.TestCase):

    def setUp(self):
        self.session = Session()
        self.adapter = Adapter()
        self.session.mount('https://', self.adapter)
        self.instance = CanaryIslands(self.session)
        json_data = resource_string("tests.mocks", "canary.txt").decode("UTF-8")
        self.adapter.register_uri(ANY, ANY, text=json_data)

    def test_instance(self):
        self.assertIsInstance(self.instance, CanaryIslands)

    def test_get(self):
        response = self.instance.get()
        self.assertIsInstance(response, Response)


if __name__ == '__main__':
    unittest.main()
