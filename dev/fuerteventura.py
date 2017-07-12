from reescraper import GenerationFuerteventura
from selenium import webdriver
from os import path

driver = webdriver.PhantomJS(service_log_path=path.devnull)

generation = GenerationFuerteventura(driver).get()
print(generation)
