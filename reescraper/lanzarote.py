from .core import Scraper


class Lanzarote(Scraper):

    def __init__(self, session=None):
        super().__init__(session)

    def get(self):
        return super().get("LANZAROT", "Atlantic/Canary")
