from .core import DemandScrapper


class DemandGranCanaria(DemandScrapper):

    def __init__(self):
        super().__init__()
        self.url = "https://demanda.ree.es/movil/canarias/gcanaria/tablas/1"

    def get(self):
        return self._get(self.url)
