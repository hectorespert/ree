from .core import Scraper


class IberianPeninsula(Scraper):

    def __init__(self, session=None):
        super(self.__class__, self).__init__(session)

    def get(self, date=None, last=True):
        return super(self.__class__, self).get("DEMANDA", "Europe/Madrid", "Peninsula", date, last)
