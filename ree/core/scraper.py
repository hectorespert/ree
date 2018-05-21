from arrow import get, utcnow
from requests import Session
from re import sub
from json import loads
from operator import attrgetter
from ..response import Response
from .exceptions import ResponseCodeException, ResponseDataException


class Scraper(object):

    def __init__(self, session=None, verify=True):
        self.verify = verify
        if session and isinstance(session, Session):
            self.session = session
        else:
            self.session = Session()

    def get(self, zone, timezone, system="Canarias", date=None, last=True):
        if not date:
            date = self._searchdate(timezone)
        url = self._makeurl(zone, date, system)
        responses = []
        for value in self._request(url):
            ts = value['ts']
            arrow = self._timestamp(ts, timezone)
            response = Response(arrow.float_timestamp)
            if 'dem' in value:
                response.demand = value['dem']
            if 'nuc' in value:
                response.nuclear = value['nuc']
            if 'die' in value:
                response.diesel = value['die']
            if 'gas' in value:
                response.gas = value['gas']
            if 'gf' in value:
                response.gas = value['gf']
            if 'eol' in value:
                response.wind = value['eol']
            if 'cc' in value:
                response.combined = value['cc']
            if 'vap' in value:
                response.vapor = value['vap']
            if 'fot' in value:
                response.solar = value['fot']
            if 'sol' in value:
                response.solar = value['sol']
            if 'hid' in value:
                response.hydraulic = value['hid']
            if 'car' in value:
                response.carbon = value['car']
            if 'termRenov' and 'cogenResto' in value:
                response.other = value['termRenov'] + value['cogenResto']
            if 'cb' in value:
                response.link['pe_ma'] = value['cb']
            if 'icb' in value:
                response.link['pe_ma'] = value['icb']
            if 'emm' in value:
                response.link['ma_me'] = value['emm']
            if 'emi' in value:
                response.link['ma_ib'] = value['emi']
            if 'eif' in value:
                response.link['ib_fo'] = value['eif']
            if 'inter' in value:
                response.link['int'] = value['inter']
            responses.append(response)
        if last:
            return max(responses, key=attrgetter('timestamp'))
        else:
            return responses

    def _request(self, url):
        response = self.session.request("GET", url, verify=self.verify)
        if response.status_code != 200:
            raise ResponseCodeException
        if not response.text:
            raise ResponseDataException
        return self.__getjson(response.text)

    def _makeurl(self, zone, date, system="Canarias"):
        base = "https://demanda.ree.es/WSvisionaMoviles{2}Rest/resources/demandaGeneracion{2}?curva={0}&fecha={1}"
        return base.format(zone, date, system)

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

