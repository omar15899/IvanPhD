# import requests
# import time
# from stem import Signal
# from stem.control import Controller

# """
# Vamos a generar un programa con tor que cambia de id cada 20 segundos
# para poder ser ultra anónimos en la red.
# """
# inicio = time.time()  # Guardar el tiempo de inicio

# # Configuración del proxy para usar Tor, que por defecto escucha en el puerto 9050
# proxies = {"http": "socks5h://localhost:9050", "https": "socks5h://localhost:9050"}

# while (
#     time.time() - inicio < 60
# ):  # Continuar mientras el tiempo transcurrido sea menor a 60 segundos
#     try:
#         with Controller.from_port(port=9151) as controller:
#             controller.authenticate(
#                 password="omarpiapanchito"
#             )  # Autenticarse con la contraseña
#             controller.signal(Signal.NEWNYM)  # Solicitar a Tor un nuevo circuito

#         # Realizar la solicitud a través del proxy de Tor
#         response = requests.get("http://httpbin.org/ip", proxies=proxies)
#         print(
#             f"Tu dirección IP pública a través de Tor es: {response.json()['origin']}"
#         )

#     except requests.RequestException as e:
#         print(f"Error al realizar la solicitud: {e}")

#     time.sleep(11)  # Esperar 10 segundos antes de la próxima iteración

# print("El programa ha finalizado después de 1 minuto de ejecución.")

# """
# Si quiero tener información completa acerca de qué archivos de tor se están utilizando:

# ps aux | grep tor
# """


from stem import Signal
from stem.control import Controller


def renew_tor_ip():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(
            "omarpiapanchito"
        )  # Necesitas autenticarte con el controlador de Tor
        controller.signal(Signal.NEWNYM)


try:
    renew_tor_ip()
    print("Solicitud de cambio de IP enviada a Tor.")
except Exception as e:
    print(f"Error al intentar cambiar la IP de Tor: {e}")
