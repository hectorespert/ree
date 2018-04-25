import unittest

from pkg_resources import resource_string
from requests import Session
from requests_mock import Adapter, ANY

from ree import IberianPeninsula, Response


class TestIberianPeninsula(unittest.TestCase):

    def setUp(self):
        self.session = Session()
        self.adapter = Adapter()
        self.session.mount('https://', self.adapter)
        self.instance = IberianPeninsula(self.session)
        data = resource_string("tests.mocks", "peninsula.txt")
        self.adapter.register_uri(ANY, ANY, text=data.decode("UTF-8"))

    def test_instance(self):
        self.assertIsInstance(self.instance, IberianPeninsula)

    def test_get(self):
        response = self.instance.get()
        self.assertIsInstance(response, Response)
        self.assertTrue('pe_ma' in response.link)
        self.assertTrue('int' in response.link)


if __name__ == '__main__':
    unittest.main()
