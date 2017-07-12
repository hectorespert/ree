from operator import attrgetter
from .scrapper import Scrapper
from ..responses import Generation


class GenerationScrapper(Scrapper):

    def __init__(self):
        super().__init__()

    def _get(self, url):
        generations = []
        self._gethtml(url)
        rows = self._rows()
        for row in rows:
            cells = self._cells(row)
            date_value = cells[0].get_text()
            diesel_value = float(cells[1].get_text())
            gas_value = float(cells[3].get_text())
            wind_value = float(cells[4].get_text())
            combined_value = float(cells[5].get_text())
            vapor_value = float(cells[6].get_text())
            solar_value = float(cells[7].get_text())
            hydraulic_value = float(cells[8].get_text())
            dt = self._timestamp(date_value, 'Atlantic/Canary')
            generation = Generation(dt.float_timestamp, diesel_value, gas_value, wind_value, combined_value,
                                    vapor_value, solar_value, hydraulic_value)
            generations.append(generation)

        if generations:
            return max(generations, key=attrgetter('timestamp'))
        else:
            return None
