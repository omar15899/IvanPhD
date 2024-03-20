import requests
import time

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
            "offset": 0,
            "limit": 20,
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


offset = 0
while True:
    time.sleep(5)
    PAYLOAD[0]["variables"]["offset"] = offset

    response = requests.post(DATA_URL, headers=headers, json=PAYLOAD).json()

    # Suponiendo que existe una función para procesar la respuesta
    # y determinar si continuar o no...
    # if not alguna_condicion_para_continuar(response):
    #     break

    print(response)  # Imprimir la respuesta o procesarla como necesites

    offset += 20  # Incrementa el offset para la siguiente solicitud
    # Condición de salida del bucle, si es necesario
    if offset > 200:
        break  # Remover o modificar esta línea según la lógica deseada

print(response)


# import requests

# # Configurar la sesión de requests para utilizar el proxy de Tor
# session = requests.session()
# session.proxies = {
#     "http": "socks5h://localhost:9050",
#     "https": "socks5h://localhost:9050",
# }

# # Ajustes iniciales
# DATA_URL = "https://www.tripadvisor.es/data/graphql/ids"
# offset = 0

# PAYLOAD = [
#     {
#         "variables": {
#             "locationId": 190146,
#             "albumId": -160,
#             "subAlbumId": -160,
#             "client": "ar",
#             "dataStrategy": "ar",
#             "filter": {"mediaGroup": "ALL_INCLUDING_RESTRICTED"},
#             "offset": 0,  # Este valor se actualizará en el bucle
#             "limit": 20,
#         },
#         "extensions": {"preRegisteredQueryId": "2d46abde60a014b0"},
#     }
# ]

# # Configuración de headers basada en la petición proporcionada
# headers = {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Accept-Language": "en-GB,en;q=0.9",
#     "Connection": "keep-alive",
#     "Content-Type": "application/json",
#     "Host": "www.tripadvisor.es",
#     "Origin": "https://www.tripadvisor.es",
#     "Referer": "https://www.tripadvisor.es/Attraction_Review-g187514-d190146-Reviews-Royal_Palace_of_Madrid-Madrid.html",
#     "Sec-Fetch-Dest": "empty",
#     "Sec-Fetch-Mode": "same-origin",
#     "Sec-Fetch-Site": "same-origin",
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15",
# }

# # Configuración de cookies
# cookies = {
#     "_lr_env_src_ats": "false",
#     # Agrega aquí todas las cookies necesarias...
# }

# while True:
#     PAYLOAD[0]["variables"]["offset"] = offset

#     response = session.post(
#         DATA_URL, headers=headers, cookies=cookies, json=PAYLOAD
#     ).json()

#     # Suponiendo que existe una función para procesar la respuesta
#     # y determinar si continuar o no...
#     # if not alguna_condicion_para_continuar(response):
#     #     break

#     print(response)  # Imprimir la respuesta o procesarla como necesites

#     offset += 20  # Incrementa el offset para la siguiente solicitud
#     # Condición de salida del bucle, si es necesario
#     if offset > 100:
#         break  # Remover o modificar esta línea según la lógica deseada
