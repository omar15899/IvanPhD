import requests
import subprocess


def restart_tor():
    """
    Función que reinicia el servicio Tor desde el terminal de dispositivos macOS.
    """
    subprocess.run(["brew", "services", "stop", "tor"], check=True)
    subprocess.run(["brew", "services", "start", "tor"], check=True)


# Generamos el payload:
headers = {
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
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15",
}


# iniciamos una session de request:
response = requests.post(
    "https://www.tripadvisor.es/data/graphql/ids",
    headers=headers,
    json={
        "variables": {
            "locationId": 190146,
            "albumId": -160,
            "subAlbumId": -160,
            "client": "ar",
            "dataStrategy": "ar",
            "filter": {"mediaGroup": "ALL_INCLUDING_RESTRICTED"},
            "offset": 0,
            "limit": 150,
        }
    },
)

# Obtenemos el json de la respuesta:
json_response = response.json()

# Imprimimos resultado
print(json_response)

# Generamos una lista con todas lass imágenes y calculamos límites:
