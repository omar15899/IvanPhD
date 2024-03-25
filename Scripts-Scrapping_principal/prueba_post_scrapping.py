import pickle

with open(
    "/Users/omarkhalil/Desktop/Universidad/IvanPhD/Programacion/Scripts-Scrapping_principal/Fichero_Scrapping/Parque_El_Retiro.pkl",
    "rb",
) as archivo:
    # Cargar el contenido del archivo pickle al objeto de Python
    lista_elementos = pickle.load(archivo)

print(len(lista_elementos[0]))
