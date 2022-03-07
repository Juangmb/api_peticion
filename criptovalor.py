import requests

endpoint =  "https://rest.coinapi.io/v1/exchangerate/{}/{}?apikey=73FCB3D2-DDDE-46FB-A5C8-F507C0504765"

moneda_from = input("Moneda de origen: ")

moneda_to = input("Moneda a conseguir: ")

r = requests.get(endpoint.format(moneda_from, moneda_to))
print(r.json())
print(r.status_code)
print(round(r.json()["rate"], 2))