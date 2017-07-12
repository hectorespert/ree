from .core import DemandScrapper


class DemandHierro(DemandScrapper):

    def __init__(self):
        super().__init__()
        self.url = "https://demanda.ree.es/movil/canarias/el_hierro/tablas/1"

    def get(self):
        return self._get(self.url)
