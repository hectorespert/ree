from reescraper import Mallorca

response = Mallorca().get()
print(response)

print(response.link['pe_ma'])

print(response.link['ma_me'])

print(response.link['ma_ib'])

print(response.link['ib_fo'])