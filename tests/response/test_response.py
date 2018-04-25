from unittest import TestCase, main

from arrow import utcnow

from ree.response import Response


class TestResponse(TestCase):

    def setUp(self):
        self.timestamp = utcnow().timestamp

    def test_instance(self):
        instance = Response(self.timestamp)
        self.assertIsInstance(instance, Response)
        self.assertEqual(instance.timestamp, self.timestamp)

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

        expected = 11111111.0
        result = response.production()
        self.assertEqual(result, expected)

    def test_links(self):
        response = Response(self.timestamp)
        response.link['a'] = 1.0
        response.link['b'] = 10.0
        response.link['c'] = 100.0
        response.link['d'] = -100.0

        expected = 11.0
        result = response.links()
        self.assertEqual(result, expected)

        response.link['e'] = -21.0

        expected = -10.0
        result = response.links()
        self.assertEqual(result, expected)

    def test_unknown(self):
        response = Response(self.timestamp)
        response.demand = 250.0
        response.diesel = 100.0

        expected = 150.0
        result = response.unknown()
        self.assertEqual(result, expected)

        response.link['a'] = 100.0
        expected = 50.0
        result = response.unknown()
        self.assertEqual(result, expected)

        response.link['c'] = -300.0
        expected = 350.0
        result = response.unknown()
        self.assertEqual(result, expected)

        response.link['c'] = 300.0
        expected = 0.0
        result = response.unknown()
        self.assertEqual(result, expected)


if __name__ == '__main__':
    main()