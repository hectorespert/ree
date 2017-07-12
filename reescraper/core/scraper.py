from arrow import get
from requests import Session
from re import sub
from json import loads


class Scraper:

    def __init__(self, session=None):
        if session and isinstance(session, Session):
            self.session = session
        else:
            self.session = Session()

    def _getjson(self, url):
        response = self.session.request("GET", self.url)
        removed_null = sub("null\(", "", response.text)
        response_cleaned = sub("\);", "", removed_null)
        json = loads(response_cleaned)
        return json['valoresHorariosGeneracion']

    def _timestamp(self, date_str, timezone):
        return get(date_str + ' ' + timezone, 'YYYY-MM-DD HH:mm ZZZ')

