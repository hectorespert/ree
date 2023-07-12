import unittest

from arrow import get
from requests import Session
from requests_mock import ANY, GET, Adapter

from ree import Response, ElHierro


class TestElHierro(unittest.TestCase):
    def setUp(self):
        self.instance = ElHierro()
        self.date = get("2022-06-19").format("YYYY-MM-DD")
        self.session = Session()
        self.adapter = Adapter()
        self.session.mount("https://", self.adapter)

    def test_instance(self):
        self.assertIsInstance(self.instance, ElHierro)

    def test_get(self):
        with open("tests/mocks/El_Hierro.txt", "rb") as elhierro_mock:
            self.adapter.register_uri(
                GET,
                ANY,
                content=elhierro_mock.read(),
            )
        response = ElHierro(session=self.session).get()
        self.assertIsInstance(response, Response)
        self.assertIsNotNone(response.timestamp)
        self.assertEqual(response.demand, 7)
        self.assertEqual(response.hydraulic, -1.4)
        self.assertEqual(response.wind, 0.0)
        self.assertEqual(response.vapor, 0.0)
        self.assertEqual(response.diesel, 1)

    def test_get_all(self):
        responses = self.instance.get_all()
        self.assertIsNotNone(responses)


if __name__ == "__main__":
    unittest.main()
