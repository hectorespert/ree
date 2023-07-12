from typing import List, Union
from arrow import get, utcnow
from requests import Session
from json import loads
from operator import attrgetter
from ..response import Response
from .exceptions import ResponseCodeException, ResponseDataException

FUEL_MAPPING = {
    "dem": "demand",
    "nuc": "nuclear",
    "die": "diesel",
    "genAux": "diesel",
    "gas": "gas",
    "gf": "gas",
    "eol": "wind",
    "cc": "combined",
    "vap": "vapor",
    "fot": "solar",
    "sol": "solar",
    "hid": "hydraulic",
    "car": "carbon",
    "resid": "waste",
    "termRenov": "other",
    "cogenResto": "other",
}

LINK_MAPPING = {
    "cb": "pe_ma",
    "icb": "pe_ma",
    "emm": "ma_me",
    "emi": "ma_ib",
    "eif": "ib_fo",
    "inter": "int",
}


class Scraper(object):
    def __init__(self, session=None, verify=True):
        self.verify = verify
        if session and isinstance(session, Session):
            self.session = session
        else:
            self.session = Session()

    def _get(
        self, zone, timezone, system="Canarias", date=None, last=True
    ) -> Union[Response, List[Response]]:
        if not date:
            date = self._searchdate(timezone)
        url = self._makeurl(zone, date, system)
        responses = []
        for value in self._request(url):
            ts = value["ts"]
            arrow = self._timestamp(ts, timezone)
            response = Response(arrow.float_timestamp)

            for key, attr in FUEL_MAPPING.items():
                if key in value:
                    if getattr(response, attr) is None:
                        setattr(response, attr, value[key])
                    else:
                        setattr(response, attr, getattr(response, attr) + value[key])

            for key, attr in LINK_MAPPING.items():
                if key in value:
                    response.link[attr] = value[key]
                else:
                    response.link[attr] = None

            responses.append(response)
        if last:
            return max(responses, key=attrgetter("timestamp"))
        else:
            return responses

    def get(self, zone, timezone, system="Canarias", date=None, last=True) -> Response:
        response = self._get(zone, timezone, system, date, last)
        if isinstance(response, Response):
            return response
        else:
            raise TypeError

    def get_all(self, zone, timezone, system="Canarias", date=None) -> List[Response]:
        response_list = self._get(zone, timezone, system, date, False)
        if isinstance(response_list, list):
            return response_list
        else:
            raise TypeError

    def _request(self, url: str):
        response = self.session.request("GET", url, verify=self.verify)
        if response.status_code != 200:
            raise ResponseCodeException
        if not response.text:
            raise ResponseDataException
        return self.__getjson(response.text)

    def _makeurl(self, zone, date, system="Canarias"):
        return f"https://demanda.ree.es/WSvisionaMoviles{system}Rest/resources/demandaGeneracion{system}?curva={zone}&fecha={date}"

    def __getjson(self, text: str):
        response_cleaned = text.replace("null(", "", 1).replace(r");", "", 1)
        json = loads(response_cleaned)
        return json["valoresHorariosGeneracion"]

    def _timestamp(self, date_str, timezone):
        return get(date_str + " " + timezone, "YYYY-MM-DD HH:mm ZZZ")

    def _searchdate(self, timezone, arrow=None):
        if not arrow:
            arrow = utcnow()
        return arrow.to(timezone).format("YYYY-MM-DD")
