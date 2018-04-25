import unittest

from pkg_resources import resource_string
from requests import Session
from requests_mock import Adapter, ANY

from ree import Response, Mallorca


class TestMallorca(unittest.TestCase):

    def setUp(self):
        self.session = Session()
        self.adapter = Adapter()
        self.session.mount('https://', self.adapter)
        self.instance = Mallorca(self.session)
        json_data = resource_string("tests.mocks", "mallorca.txt").decode("UTF-8")
        self.adapter.register_uri(ANY, ANY, text=json_data)

    def test_instance(self):
        self.assertIsInstance(self.instance, Mallorca)

    def test_get(self):
        response = self.instance.get()
        self.assertIsInstance(response, Response)
        self.assertIsNotNone(response.timestamp)
        self.assertEqual(response.demand, 497.3)
        self.assertEqual(response.carbon, 315.9)
        self.assertEqual(response.link['pe_ma'], 80.3)
        self.assertEqual(response.link['ma_me'], 0.0)
        self.assertEqual(response.link['ma_ib'], -7.6)

    def test_get_all(self):
        responses = self.instance.get_all()
        self.assertIsNotNone(responses)


if __name__ == '__main__':
    unittest.main()
