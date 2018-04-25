from unittest import TestCase, main

from arrow import get

from ree.core import Scraper


class TestScraper(TestCase):

    def setUp(self):
        self.scrapper = Scraper()

    def test_instance(self):
        self.assertIsInstance(self.scrapper, Scraper)

    def test__timestamp(self):
        date_str = '2017-07-13 10:00'
        timezone = 'Atlantic/Canary'
        result = self.scrapper._timestamp(date_str, timezone)
        expected = get('2017-07-13T10:00:00+01:00')
        self.assertEqual(result, expected)

    def test__searchdate(self):
        arrow = get('2017-07-13T10:00:00+00:00')
        result = self.scrapper._searchdate('Atlantic/Canary', arrow)
        expected = '2017-07-13'
        self.assertEqual(result, expected)

    def test__makeurl(self):
        zone = "GCANARIA"
        date = "2017-07-13"
        result = self.scrapper._makeurl(zone, date)
        expected = "https://demanda.ree.es/WSvisionaMovilesCanariasRest/resources/demandaGeneracionCanarias?curva=GCANARIA&fecha=2017-07-13"
        self.assertEqual(result, expected)
        result = self.scrapper._makeurl(zone, date, "Baleares")
        expected = "https://demanda.ree.es/WSvisionaMovilesBalearesRest/resources/demandaGeneracionBaleares?curva=GCANARIA&fecha=2017-07-13"
        self.assertEqual(result, expected)

if __name__ == '__main__':
    main()
