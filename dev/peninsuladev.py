from reescraper import IberianPeninsula

response = IberianPeninsula().get()
print(response)


responses = IberianPeninsula().get(None, False)
for response in responses:
    print(response)
