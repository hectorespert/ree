from selenium import webdriver
from os import path
from bs4 import BeautifulSoup


class Scrapper:

    def __init__(self):
        self.driver = webdriver.PhantomJS(service_log_path=path.devnull)

    def _gethtml(self, url):
        self.driver.get(url)
        return BeautifulSoup(self.driver.page_source, 'html.parser')

    def _getrows(self, soup):
        return soup.find_all('tr', class_='ng-scope')

    def _getcells(self, value):
        return value.find_all('td', class_='ng-scope ng-binding')

