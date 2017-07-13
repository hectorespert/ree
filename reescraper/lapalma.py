from .core import Scraper


class LaPalma(Scraper):

    def __init__(self, session=None):
        super().__init__(session)

    def get(self):
        return super().get("LA_PALMA", "Atlantic/Canary")
