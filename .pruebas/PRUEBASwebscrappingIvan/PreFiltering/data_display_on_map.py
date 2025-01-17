import pandas as pd
import folium

df = pd.read_excel(
    "/Users/omarkhalil/Desktop/Universidad/IvanPhD/webscrappingIvan/PreFiltering/resultados_prefiltering/df1_prueba6.xlsx"
)
df = df[~pd.isna(df["lat"]) & ~pd.isna(df["lon"])]
df["Coordenadas"] = df[["lat", "lon"]].apply(lambda row: (row[0], row[1]), axis=1)
print(df)
print(df.columns)
# Coordenadas de Madrid (latitud y longitud)
latitud_madrid = 40.416775
longitud_madrid = -3.703790

# Crear un mapa de Madrid
mapa_madrid = folium.Map(location=[latitud_madrid, longitud_madrid], zoom_start=12)

# Lista de coordenadas de ejemplo (latitud, longitud)
puntos = df["Coordenadas"].to_list()

# Añadir puntos al mapa
for punto in puntos:
    folium.Marker(location=[punto[0], punto[1]]).add_to(mapa_madrid)

# Guardar el mapa en un archivo HTML
mapa_madrid.save(
    "/Users/omarkhalil/Desktop/Universidad/IvanPhD/webscrappingIvan/PreFiltering/resultados_prefiltering/mapa_madrid_1.html"
)
