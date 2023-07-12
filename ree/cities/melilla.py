from typing import Union

from requests import Session

from ..core import Scraper


class Melilla(Scraper):
    def __init__(self, session: Union[Session, None] = None, verify=True):
        super(self.__class__, self).__init__(session, verify)

    def get(self, date: Union[str, None] = None, last=True):
        return super(self.__class__, self).get(
            "MELILLA5M", "Africa/Ceuta", "Peninsula", date, last
        )

    def get_all(self, date: Union[str, None] = None):
        return super(self.__class__, self).get_all(
            "MELILLA5M", "Africa/Ceuta", "Peninsula", date
        )
