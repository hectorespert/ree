from .core import Scraper

from arrow import get
from operator import attrgetter
from .response import Response


class GranCanaria(Scraper):

    def __init__(self, session=None):
        super().__init__(session)
        self.url = "https://demanda.ree.es/WSvisionaMovilesCanariasRest/resources/demandaGeneracionCanarias?curva=GCANARIA&fecha=2017-07-13"

    def get(self):
        responses = []
        for value in self._getjson(self.url):
            dt = get(value['ts'] + ' ' + 'Atlantic/Canary', 'YYYY-MM-DD HH:mm ZZZ')
            response = Response(dt.float_timestamp)
            response.demand = value['dem']
            response.diesel = value['die']
            response.gas = value['gas']
            response.wind = value['eol']
            response.combined = value['cc']
            response.vapor = value['vap']
            response.solar = value['fot']
            response.hydraulic = value['hid']
            responses.append(response)

        return max(responses, key=attrgetter('timestamp'))


