from reescraper.core import Scraper


class LaPalma(Scraper):

    def __init__(self, session=None):
        super(self.__class__, self).__init__(session)

    def get(self):
        return super(self.__class__, self).get("LA_PALMA", "Atlantic/Canary")
