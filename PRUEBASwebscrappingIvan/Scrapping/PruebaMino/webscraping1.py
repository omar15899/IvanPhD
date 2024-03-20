import requests

DATA_URL = "https://www.tripadvisor.es/data/graphql/ids"
REQ_LIMIT = 40
LOCATION_ID = 191050
PAYLOAD = [
    {
        "variables": {
            "locationId": LOCATION_ID,
            "albumId": -160,
            "subAlbumId": -160,
            "client": "ar",
            "dataStrategy": "ar",
            "filter": {"mediaGroup": "ALL_INCLUDING_RESTRICTED"},
            "limit": REQ_LIMIT,
        },
        "extensions": {"preRegisteredQueryId": "2d46abde60a014b0"},
    }
]
# Ejemplo de User-Agent de Safari
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15"
}


offset = 0


def get_media_list(response) -> list:
    return response["data"]["mediaAlbumPage"]["mediaList"]


# while True:
#     PAYLOAD[0]["offset"] = offset

#     response = requests.post(DATA_URL, json=PAYLOAD).json()

#     if not get_media_list(response):
#         break
#     print(response)
#     break
#     offset += 20

PAYLOAD[0]["offset"] = 0
response = requests.post(DATA_URL, json=PAYLOAD, headers=headers)
