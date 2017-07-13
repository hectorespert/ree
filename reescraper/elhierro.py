from .core import Scraper


class ElHierro(Scraper):

    def __init__(self, session=None):
        super().__init__(session)

    def get(self):
        return super().get("EL_HIERRO", "Atlantic/Canary")
