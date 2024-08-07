import requests
import time
import pickle

# Configurar la sesión de requests para utilizar el proxy de Tor
session = requests.session()
session.proxies = {
    "http": "socks5h://localhost:9050",
    "https": "socks5h://localhost:9050",
}

# Ajustes iniciales
DATA_URL = "https://www.tripadvisor.es/data/graphql/ids"
PAYLOAD = [
    {
        "variables": {
            "locationId": 190146,
            "albumId": -160,
            "subAlbumId": -160,
            "client": "ar",
            "dataStrategy": "ar",
            "filter": {"mediaGroup": "ALL_INCLUDING_RESTRICTED"},
            "offset": 23000,
            "limit": 10,
        },
        "extensions": {"preRegisteredQueryId": "2d46abde60a014b0"},
    }
]

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-GB,en;q=0.9",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Host": "www.tripadvisor.es",
    "Origin": "https://www.tripadvisor.es",
    "Referer": "https://www.tripadvisor.es/Attraction_Review-g187514-d190146-Reviews-Royal_Palace_of_Madrid-Madrid.html",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "same-origin",
    "Sec-Fetch-Site": "same-origin",
    # Asegúrate de actualizar las cookies a las que sean pertinentes para tu sesión o necesidades específicas
    "Cookie": "_lr_env_src_ats=false; _lr_retry_request=true; ...",
}


offset = PAYLOAD[0]["variables"]["offset"]
lista_total = []  # Lista para acumular los resultados de cada extracción
cont = 0
while True:
    cont += 1
    time.sleep(2)
    try:
        response = session.post(DATA_URL, headers=headers, json=PAYLOAD).json()
        lista_total.append(response)
        print(response)
    except:
        continue

    offset += PAYLOAD[0]["variables"]["limit"]
    if cont > 2:  # Condición de salida modificable según la lógica deseada
        break


# Serializar y guardar la lista total en un archivo
with open("lista_total.pkl", "wb") as f:
    pickle.dump(lista_total, f)
