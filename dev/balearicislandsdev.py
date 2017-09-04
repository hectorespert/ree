from reescraper import BalearicIslands
from requests import Session

session = Session()
response = BalearicIslands(session).get()
print(response)

print(response.demand)
print(response.production())
print(response.links())
print(response.unknown())

response = BalearicIslands(session).get_all()
print(response)
