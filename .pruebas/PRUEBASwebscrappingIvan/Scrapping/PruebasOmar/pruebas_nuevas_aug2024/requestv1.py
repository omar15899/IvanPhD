from typing import List, Dict, Tuple, Union, Optional
from collections import deque
import requests
import subprocess
import json
import time
import random


def restart_tor():
    subprocess.run(["brew", "services", "stop", "tor"], check=True)
    subprocess.run(["brew", "services", "start", "tor"], check=True)


def extractor(
    data: Union[List, Dict, Tuple],
    result: Optional[List] = None,
    iteration: int = 0,
    max_iterations: int = 5,
) -> Optional[List]:
    if result is None:
        result = []

    if iteration >= max_iterations:
        return

    if isinstance(data, list):
        for item in data:
            extractor(item, result, iteration=iteration + 1)

    elif isinstance(data, tuple):
        for item in data:
            extractor(item, result, iteration=iteration + 1)

    elif isinstance(data, dict):
        for key, value in data.items():
            if key in ["data", "mediaAlbumPage"]:
                extractor(value, result, iteration=iteration + 1)
            elif key == "mediaList":
                if isinstance(value, list):
                    result.extend(value)
                extractor(value, result, iteration=iteration + 1)
            else:
                extractor(value, result, iteration=iteration + 1)

    if iteration == 0:
        return result


# Forma más elegante y beloz


def json_extractor(
    data: Union[List, Dict, Tuple], max_iterations: int = 5
) -> Optional[List]:
    """
    Función que trabaja la devolución del request, que es un json no estructurado
    y lo convierte en una lista de jsons donde está la información al completo de
    cada una de las imágenes.
    """

    # Inicializamos la pila de trabajo con la data inicial
    stack = deque(
        [(data, 0)]
    )  # Usamos una deque como pila (stack), donde cada elemento es una tupla (data, depth)
    result = []

    while stack:
        current_data, depth = stack.pop()

        if depth >= max_iterations:
            continue

        if isinstance(current_data, list):
            for item in current_data:
                stack.append((item, depth + 1))

        elif isinstance(current_data, tuple):
            for item in current_data:
                stack.append((item, depth + 1))

        elif isinstance(current_data, dict):
            for key, value in current_data.items():
                if key == "mediaList":
                    if isinstance(value, list):
                        result.extend(value)
                    stack.append((value, depth + 1))
                else:
                    stack.append((value, depth + 1))

    return result if result else None


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
    "Cookie": "_lr_env_src_ats=false; _lr_retry_request=true; ...",
}

offset = 0
fragment_id = 0
resultadototal = []
while offset < 300:
    time.sleep(2 * random.random())
    payload = [
        {
            "variables": {
                "locationId": 190146,
                "albumId": -160,
                "subAlbumId": -160,
                "client": "ar",
                "dataStrategy": "ar",
                "filter": {"mediaGroup": "ALL_INCLUDING_RESTRICTED"},
                "offset": offset,
                "limit": 40,
            },
            "extensions": {"preRegisteredQueryId": "2d46abde60a014b0"},
        },
    ]
    try:
        response = requests.post(
            "https://www.tripadvisor.es/data/graphql/ids", headers=headers, json=payload
        )
        response.raise_for_status()

        json_response = response.json()
        print(f"Procesando fragmento {fragment_id} con offset {offset}...")

        resultado = extractor(json_response)
        resultadototal.extend(resultado)

        # Guardar cada fragmento en un archivo separado
        with open(
            f"/Users/omarkhalil/Desktop/Universidad/IvanPhD/Programacion/.pruebas/PRUEBASwebscrappingIvan/Scrapping/PruebasOmar/pruebas_nuevas_aug2024/datos_requestv1/Palacio_Real_fragmento_{fragment_id}.json",
            "w",
        ) as f:
            json.dump(resultado, f, indent=4)

        fragment_id += 1

    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud: {e}")

    offset += 41

# print(len(resultadototal))
# print(resultadototal)
