import unittest

from pkg_resources import resource_string
from requests import Session
from requests_mock import Adapter, ANY

from ree import BalearicIslands, Response


class TestBalearicIslands(unittest.TestCase):

    def setUp(self):
        self.session = Session()
        self.adapter = Adapter()
        self.session.mount('https://', self.adapter)
        self.instance = BalearicIslands(self.session)
        json_data = resource_string("tests.mocks", "balearic.txt").decode("UTF-8")
        self.adapter.register_uri(ANY, ANY, text=json_data)

    def test_instance(self):
        self.assertIsInstance(self.instance, BalearicIslands)

    def test_get(self):
        response = self.instance.get()
        self.assertIsInstance(response, Response)
        self.assertTrue('pe_ma' in response.link)

    def test_get_all(self):
        responses = self.instance.get_all()
        self.assertIsNotNone(responses)
        for response in responses:
            self.assertIsInstance(response, Response)


if __name__ == '__main__':
    unittest.main()
