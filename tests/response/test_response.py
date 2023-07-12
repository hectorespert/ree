from unittest import TestCase, main

from arrow import get
from requests import Session
from requests_mock import ANY, GET, Adapter

from ree import Menorca, Response

MOCK_FILE = "tests/mocks/Menorca.txt"


class TestResponse(TestCase):
    def setUp(self):
        self.timestamp = get(
            "2023-07-12 19:20" + " " + "Europe/Madrid", "YYYY-MM-DD HH:mm ZZZ"
        ).timestamp()
        self.session = Session()
        self.adapter = Adapter()
        self.session.mount("https://", self.adapter)

    def test_instance(self):
        with open(MOCK_FILE, "rb") as menorca_mock:
            self.adapter.register_uri(
                GET,
                ANY,
                content=menorca_mock.read(),
            )
        instance = Menorca(session=self.session).get()
        self.assertIsInstance(instance, Response)
        self.assertEqual(instance.timestamp, self.timestamp)

    def test_to_dict(self):
        with open(MOCK_FILE, "rb") as menorca_mock:
            self.adapter.register_uri(
                GET,
                ANY,
                content=menorca_mock.read(),
            )
        response = Menorca(session=self.session).get()
        expected = {
            "carbon": 0.0,
            "combined": 0.0,
            "datetime": "2023-07-12T17:20:00+00:00",
            "demand": 110.1,
            "diesel": 31.2,
            "gas": 57.1,
            "hydraulic": None,
            "nuclear": None,
            "other": None,
            "solar": 1.3,
            "timestamp": 1689182400.0,
            "vapor": None,
            "waste": 0.0,
            "wind": 0.0,
        }
        response_dict = response.to_dict()
        self.assertEqual(response_dict, expected)
        datetime = response_dict["datetime"]
        timestamp = response_dict["timestamp"]
        self.assertEqual(get(datetime), get(timestamp))

    def test_production(self):
        response = Response(self.timestamp)
        response.diesel = 1.0
        response.gas = 10.0
        response.wind = 100.0
        response.combined = 1000.0
        response.vapor = 10000.0
        response.solar = 100000.0
        response.hydraulic = 1000000.0
        response.carbon = 10000000.0
        response.waste = 100000000.0

        expected = 111111111.0
        result = response.production()
        self.assertEqual(result, expected)

    def test_links(self):
        response = Response(self.timestamp)
        response.link["a"] = 1.0
        response.link["b"] = 10.0
        response.link["c"] = 100.0
        response.link["d"] = -100.0

        expected = 11.0
        result = response.links()
        self.assertEqual(result, expected)

        response.link["e"] = -21.0

        expected = -10.0
        result = response.links()
        self.assertEqual(result, expected)

    def test_unknown(self):
        with open(MOCK_FILE, "rb") as menorca_mock:
            self.adapter.register_uri(
                GET,
                ANY,
                content=menorca_mock.read(),
            )
        response = Menorca(session=self.session).get()

        expected = 0.1
        result = response.unknown()
        self.assertEqual(result, expected)

        response.link["ma_me"] = 10
        expected = 10.5
        result = response.unknown()
        self.assertEqual(result, expected)

        response.link["ma_ib"] = -300.0
        expected = 310.5
        result = response.unknown()
        self.assertEqual(result, expected)

        response.link["pe_ma"] = None
        expected = 310.5
        result = response.unknown()
        self.assertEqual(result, expected)


if __name__ == "__main__":
    main()
