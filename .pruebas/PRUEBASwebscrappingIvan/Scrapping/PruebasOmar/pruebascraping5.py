import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import time
import pickle

# Configuración de la sesión de requests para utilizar el proxy de Tor
session = requests.Session()
session.proxies = {
    "http": "socks5h://localhost:9050",
    "https": "socks5h://localhost:9050",
}

# Política de reintento con backoff exponencial
retries = Retry(total=5, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
session.mount("http://", HTTPAdapter(max_retries=retries))
session.mount("https://", HTTPAdapter(max_retries=retries))

# Configuraciones iniciales
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
            "offset": 0,
            "limit": 20,
        },
        "extensions": {"preRegisteredQueryId": "2d46abde60a014b0"},
    }
]

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15",
    # Considera cambiar o rotar el User-Agent y limpiar las cookies para cada solicitud
    # Omitir las cookies si no son necesarias para la solicitud
}

lista_total = []  # Lista para acumular los resultados
offset = 0

while True:
    time.sleep(2)
    PAYLOAD[0]["variables"]["offset"] = offset
    try:
        response = session.post(DATA_URL, headers=headers, json=PAYLOAD).json()
        lista_total.append(response)  # Añadir la respuesta a la lista
        with open("lista_total.pkl", "wb") as f:
            pickle.dump(lista_total, f)  # Guardar la lista actualizada en el archivo
        print(response)  # Imprimir la respuesta o procesarla como necesites
    except Exception as e:
        print(f"Error durante la solicitud: {e}")
        continue

    offset += 20  # Ajustar el offset basado en la paginación deseada
    if offset > 20000:  # Condición de salida
        break
