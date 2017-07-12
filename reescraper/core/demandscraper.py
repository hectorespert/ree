from operator import attrgetter
from .scraper import Scraper
from ..responses import Demand


class DemandScraper(Scraper):

    def __init__(self):
        super().__init__()

    def _get(self, url):
        demands = []
        self._gethtml(url)
        rows = self._rows()
        for row in rows:
            cells = self._cells(row)
            demand_value = cells[1].get_text()
            date_str = cells[0].get_text()
            if demand_value:
                dt = self._timestamp(date_str, 'Atlantic/Canary')
                demand = Demand(float(demand_value), dt.float_timestamp)
                demands.append(demand)

        if demands:
            return max(demands, key=attrgetter('timestamp'))
        else:
            return None


