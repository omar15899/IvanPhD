import os
import time
import pickle
import subprocess
import requests
import random
import pandas as pd

# Hacemos una importación relativa, primero volvemos hacia
# atrás y después importamos todo de la carpeta PreScrapping
from .. import PreScrapping
from PreScrapping import *

# otra forma sería from PreScrapping.mapping import * o alguna de las variantes


class Scrapping(Mapping):
    def __init__(self, df: pd.DataFrame, directory: str = os.getcwd()) -> None:
        super().__init__(df, directory)

    @staticmethod
    def tratamiento_post_scrapping():
        """
        Una vez tenemos las listas cuyos elementos son json con los datos de cada una
        de las requests mandadas, se genera un procesamiento de cada uno de los archivos
        para tener un único json con toda la información de cada una de las imágenes.
        """
        
        '''
        Pasos:
        1. Crear un programita para ir descargando todas las imágenes e ir descargándolas
        en sus respectivas carpetas. Tienen que tener como metadato su mediaId que encontramos
        en el JSON de extracciones.
        2. 
        '''

        pass

    @staticmethod
    def restart_tor():
        # Detenemos el servicio Tor
        subprocess.run(["brew", "services", "stop", "tor"], check=True)
        # Iniciamos el servicio Tor
        subprocess.run(["brew", "services", "start", "tor"], check=True)

    @staticmethod
    def scrapping(
        row: pd.Series | dict,
        nombre_carpeta: str,
        nombre_directorio: str = os.path.dirname(__file__)
        ) -> None:
        """'
        Función que hace el request a la API de tripadvisor para obtener
        todos los valores e ir devolviendolos en la lista. El formato de
        entrada tiene que tener un Series con los indices de los elementos
        siendo las columnas del excel que ha hecho ivan en tripadvisor
        formateado o un diccionario con las mismas características.
        """
        # Comprobamos que efectivamente tenemos todas las columnas que necesitamos:
        columnas = ["Enlace", "Elemento1", "Nº fotos"]

        # if isinstance(row, pd.Series):
        #     num_presentes = row.index.isin(columnas).sum()
        #     if num_presentes < 3:
        #         raise Exception(
        #             "No se han incluido los parámetros mínimos para poder realizar el Scrapping."
        #         )
        # elif isinstance(row, dict):
        #     list(row.keys())

        # Extraemos info importante de las columnas:
        name_fichero = row["Elemento1"] + ".pkl"
        n_fotos = row["Nº fotos"]
        enlace = row["Enlace"]
        # Expresión regular para encontrar el patrón '-d' seguido de uno o más dígitos
        patron = r"-d(\d+)"
        # Buscar el patrón en la URL
        resultado = re.search(patron, enlace)
        if not resultado:
            raise Exception("No se ha encontrado el locationid en el enlace")
        locationid = resultado.group(1)
        # El locationid se obiene siempre del link y va después del -d primero que encuentre

        # Configuramos la sesión de requests para utilizar el proxy de Tor
        session = requests.session()
        session.proxies = {
            "http": "socks5h://localhost:9050",
            "https": "socks5h://localhost:9050",
        }

        # Hallamos los valores que vamos a incluir en el request del servidor, se trata de un post porque
        # se escribe en el servidor esta información para tener un registro de quien extrae los datos:
        DATA_URL = "https://www.tripadvisor.es/data/graphql/ids"
        PAYLOAD = [
            {
                "variables": {
                    "locationId": locationid,
                    "albumId": -160,
                    "subAlbumId": -160,
                    "client": "ar",
                    "dataStrategy": "ar",
                    "filter": {"mediaGroup": "ALL_INCLUDING_RESTRICTED"},
                    "offset": 0,
                    "limit": 100,
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
            "Referer": enlace,
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "same-origin",
            "Sec-Fetch-Site": "same-origin",
            # Asegúrate de actualizar las cookies a las que sean pertinentes para tu sesión o necesidades específicas
            "Cookie": "_lr_env_src_ats=false; _lr_retry_request=true; ...",
        }

        # Procedemos a hacer el scrapping:

        offset = PAYLOAD[0]["variables"]["offset"]
        lista_total = []  # Lista para acumular los resultados de cada extracción
        contador_errores_request = 0

        # Creamos un folder con el nombre si no existe y un archivo vacío, reescribimos
        # el name_fichero con la enumeración pertinente que esté habilitada en ese folder:
        name_fichero = Scrapping._crear_carpeta_archivo_en_ubicacion_script(
            nombre_carpeta= nombre_carpeta,
            nombre_directorio= nombre_directorio,
            nombre_archivo = name_fichero,
        )
        # Abrimos el archivo (no lo creamos porque ya se ha creado en la función previa)
        f = open(name_fichero, "wb")
        while True:
            time.sleep(2 * random.random())
            try:
                response = session.post(DATA_URL, headers=headers, json=PAYLOAD).json()
                lista_total.append(response[0])
                # Serializar y guardar la lista total en un archivo con el conteo de errores
                pickle.dump((lista_total, contador_errores_request), f)
            except:
                contador_errores_request += 1
                continue

            offset += PAYLOAD[0]["variables"]["limit"]
            if (
                offset > n_fotos
            ): 
                break
        f.close()
        print(
            f"Extracción realizada con éxito con {contador_errores_request} errores para {n_fotos}."
        )

    def scrap_everything(self):
        """'
        Esta función hará todo el trabajo importante relacionado con el scrapping,
        hará todos los cálculos importantes y acto seguido pasará a guardarlos en
        carpetas de un fichero en concreto.
        """
        df = self.df

        # Limpiamos todos los monumentos que no tengan links definidos
        df = df[~pd.isna(df["Enlace"])]

        lista_errores_scrapping = []
        # Recorremos todos los enlaces de la lista recorriendo toda la lista y aplicamos
        # la función de scrapping:
        for index, row in df.iterrows():
            # Reiniciamos tor para cada scrapping, esto facilitará las cosas para que no rastreen
            Scrapping.restart_tor()
            time.sleep(10)
            # Salvo error, se generarán todos los scrappings pertinentes.
            try:
                Scrapping.scrapping(
                    row = row,
                    nombre_carpeta='Fichero_Scrapping',
                    nombre_directorio= self.directory
                    )
            except:
                lista_errores_scrapping.append(row["Elemento1"])
                print(f'Error en elemento {row['Elemento1']}')
                continue