from ree.core import Scraper


class LaPalma(Scraper):

    def __init__(self, session=None):
        super(self.__class__, self).__init__(session)

    def get(self, date=None, last=True):
        return super(self.__class__, self).get("LA_PALMA", "Atlantic/Canary", "Canarias", date, last)

    def get_all(self, date=None):
        return self.get(date, False)