from .core import DemandScrapper


class DemandLanzarote(DemandScrapper):

    def __init__(self):
        super().__init__()
        self.url = "https://demanda.ree.es/movil/canarias/lanzarot/tablas/1"

    def get(self):
        return self._get(self.url)
