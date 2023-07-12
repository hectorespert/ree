import unittest

from arrow import get
from requests import Session
from requests_mock import ANY, GET, Adapter

from ree import Response, Menorca


class TestMenorca(unittest.TestCase):
    def setUp(self):
        self.instance = Menorca()
        self.date = get("2022-06-19").format("YYYY-MM-DD")
        self.timestamp = get(
            "2023-07-12 19:20" + " " + "Europe/Madrid", "YYYY-MM-DD HH:mm ZZZ"
        ).timestamp()
        self.session = Session()
        self.adapter = Adapter()
        self.session.mount("https://", self.adapter)

    def test_instance(self):
        self.assertIsInstance(self.instance, Menorca)

    def test_get(self):
        with open("tests/mocks/Menorca.txt", "rb") as menorca_mock:
            self.adapter.register_uri(
                GET,
                ANY,
                content=menorca_mock.read(),
            )
        response = Menorca(session=self.session).get()
        self.assertIsInstance(response, Response)
        self.assertIsNotNone(response.timestamp)
        self.assertEqual(response.demand, 110.1)
        self.assertEqual(response.carbon, 0.0)
        self.assertEqual(response.link["pe_ma"], None)
        self.assertEqual(response.link["ma_me"], 20.4)
        self.assertEqual(response.link["ma_ib"], 0.0)

    def test_get_all(self):
        responses = self.instance.get_all()
        self.assertIsNotNone(responses)


if __name__ == "__main__":
    unittest.main()
