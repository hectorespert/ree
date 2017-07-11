from selenium import webdriver
from os import path


class Scrapper:

    def __init__(self):
        self.driver = webdriver.PhantomJS(service_log_path=path.devnull)

