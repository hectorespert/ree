from arrow import get, utcnow
from requests import Session
from re import sub
from json import loads
from operator import attrgetter
from ..response import Response
from .exceptions import ResponseCodeException, ResponseDataException


class Scraper(object):

    def __init__(self, session=None):
        if session and isinstance(session, Session):
            self.session = session
        else:
            self.session = Session()

    def get(self, zone, timezone, date=None):
        if not date:
            date = self._searchdate(timezone)
        url = self._makeurl(zone, date)
        responses = []
        for value in self._request(url):
            ts = value['ts']
            arrow = self._timestamp(ts, timezone)
            response = Response(arrow.float_timestamp)
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

    def _request(self, url):
        response = self.session.request("GET", url)
        if response.status_code != 200:
            raise ResponseCodeException
        if not response.text:
            raise ResponseDataException
        return self.__getjson(response.text)

    def _makeurl(self, zone, date):
        base = "https://demanda.ree.es/WSvisionaMovilesCanariasRest/resources/demandaGeneracionCanarias?curva={0}&fecha={1}"
        return base.format(zone, date)

    def __getjson(self, text):
        removed_null = sub("null\(", "", text)
        response_cleaned = sub("\);", "", removed_null)
        json = loads(response_cleaned)
        return json['valoresHorariosGeneracion']

    def _timestamp(self, date_str, timezone):
        return get(date_str + ' ' + timezone, 'YYYY-MM-DD HH:mm ZZZ')

    def _searchdate(self, timezone, arrow=None):
        if not arrow:
            arrow = utcnow()
        return arrow.to(timezone).format('YYYY-MM-DD')



