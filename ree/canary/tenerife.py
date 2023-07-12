from typing import Union

from ree.core import Scraper


class Tenerife(Scraper):
    def __init__(self, session=None, verify=True):
        super(self.__class__, self).__init__(session, verify)

    def get(self, date: Union[str, None] = None, last=True):
        return super(self.__class__, self).get(
            "TENERIFE5M", "Atlantic/Canary", "Canarias", date, last
        )

    def get_all(self, date: Union[str, None] = None):
        return super(self.__class__, self).get_all(
            "TENERIFE5M", "Atlantic/Canary", "Canarias", date
        )
