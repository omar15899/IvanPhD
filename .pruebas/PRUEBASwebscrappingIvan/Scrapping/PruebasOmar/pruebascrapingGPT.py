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
PAYLOAD = {
    "wss_url": "wss://chatgpt-async-webps-prod-southcentralus-5.webpubsub.azure.com/client/hubs/conversations?access_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJodHRwczovL2NoYXRncHQtYXN5bmMtd2VicHMtcHJvZC1zb3V0aGNlbnRyYWx1cy01LndlYnB1YnN1Yi5henVyZS5jb20vY2xpZW50L2h1YnMvY29udmVyc2F0aW9ucyIsImlhdCI6MTcxMDcyNjgzMCwiZXhwIjoxNzEwNzMwNDMwLCJzdWIiOiJ1c2VyLW9INWRzSHdoOHlGcEt1dEd6eVJQbjNTOCIsInJvbGUiOlsid2VicHVic3ViLmpvaW5MZWF2ZUdyb3VwLnVzZXItb0g1ZHNId2g4eUZwS3V0R3p5UlBuM1M4Il0sIndlYnB1YnN1Yi5ncm91cCI6WyJ1c2VyLW9INWRzSHdoOHlGcEt1dEd6eVJQbjNTOCJdfQ.cP9TIpUPCVpVTbfh_dA5T-O6_FFLK7Zq_80uky6AUzs",
    "expires_at": "2024-03-18T02:53:50.996572+00:00",
    "conversation_id": "d81e8b21-1028-457c-80a7-4b9e99852407",
    "response_id": "8661976288295e1f-MAD",
    "websocket_request_id": "853fadb7-f8c7-4a0e-b23d-779ca59a46ec",
}

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
lista_total = []  # Lista para acumular los resultados

while True:
    time.sleep(2)
    PAYLOAD[0]["variables"]["offset"] = offset
    try:
        response = session.post(DATA_URL, headers=headers, json=PAYLOAD).json()
        lista_total.append(
            response
        )  # Asume que quieres guardar la respuesta en la lista
        print(response)  # Imprimir la respuesta o procesarla como necesites
    except:
        continue

    offset += 40
    if offset > 20000:  # Condición de salida modificable según la lógica deseada
        break

# Serializar y guardar la lista total en un archivo
with open("lista_total.pkl", "wb") as f:
    pickle.dump(lista_total, f)
