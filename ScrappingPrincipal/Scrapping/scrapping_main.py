import os
import time
import pickle
import subprocess
import requests
import random
import base64
import json
import pandas as pd
from typing import List, Dict, Tuple, Union, Optional


# Hacemos una importación relativa, primero volvemos hacia
# atrás y después importamos todo de la carpeta PreScrapping
# from .. import PreScrapping
# from PreScrapping import *

# Como el script que utilice esta librería va a tener si o si 
# en el path el directorio principal de todos, podemos hacer
# una importación absoluta, aunque esto va a impedir poder
# ejecutar el código desde aquí si no anadimos al PATH la ubicación
# de la librería ScrappingPrincipal. Pero es así como se escriben las liberías
# profesionales:
from ScrappingPrincipal.PreScrapping import *

# otra forma sería from PreScrapping.mapping import * o alguna de las variantes


class Scrapping(Mapping):
    def __init__(
            self, 
            df: pd.DataFrame, 
            directory: str = os.getcwd(), 
            name_folder: str = 'Fichero_Scrapping'
            ) -> None:
        '''
        name_folder_scrapping me permite elegir el nombre del fichero de scrapping que vamos a 
        querer utilizar. 
        '''
        super().__init__(df, directory, name_folder)

    
    @staticmethod
    def restart_tor():
        '''
        Función que reinicia el servicio Tor desde el terminal de dispositivos macOS.
        '''
        subprocess.run(["brew", "services", "stop", "tor"], check=True)
        subprocess.run(["brew", "services", "start", "tor"], check=True)
        
    @staticmethod
    def photo_b64downloader(url: str) -> str:
        """
        Descarga una foto de una URL y la decodifica a un str base64.
        """
        # Descargamos la foto
        response = requests.get(url)
        # Decodificamos la foto a base64
        return base64.b64encode(response.content).decode()
        
    @staticmethod
    def json_extractor(
        data: Union[List, Dict, Tuple],
        result: Optional[List] = None,
        iteration: int = 0,
        max_iterations: int = 5,
    ) -> Optional[List]:
        """
        Función que trabaja la devolución del request, que es un json no estructurado 
        y lo convierte en una lista de jsons donde está la información al completo de 
        cada una de las imágenes.
        """
        if result is None:
            result = []

        if iteration >= max_iterations:
            return

        if isinstance(data, list):
            for item in data:
                Scrapping.json_extractor(item, result, iteration=iteration + 1)

        elif isinstance(data, tuple):
            for item in data:
                Scrapping.json_extractor(item, result, iteration=iteration + 1)

        elif isinstance(data, dict):
            for key, value in data.items():
                if key in ["data", "mediaAlbumPage"]:
                    Scrapping.json_extractor(value, result, iteration=iteration + 1)
                elif key == "mediaList":
                    if isinstance(value, list):
                        result.extend(value)
                    Scrapping.json_extractor(value, result, iteration=iteration + 1)
                else:
                    Scrapping.json_extractor(value, result, iteration=iteration + 1)

        if iteration == 0:
            return result

    @staticmethod
    def scrapper(
        row: pd.Series | dict,
        nombre_carpeta: str,
        nombre_directorio: str = os.path.dirname(__file__)
        ) -> None:
        """
        Realiza una solicitud a la API de TripAdvisor para obtener datos.

        Esta función realiza el trabajo principal relacionado con el web scraping. 
        Realiza cálculos importantes y luego guarda los resultados en carpetas de un archivo específico.

        Args:
            row (Union[pd.Series, dict]): Un pandas Series o un diccionario que contiene los datos a raspar.
                Debe tener los índices de los elementos como las columnas del excel que ha hecho Ivan en TripAdvisor
                formateado o un diccionario con las mismas características.
            nombre_carpeta (str): El nombre de la carpeta donde se guardarán los datos raspados.
            nombre_directorio (str, optional): La ruta del directorio donde se encuentra el archivo. 
                Por defecto es el directorio del archivo actual.

        Raises:
            Exception: Si no se incluyen los parámetros mínimos para realizar el web scraping.

        Returns:
            None
        
        Función que hace el request a la API de tripadvisor para obtener
        todos los valores e ir devolviendolos en la lista. El formato de
        entrada tiene que tener un Series con los indices de los elementos
        siendo las columnas del excel que ha hecho ivan en tripadvisor
        formateado o un diccionario con las mismas características.
    
        Esta función hará todo el trabajo importante relacionado con el scrapping,
        hará todos los cálculos importantes y acto seguido pasará a guardarlos en
        carpetas de un fichero en concreto.
        """
        
        # Extraemos info importante de las columnas:
        name_fichero = row["Elemento1"]
        n_fotos = row["Nº fotos"]
        enlace = row["Enlace"]
        # Expresión regular para encontrar el patrón '-d' seguido de uno o más dígitos
        patron = r"-d(\d+)"
        # Buscamos el patrón en la URL
        resultado = re.search(patron, enlace)
        if not resultado:
            raise Exception("No se ha encontrado el locationid en el enlace")
        locationid = int(resultado.group(1))
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
                    "limit": 40,
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

        # Creamos un folder con el nombre si no existe
        Scrapping._crear_carpeta_archivo_en_ubicacion_script(
            nombre_carpeta= nombre_carpeta,
            nombre_directorio= nombre_directorio,
        )
        
        # Procedemos a hacer el scrapping:
        resultado_total, resultado_parcial = [], []
        contador_errores_request = 0
        
        # Empezamos con el bucle, cada 400 imágenes vamos a crear un nuevo archivo:
        contador_fichero, contador_photos= 1,0
        while True:
            print(f"Extrayendo {contador_photos} fotos de {n_fotos} para {name_fichero}...")
            time.sleep(2 *random.random())
            try:
                response = session.post(DATA_URL, headers=headers, json=PAYLOAD)
                response.raise_for_status()
                json_response = response.json()
                
                Scrapping.json_extractor(json_response, resultado_parcial)
                # resultado_total.extend(resultado_parcial)
                contador_photos += PAYLOAD[0]["variables"]["limit"]
            except Exception as e:
                contador_errores_request += 1
                print(f"{e}")
                continue
            
            if contador_photos > 5000:
                file_name = os.path.join(nombre_directorio, nombre_carpeta, name_fichero + f"_{contador_fichero}" + ".json")
                with open(file_name, "w") as stream:
                    json.dump(resultado_parcial, stream, indent=4)
                    # Vaciamos el resultado parcial y añadimos un nuevo numero al contador de ficheros:
                    resultado_parcial = []
                    contador_fichero += 1
                    contador_photos = 0

            PAYLOAD[0]["variables"]["offset"] += (PAYLOAD[0]["variables"]["limit"] + 1)
            if (
                PAYLOAD[0]["variables"]["offset"] >= n_fotos
            ): 
                break
            
        if resultado_parcial:
            file_name = os.path.join(nombre_directorio, nombre_carpeta, name_fichero + f"_{contador_fichero}" + ".json")
            with open(file_name, "w") as stream:
                json.dump(resultado_parcial, stream, indent=4)
                
        # # Guardamos el archivo json total:
        # file_name = os.path.join(nombre_directorio, nombre_carpeta, name_fichero + ".json") 
        # try:
        #     with open(file_name, "w") as stream:
        #         json.dump(resultado_total, stream, indent=4)
        # except Exception as e:
        #     print(f"Error al guardar el archivo {name_fichero}. {e}")

        print(
            f"Extracción realizada con éxito con {contador_errores_request} errores para {name_fichero}."
        )

    def scrap_everything(self):
        ''' 
        Función que realiza el scrapping sobre todos los elementos del fichero. Cuando salgamos de este
        fichero vamos a tener gran parte del trabajo hecho. 
        '''

        # Limpiamos todos los monumentos que no tengan links definidos
        df = self.df[~pd.isna(self.df["Enlace"])] 

        lista_errores_scrapping = []
        # Recorremos todos los enlaces de la lista recorriendo toda la lista y aplicamos
        # la función de scrapping:
        for index, row in df.iterrows():
            # Reiniciamos tor para cada scrapping, esto facilitará las cosas para que no rastreen
            # Scrapping.restart_tor()
            # Vemos la ip que estamos utilizando en tor:
            print('IP actual:', requests.get('http://httpbin.org/ip').text)
            time.sleep(2 * random.random())
            # Salvo error, se generarán todos los scrappings pertinentes.
            try:
                Scrapping.scrapper(
                    row = row,
                    nombre_carpeta=self.name_folder,
                    nombre_directorio= self.directory
                    )
            except:
                lista_errores_scrapping.append(row["Elemento1"])
                print(f'Error en elemento {row['Elemento1']}')
                continue
            
        # Creamos un archivo para guardar los elementos que no se han scrappeado bien:
        texto = '\n'.join(lista_errores_scrapping)
        ruta_archivo = Scrapping._crear_carpeta_archivo_en_ubicacion_script(
            nombre_carpeta=self.name_folder,
            nombre_directorio= self.directory,
            nombre_archivo='monumentos_no_scrappeados.txt',
        )
        with open(ruta_archivo, 'w') as stream:
            stream.write(texto)

