from reescraper import BalearicIslands

response = BalearicIslands().get()
print(response)

print(response.demand)
print(response.production())
print(response.links())
print(response.unknow())
