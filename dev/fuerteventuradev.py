from requests import Session
from reescraper import Fuerteventura
session = Session()

generation = Fuerteventura(session).get()
print(generation)
