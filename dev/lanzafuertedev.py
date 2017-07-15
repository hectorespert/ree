from reescraper import Lanzarote, Fuerteventura, LanzaroteFuerteventura
from requests import Session

session = Session()

generation = Lanzarote(session).get()
print(generation)

generation = Fuerteventura(session).get()
print(generation)

generation = LanzaroteFuerteventura(session).get()
print(generation)
