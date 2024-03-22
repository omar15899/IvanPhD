import pickle

with open(
    "/Users/omarkhalil/Desktop/Universidad/IvanPhD/Programacion/Scripts-Scrapping_principal/Fichero_Scrapping/Teatro_Arenal_1.pkl",
    "rb",
) as archivo:
    # Cargar el contenido del archivo pickle al objeto de Python
    lista_elementos = pickle.load(archivo)

print(lista_elementos)
