# class SuperClase:
#     def __init__(self, variable1, variable2) -> None:
#         self.variable1 = variable1
#         self.variable2 = variable2
#         self.polla = "hola"


# class SubClase(SuperClase):
#     def __init__(self, variable1, variable2):
#         super().__init__(variable1, variable2)
#         self.variable2 = variable2


# objeto2 = SubClase(5, 5)
# print(objeto2.polla)
# print(objeto2.variable)

import os

# Ruta al directorio del cual quieres listar los archivos
directorio = "ScrappingPrincipal\PreScrapping\Resultados_PreFiltering"

# Obtener lista de archivos y directorios en el directorio especificado
archivos_y_directorios = os.listdir(directorio)
print(archivos_y_directorios)

# # Convertir a rutas absolutas
# rutas_absolutas = [os.path.abspath(os.path.join(directorio, nombre)) for nombre en archivos_y_directorios]

# for ruta in rutas_absolutas:
#     print(ruta)
