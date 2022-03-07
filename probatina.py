import requests

respuesta = requests.get("https://rest.coinapi.io/v1/exchangerate/BTC?apikey=73FCB3D2-DDDE-46FB-A5C8-F507C0504765")

print(respuesta.status_code)

data = respuesta.json()

print(data["rates"][3])