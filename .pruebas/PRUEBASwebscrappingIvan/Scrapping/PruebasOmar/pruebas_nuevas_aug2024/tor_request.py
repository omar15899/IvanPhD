from stem.control import Controller
from stem import Signal


def change_tor_ip():
    try:
        print("Intentando conectar al ControlPort en 127.0.0.1:9061...")
        with Controller.from_port(address="127.0.0.1", port=9051) as controller:
            print("Conexión establecida. Autenticando...")
            controller.authenticate()
            print("Autenticación exitosa.")
            previous_ip = controller.get_info("ip-to-country/ipv4")["ip"]
            print("IP previa: ", previous_ip)
            controller.signal(Signal.NEWNYM)
            print("IP cambiada con éxito.")
            new_ip = controller.get_info("ip-to-country/ipv4")["ip"]
            print("IP actual: ", new_ip)
    except Exception as e:
        print("Ocurrió un error: ", e)


change_tor_ip()
print("Fin del proceso")
