"""
El objetivo de este script es dejar un dataset con toda la información util con la que vamos a 
basarnos para enviar el prompt. Una vez enviemos el prompt, en otro script generaremos un dataset
con todas las imágenes y cada una de las imágenes tendrá ademaás todas estas columnas de este 
dataset (se vinculará en base al http del que fueron descargadas).
"""

import os
import inspect
import re
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter


class PreScrapping:
    def __init__(self, df: pd.DataFrame, directory: str = os.getcwd()) -> None:
        """
        directory es opcional, sirve para indicar dónde queremos que se generen
        las carpetas. En caso de que no escribamos nada las carpetas se generaran
        en el directorio desde donde se esté ejecutando el terminal.
        """
        self.df = df
        self.directory = directory
        self.df_prepared = self._preparacion_datos()
        self.df_coordenadas = None

    # --------------------------------------------------------------------------------------- Métodos para crear archivos
    """
    Estos métodos van a ser cruciales no solo en esta parte del código, si no también en el 
    scrapping puesto que estamos sistematizando una forma de crear archivos y carpetas en la 
    ubicación del script que nos va a permitir generar todas las carpetas que nos den la gana
    de una forma fácil y sencilla.

    ATENCIÓN: CONTENIDO_ARCHIVO PUEDE SER UN STR POR LOS JSON EN EL SCRAPPING. CONSTRUIRÉ ESA
    PARTE DEL CÓDIGO MÁS ADELANTE.
    """

    @staticmethod
    def _buscar_directorio_script() -> str | None:
        """
        Función que devuelve el directorio del script que llama a esta clase
        se encuentra ubicado. Para ello buscamos el frame o call stack de la
        función a la que está llamando dentro del script y de ahí substraemos
        la ubicación completa del script.
        """
        # Obtenemos el marco de llamada del antecesor del script actual:
        marco = inspect.currentframe()
        ruta_script = inspect.getfile(marco.f_back)

        # Obtenemos la ruta del directorio donde se encuentra el script:
        directorio_script = os.path.dirname(ruta_script)

        # return directorio_script
        return os.getcwd()

    @staticmethod
    def _crear_carpeta_archivo_en_ubicacion_script(
        nombre_carpeta: str,
        nombre_directorio: str = os.path.dirname(__file__),
        nombre_archivo: str | None = None,
        contenido_archivo: str | pd.DataFrame | None = None,
    ) -> None:
        """
        Busca una carpeta en el directorio donde se está ejecutando el script
        con nombre nombre_carpeta y si no la encuentra crea una. Si nombre_archivo
        es diferente a None creará un archivo además dentro de esa carpeta. Primero
        intentará con el nombre del archivo, si no con el sufijo _1,...,_n.
        """
        # Importamos el directorio del script
        # directorio_script = PreScrapping._buscar_directorio_script()

        # Construimos la ruta completa de la carpeta
        ruta_carpeta = os.path.join(nombre_directorio, nombre_carpeta)

        # Creamos la carpeta si no existe
        if not os.path.exists(ruta_carpeta):
            os.makedirs(ruta_carpeta)

        if nombre_archivo:
            ruta_archivo = os.path.join(ruta_carpeta, nombre_archivo)
            contador = 1

            # Extraemos la extensión y el nombre base del archivo
            nombre_base, extension = os.path.splitext(nombre_archivo)

            # Mientras el archivo exista, modificamos el nombre
            while os.path.exists(ruta_archivo):
                ruta_archivo = os.path.join(
                    ruta_carpeta, f"{nombre_base}_{contador}{extension}"
                )
                contador += 1

            # Si es un xlsx, directamente generamos el df
            if extension == ".xlsx":
                contenido_archivo.to_excel(ruta_archivo)
            elif extension == ".csv":
                contenido_archivo.to_csv(ruta_archivo, index=False)
            elif extension == ".json":
                contenido_archivo.to_json(ruta_archivo, orient="records", lines=True)
            elif extension == ".pkl":
                contenido_archivo.to_pickle(ruta_archivo)
            else:
                # Si no, creamos el archivo (vacío) en la ruta final
                with open(ruta_archivo, "w") as archivo:
                    pass  # No es necesario escribir nada en el archivo por ahora.

    # --------------------------------------------------------------------------------------- Métodos para dfs:
    def _preparacion_datos(self) -> pd.DataFrame:
        """
        Función que solo trabaja con df en el formato que tiene Ivan ahora mismo, cualquier
        cambio tendría consecuencias graves.
        """

        # --------------------------------------------------------------------------------------- Funciones para apply
        # Generamos la función añadir a cada ubicación el Madrid, Spain:
        def _anadir_ciudad(elem):
            if isinstance(elem, str):
                return elem + " ,Madrid, Comunidad de Madrid, España"
            else:
                return pd.NA

        # Generamos la función corrección de formato para la columna Ubicación
        def _corrector_formatos_direcciones(elem):
            """
            Reemplaza abreviaturas comunes en direcciones con sus nombres completos.

            Parámetros:
            - direccion (str): La dirección original que necesita ser modificada.

            Retorna:
            - str: La dirección con las abreviaturas reemplazadas.
            """
            # Reemplazos para facilitar a geopy la búsqueda de coordenadas:
            elem = elem.replace("C/", "Calle ")
            elem = elem.replace("Pl.", "Plaza ")
            elem = elem.replace("Crra", "Carrera")
            elem = elem.replace("S/n", "")
            elem = elem.replace("Pº.", "Paseo")
            elem = elem.replace("Gta.", "Glorieta")
            elem = elem.replace("Cta.", "Cuesta")
            elem = elem.replace("Ct.", "Cuesta")

            return elem

        # --------------------------------------------------------------------------------------- Limpieza de datos básica
        df = self.df

        # Eliminamos de la columna ranking el símobolo de posición:
        if df["Ranking"][0][:-1] == "°":
            df["Ranking"] = df["Ranking"].apply(lambda x: x[:-1])

        # Reemplaza cualquier símbolo especial por '_'
        # Nota: '[^\w\s]' selecciona cualquier carácter que no sea alfanumérico o espacio en blanco
        df["ElementoModificado"] = df["Elemento"].apply(
            lambda x: re.sub(r"[^\w\s]", "_", x)
        )

        # Eliminamos de la columna Elemento los espacios:
        df["ElementoModificado"] = df["ElementoModificado"].apply(
            lambda x: x.replace(" ", "_")
        )

        # Ordenamos el dataframe en base al número que ocupa en el ranking de tripadvisor:
        df = df.sort_values(by=["Ranking"], ascending=True)
        df["Ubicación1"] = df["Ubicación"]
        df["Ubicación"] = df["Ubicación"].apply(_anadir_ciudad)
        df = df.loc[~pd.isna(df["Ubicación"]), :].copy()
        df["Ubicación"] = df["Ubicación"].apply(_corrector_formatos_direcciones)

        # --------------------------------------------------------------------------------------- Guardado en carpeta:
        PreScrapping._crear_carpeta_archivo_en_ubicacion_script(
            "Resultados_PreFiltering",
            nombre_directorio=self.directory,
            nombre_archivo="df_limpio.xlsx",
            contenido_archivo=df,
        )

        return df

    # --------------------------------------------------------------------------------------- Geoanálisis
    def geocodificator(self):
        # Inicializamos el geocodificador
        geolocator = Nominatim(
            user_agent="myGeocoder", timeout=10
        )  # Aumenta el timeout a 10 segundos
        geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

        # Aplicamos la geocodificación a cada dirección
        self.df["location"] = self.df_prepared["Ubicación"].apply(geocode)

        # Extraemos latitud y longitud
        self.df_prepared["lat"] = self.df_prepared["location"].apply(
            lambda loc: loc.latitude if loc else None
        )
        self.df_prepared["lon"] = self.df_prepared["location"].apply(
            lambda loc: loc.longitude if loc else None
        )
        self.df_prepared["Coordenadas"] = self.df_prepared[["lat", "lon"]].apply(
            lambda row: (row[0], row[1]), axis=1
        )

        # Guardamos los valores de la misma forma
        PreScrapping._crear_carpeta_archivo_en_ubicacion_script(
            "Resultados_PreFiltering",
            nombre_directorio=self.directory,
            nombre_archivo="df_coordenadas.xlsx",
            contenido_archivo=self.df_prepared,
        )

        PreScrapping._crear_carpeta_archivo_en_ubicacion_script(
            "Resultados_PreFiltering",
            nombre_directorio=self.directory,
            nombre_archivo="df_coordenadas.pkl",
            contenido_archivo=self.df_prepared,
        )
