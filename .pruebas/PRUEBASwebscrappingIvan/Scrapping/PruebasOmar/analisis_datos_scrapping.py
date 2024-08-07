import pickle

# Importar los datos del archivo .pkl
with open(
    "/Users/omarkhalil/Desktop/Universidad/IvanPhD/webscrappingIvan/Scrapping/PruebasOmar/lista_total.pkl",
    "rb",
) as f:
    datos_importados = pickle.load(f)

datos_limpios = [elem[0] for elem in datos_importados]
# Diccionario unificado
diccionario_unificado = {}

# Unificar los diccionarios
for diccionario in datos_limpios:
    diccionario_unificado.update(diccionario)


print(diccionario_unificado)
