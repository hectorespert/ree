from operator import attrgetter

from arrow import get
from bs4 import BeautifulSoup

from reescrapper.responses import Demand
from reescrapper.core import Scrapper


class HierroDemand(Scrapper):

    def __init__(self):
        super().__init__()
        self.url = "https://demanda.ree.es/movil/canarias/el_hierro/tablas/1"

    def get(self):
        demands = []
        self.driver.get(self.url)
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        values = soup.find_all('tr', class_='ng-scope')
        for value in values:
            cleaned = value.find_all('td', class_='ng-scope ng-binding')
            demand_value = cleaned[1].get_text()
            date_str = cleaned[0].get_text()
            if demand_value:
                dt = get(date_str + ' Atlantic/Canary', 'YYYY-MM-DD HH:mm ZZZ')
                demand = Demand(float(demand_value), dt.float_timestamp)
                demands.append(demand)

        if demands:
            return max(demands, key=attrgetter('timestamp'))
        else:
            return None
