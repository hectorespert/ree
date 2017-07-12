from operator import attrgetter
from arrow import get
from .scrapper import Scrapper
from ..responses import Demand


class DemandScrapper(Scrapper):

    def __init__(self):
        super().__init__()

    def _get(self, url):
        demands = []
        html = self._gethtml(url)
        rows = self._getrows(html)
        for row in rows:
            cells = self._getcells(row)
            demand_value = cells[1].get_text()
            date_str = cells[0].get_text()
            if demand_value:
                dt = get(date_str + ' Atlantic/Canary', 'YYYY-MM-DD HH:mm ZZZ')
                demand = Demand(float(demand_value), dt.float_timestamp)
                demands.append(demand)

        if demands:
            return max(demands, key=attrgetter('timestamp'))
        else:
            return None


