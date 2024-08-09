"""
Hay que ejecutar este ecript desde la carpeta donde queremos que se guarden los folder,
es así como está configurado o especificarlo nosotros mismos.
"""

import sys
import pandas as pd

# Añadimos al path el directorio principal.
sys.path.append("/Users/omarkhalil/Desktop/Universidad/IvanPhD/Programacion")
# import ScrappingPrincipal.PreScrapping as sc
import ScrappingPrincipal.Scrapping as sc


# Importamos la libería:
df = pd.read_excel(
    "/Users/omarkhalil/Desktop/Universidad/IvanPhD/Programacion/ArchivosDrive/df_limpio.xlsx",
    header=0,
    engine="openpyxl",
)

# ordenamos por Nº fotos:
df = df.sort_values(by="Nº fotos", ascending=True)

objeto = sc.Scrapping(
    df,
    directory="/Users/omarkhalil/Desktop/Universidad/IvanPhD/Datos_Obtenidos",
    name_folder="Fichero_Scrapping",
)

objeto.scrap_everything()
