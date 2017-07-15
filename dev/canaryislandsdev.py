from reescraper import CanaryIslands

response = CanaryIslands().get()
print(response)

print(response.demand)
print(response.production())
print(response.storage)
print(response.links())
print(response.unknown())
