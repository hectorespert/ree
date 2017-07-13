from .core import Scraper


class Tenerife(Scraper):

    def __init__(self, session=None):
        super().__init__(session)

    def get(self):
        return super().get("TENERIFE", "Atlantic/Canary")

