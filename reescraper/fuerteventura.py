from .core import Scraper


class Fuerteventura(Scraper):

    def __init__(self, session=None):
        super().__init__(session)

    def get(self):
        return super().get("FUERTEVE", "Atlantic/Canary")
