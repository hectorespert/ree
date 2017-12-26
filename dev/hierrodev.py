from reescraper import ElHierro

response = ElHierro().get()
print(response)

response = ElHierro().get_all()
print(response)
