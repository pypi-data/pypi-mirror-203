from pyfobal import Client

pyfobal = Client("api_key")
leagues = pyfobal.get_leagues()
print(leagues)
