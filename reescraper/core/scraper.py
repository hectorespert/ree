from selenium import webdriver
from os import path
from bs4 import BeautifulSoup
from arrow import get


class Scraper:

    def __init__(self, driver=None):
        if driver:
            self.driver = driver
        else:
            self.driver = webdriver.PhantomJS(service_log_path=path.devnull)
        self.html = None

    def _gethtml(self, url):
        self.driver.get(url)
        self.html = BeautifulSoup(self.driver.page_source, 'html.parser')

    def _rows(self):
        if not self.html:
            return None
        else:
            return self.html.find_all('tr', class_='ng-scope')

    def _cells(self, row):
        return row.find_all('td', class_='ng-scope ng-binding')

    def _timestamp(self, date_str, timezone):
        return get(date_str + ' ' + timezone, 'YYYY-MM-DD HH:mm ZZZ')

