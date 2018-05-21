from .core import Scraper


class BalearicIslands(Scraper):

    def __init__(self, session=None, verify=True):
        super(self.__class__, self).__init__(session, verify)

    def get(self, date=None, last=True):
        return super(self.__class__, self).get("BALEARES", "Europe/Madrid", "Baleares", date, last)

    def get_all(self):
        return self.get(None, False)


