"""
Este módulo sirve para generar todos los mapas con etiquetas diferentes. 
Este módulo se completará una vez hallamos generado el scrapping y por ahora
solo vamos a hacer una serie de características sencillitas. Cuando se haga 
el scrapping se comprobará el overall de todo esto. 
"""

import pandas as pd
import folium
from .prescrapping import *


class Mapping(PreScrapping):
    def __init__(self, df: pd.DataFrame, directory: str = os.getcwd()) -> None:
        """
        En este caso, a diferencia de la clase PreScrapping, el df se espera que sea
        el valor salida del geocodificator, porque tiene que tener las coordenadas.
        """
        super().__init__(df, directory)

    def mapa_etiquetas(self):
        df = df[~pd.isna(df["lat"]) & ~pd.isna(df["lon"])]
        df["Coordenadas"] = df[["lat", "lon"]].apply(
            lambda row: (row[0], row[1]), axis=1
        )
        print(df)
        print(df.columns)
        # Coordenadas de Madrid (latitud y longitud)
        latitud_madrid = 40.416775
        longitud_madrid = -3.703790

        # Crear un mapa de Madrid
        mapa_madrid = folium.Map(
            location=[latitud_madrid, longitud_madrid], zoom_start=12
        )

        # Lista de coordenadas de ejemplo (latitud, longitud)
        puntos = df["Coordenadas"].to_list()

        # Añadir puntos al mapa
        for punto in puntos:
            folium.Marker(location=[punto[0], punto[1]]).add_to(mapa_madrid)

        # Guardar el mapa en un archivo HTML
        mapa_madrid.save(
            "/Users/omarkhalil/Desktop/Universidad/IvanPhD/webscrappingIvan/PreFiltering/resultados_prefiltering/mapa_madrid_1.html"
        )
