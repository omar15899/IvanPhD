"""
Script para entender la estructura de los datos que se obtienen del webscrapping
cuando se almacenan en el pkl
"""

import os
import pickle
from typing import List, Dict, Tuple, Union, Optional


def extractor(
    data: Union[List, Dict, Tuple],
    result: List,
    iteration: int = 0,
) -> None:
    # Limitar la profundidad de iteración para evitar bucles infinitos
    if iteration >= 15:
        return

    # Si 'data' es una lista, iterar sobre cada elemento
    if isinstance(data, list):
        for item in data:
            extractor(item, result, iteration=iteration + 1)

    # Si 'data' es una tupla, iterar sobre cada elemento
    elif isinstance(data, tuple):
        for item in data:
            extractor(item, result, iteration=iteration + 1)

    # Si 'data' es un diccionario, iterar sobre los valores
    elif isinstance(data, dict):
        for key, value in data.items():
            # Continuar la extracción si la clave es 'data' o 'MediaAlbumPage'
            if key in ["data", "mediaAlbumPage"]:
                extractor(value, result, iteration=iteration + 1)

            # Si la clave es 'mediaList', añadir sus elementos a 'result'
            elif key == "mediaList":
                if isinstance(value, list):
                    result.extend(value)

                # También continuar la extracción dentro de 'mediaList'
                extractor(value, result, iteration=iteration + 1)

            # Continuar la extracción dentro de otros diccionarios anidados
            else:
                extractor(value, result, iteration=iteration + 1)


def extractor2(
    data: List | Dict | Tuple,
    result: Optional[List] = None,
) -> None:
    if result is None:
        result = []
    if isinstance(data, list):
        for subrequest in data:
            extractor(subrequest, result)
    elif isinstance(data, tuple):
        for item in data:
            extractor(item, result)
    elif isinstance(data, dict):
        for key, value in data.items():
            if key == "data" or key == "MediaAlbumPage":
                extractor(value, result)
            elif key == "mediaList":
                result.extend(value)

    return result


pathname = (
    r"/Users/omarkhalil/Desktop/Universidad/IvanPhD/Datos_Obtenidos/Fichero_Scrapping_2"
)
# Listamos todos los archivillos que hay en el directorio
files = os.listdir(pathname)
# Nos quedamos con los archivos que tengan la extensión .pkl
files = [f for f in files if f[-4:] == ".pkl"]

if not os.path.exists(pathname[:-1] + "_flatlists"):
    os.makedirs(pathname[:-1] + "_flatlists")


# for file in files:
#     submedialist = []
#     # Cargamos el archivo, que va a ser un json
#     with open(os.path.join(pathname, file), "rb") as f:
#         data = pickle.load(f)

#     extractor(data, submedialist)
#     print(len(submedialist))
#     # Guardamos la lista de imagenes en un archivo pkl con el mismo nombre pero con flat_list al final
#     with open(
#         os.path.join(pathname[:-1] + "_flatlists", file[:-4] + "_flat_list.pkl"), "wb"
#     ) as f:
#         pickle.dump(submedialist, f)
#     print(f"Se ha guardado el archivo {file[:-4] + '_flat_list.pkl'}")


"""
Tengo que crear una fucnión que me permite analizar si tenemo suna lista, un diccioinario o una tupla 
y en base a ello se meta dentro, busque lo que necesitamos que es toda la inoframción de los mediaList. 
"""

# guardamos en un txt los datos del archivo Plaza_de_Oriente.pkl
with open(os.path.join(pathname, "Plaza_de_Oriente.pkl"), "rb") as f:
    data = pickle.load(f)

    with open(
        os.path.join("/Users/omarkhalil/Desktop", "Plaza_de_Oriente.txt"), "w"
    ) as f:
        f.write(str(data))
