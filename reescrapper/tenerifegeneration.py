from arrow import get
from bs4 import BeautifulSoup
from operator import attrgetter

from reescrapper.responses import Generation
from reescrapper.core import Scrapper


class TenerifeGeneration(Scrapper):

    def __init__(self):
        super().__init__()
        self.url = "https://demanda.ree.es/movil/canarias/tenerife/tablas/2"

    def get(self):
        generations = []
        self.driver.get(self.url)
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')

        values = soup.find_all('tr', class_='ng-scope')
        for value in values:
            cleaned = value.find_all('td', class_='ng-scope ng-binding')
            date_value = cleaned[0].get_text()
            diesel_value = float(cleaned[1].get_text())
            gas_value = float(cleaned[3].get_text())
            wind_value = float(cleaned[4].get_text())
            combined_value = float(cleaned[5].get_text())
            vapor_value = float(cleaned[6].get_text())
            solar_value = float(cleaned[7].get_text())
            hydraulic_value = float(cleaned[8].get_text())
            dt = get(date_value + ' Atlantic/Canary', 'YYYY-MM-DD HH:mm ZZZ')
            generation = Generation(dt.float_timestamp, diesel_value, gas_value, wind_value, combined_value, vapor_value, solar_value, hydraulic_value)
            generations.append(generation)

        if generations:
            return max(generations, key=attrgetter('timestamp'))
        else:
            return None
