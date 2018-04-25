import unittest

from pkg_resources import resource_string
from requests import Session
from requests_mock import Adapter, ANY

from ree import LaPalma, Response


class TestLaPalma(unittest.TestCase):

    def setUp(self):
        self.session = Session()
        self.adapter = Adapter()
        self.session.mount('https://', self.adapter)
        self.instance = LaPalma(self.session)
        json_data = resource_string("tests.mocks", "canary.txt").decode("UTF-8")
        self.adapter.register_uri(ANY, ANY, text=json_data)

    def test_instance(self):
        self.assertIsInstance(self.instance, LaPalma)

    def test_get(self):
        response = self.instance.get()
        self.assertIsInstance(response, Response)
        self.assertIsNotNone(response.timestamp)

    def test_get_all(self):
        responses = self.instance.get_all()
        self.assertIsNotNone(responses)


if __name__ == '__main__':
    unittest.main()
