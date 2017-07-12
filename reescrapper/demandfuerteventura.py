from .core import DemandScrapper


class DemandFuerteventura(DemandScrapper):

    def __init__(self):
        super().__init__()
        self.url = "https://demanda.ree.es/movil/canarias/fuerteve/tablas/1"

    def get(self):
        return self._get(self.url)
