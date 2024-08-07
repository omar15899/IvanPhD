import requests


def get_media_list(response) -> list:
    """Extrae la lista de medios de la respuesta."""
    try:
        return response["data"]["mediaAlbumPage"]["mediaList"]
    except KeyError:
        return []


# Configurar la sesión de requests para utilizar el proxy de Tor
session = requests.session()
session.proxies = {
    "http": "socks5h://localhost:9050",
    "https": "socks5h://localhost:9050",
}

# Ajustes iniciales
DATA_URL = "https://www.tripadvisor.es/data/graphql/ids"
offset = 0

PAYLOAD = [
    {
        "variables": {
            "locationId": 190146,
            "albumId": -160,
            "subAlbumId": -160,
            "client": "ar",
            "dataStrategy": "ar",
            "filter": {"mediaGroup": "ALL_INCLUDING_RESTRICTED"},
            "offset": 0,  # Inicialmente configurado a 0
            "limit": 20,
        },
        "extensions": {"preRegisteredQueryId": "2d46abde60a014b0"},
    }
]

# Ejemplo de User-Agent de Safari (opcional)
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15"
}

while offset <= 100:
    offset += 20  # Incrementa el offset para la siguiente solicitud
    PAYLOAD[0]["variables"]["offset"] = offset

    try:
        response = session.post(DATA_URL, json=PAYLOAD, headers=headers).json()
        media_list = get_media_list(response)
        if not media_list:
            break
    except requests.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")
        break

print(response)
