"""
El objetivo de este script es dejar un dataset con toda la información util con la que vamos a 
basarnos para enviar el prompt. Una vez enviemos el prompt, en otro script generaremos un dataset
con todas las imágenes y cada una de las imágenes tendrá ademaás todas estas columnas de este 
dataset (se vinculará en base al http del que fueron descargadas).
"""

import re
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

# https://drive.google.com/drive/folders/1fLMyMclj6MvNDslxNPLxlU6SvaNp7txe?usp=drive_link

# Copiamos el archivo de excel en la RAM mediante la función
#  pd.read_excel que actua como un open + read. Esto lo que genera
# es un puente entre el archivo en local y el script de python
# y acto seguido lo lee, sellandolo en la memoria (supongo que en binario),
# además de generar un objeto en la memoria del tipo dataframe:

df = pd.read_excel(
    "/Users/omarkhalil/Desktop/Universidad/IvanPhD/ArchivosDrive/Catalogo_Tripadvisor2.xlsx",
    header=0,
    engine="openpyxl",
)

# --------------------------------------------------------------------------------------- Limpieza de datos básica

# Eliminamos de la columna ranking el símobolo de posición:
df["Ranking"] = df["Ranking"].apply(lambda x: x[:-1])
# print([type(df["Ranking"][i]) for i in range(len(df["Ranking"]))])
# Reemplaza cualquier símbolo especial por '_'
# Nota: '[^\w\s]' selecciona cualquier carácter que no sea alfanumérico o espacio en blanco
df["Elemento"] = df["Elemento"].apply(lambda x: re.sub(r"[^\w\s]", "_", x))
# Eliminamos de la columna Elemento los espacios:
df["Elemento"] = df["Elemento"].apply(lambda x: x.replace(" ", "_"))
# Ordenamos el dataframe en base al número que ocupa en el ranking de tripadvisor:
df = df.sort_values(by=["Ranking"], ascending=True)


# Generamos la función corrección de formato:
def corrector_formatos_direcciones(elem):
    """
    Reemplaza abreviaturas comunes en direcciones con sus nombres completos.

    Parámetros:
    - direccion (str): La dirección original que necesita ser modificada.

    Retorna:
    - str: La dirección con las abreviaturas reemplazadas.
    """
    # Reemplazos
    elem = elem.replace("C/", "Calle ")
    elem = elem.replace("Pl.", "Plaza ")
    elem = elem.replace("Crra", "Carrera")
    elem = elem.replace("S/n", "")
    elem = elem.replace("Pº.", "Paseo")
    elem = elem.replace("Gta.", "Glorieta")
    elem = elem.replace("Cta.", "Cuesta")
    elem = elem.replace("Ct.", "Cuesta")

    return elem


# Añadimos a cada ubicación el Madrid, Spain:
def anadir_ciudad(elem):
    if isinstance(elem, str):
        return elem + " ,Madrid, Comunidad de Madrid, España"
    else:
        return pd.NA


df["Ubicación1"] = df["Ubicación"]
df["Ubicación"] = df["Ubicación"].apply(anadir_ciudad)
df = df.loc[~pd.isna(df["Ubicación"]), :].copy()
df["Ubicación"] = df["Ubicación"].apply(corrector_formatos_direcciones)


print(df)

# --------------------------------------------------------------------------------------- Geoanálisis
# Inicializamos el geocodificador
geolocator = Nominatim(
    user_agent="myGeocoder", timeout=10
)  # Aumenta el timeout a 10 segundos
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

# Aplicamos la geocodificación a cada dirección
df["location"] = df["Ubicación"].apply(geocode)

# Extraemos latitud y longitud
df["lat"] = df["location"].apply(lambda loc: loc.latitude if loc else None)
df["lon"] = df["location"].apply(lambda loc: loc.longitude if loc else None)
df["Coordenadas"] = df[["lat", "lon"]].apply(lambda row: (row[0], row[1]), axis=1)


# Guardamos el DataFrame en un archivo .pkl, que es un archivo de python que nos
# permite guardar en binario todos los objetos de python. De este modo cuando
# lo importemos vamos a tener un archivo con objetos de python y no con str.

df.to_pickle(
    "/Users/omarkhalil/Desktop/Universidad/IvanPhD/webscrappingIvan/PreFiltering/resultados_prefiltering/df1_prueba6.pkl"
)

# # # Para cargar el DataFrame desde un archivo .pkl
# # # df_cargado = pd.read_pickle("/ruta/donde/guardar/df.pkl")
