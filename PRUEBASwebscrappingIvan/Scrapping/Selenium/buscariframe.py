# from selenium import webdriver
# from selenium.webdriver.common.by import By  # Importa By para las búsquedas de elementos
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import requests
# import time


# # Configura la URL de la página
# url_pagina = 'https://www.tripadvisor.es/Attraction_Review-g187514-d2452516-Reviews-Iglesia_de_San_Andres-Madrid.html'

# # Inicia el navegador Safari
# driver = webdriver.Safari()

# # Navega a la página
# driver.get(url_pagina)

# # Espera hasta que el botón de cookies esté presente
# espera = WebDriverWait(driver, 10)
# boton_cookies = espera.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')))
# boton_cookies.click()

# # Espera a que la página cargue completamente
# time.sleep(2)

# # # Localiza y haz clic en la imagen
# imagen = driver.find_element(By.XPATH, '//*[@id="lithium-root"]/main/div[1]/div[2]/div[2]/div[2]/div/div[1]/section[2]/div/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div[1]/div/div[2]')
# imagen.click()
# # time.sleep(5)  # Espera para que la imagen se cargue

# # Obtén todos los iframes en la página
# # Espera a que todos los iframes estén presentes
# WebDriverWait(driver, 10).until(
#     EC.presence_of_all_elements_located((By.TAG_NAME, 'iframe'))
# )
# iframes = driver.find_elements(By.TAG_NAME, 'iframe')

# # Itera sobre cada iframe utilizando su índice
# for index, iframe in enumerate(iframes):
#     try:
#         # Intenta cambiar al iframe por índice
#         driver.switch_to.frame(index)
        
#         # Busca si existe un elemento específico que solo se encuentra dentro del iframe deseado
#         # Corrige el método para encontrar elementos dentro del iframe
#         if driver.find_elements(By.XPATH, '//*[@id="lithium-root"]/main/div[1]/div[2]/div[2]/div[2]/div/div[1]/section[2]/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[2]/div/div/div[1]/div/div/div/div/picture/img'):
#             print(f"Se encontró el iframe deseado en el índice {index}",
#                   f'\nEl iframe en cuestión es {iframe}')
#             # Si se encuentra el elemento, significa que este es el iframe correcto
#             # Realiza las operaciones que necesites aquí
#             break
#     except Exception as e:
#         print(f"No se pudo cambiar al iframe con índice {index}: {e}, {type(e).__name__}")

#     finally:
#         # Asegúrate de volver al contenido principal antes de pasar al siguiente iframe
#         driver.switch_to.default_content()



# # Si ninguno de los iframes contiene el elemento, posiblemente no estás utilizando el XPATH correcto,
# # o el elemento no se encuentra en un iframe.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time

# Configura la URL de la página
url_pagina = 'https://www.tripadvisor.es/Attraction_Review-g187514-d2452516-Reviews-Iglesia_de_San_Andres-Madrid.html'

# Inicia el navegador Safari
driver = webdriver.Safari()

# Navega a la página
driver.get(url_pagina)

# Espera hasta que el botón de cookies esté presente y haz clic en él
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))).click()

# Haz clic en la imagen que activa el iframe
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="lithium-root"]/main/div[1]/div[2]/div[2]/div[2]/div/div[1]/section[2]/div/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div[1]/div/div[2]'))).click()

# Espera a que el iframe se cargue
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'iframe')))

# Obtén todos los iframes en la página después de que la imagen se haya clickeado y el iframe aparezca
iframes = driver.find_elements(By.TAG_NAME, 'iframe')

# Itera sobre cada iframe utilizando su índice
for index, iframe in enumerate(iframes):
    try:
        # Cambia al iframe por índice
        driver.switch_to.frame(index)
        
        # Intenta realizar alguna acción dentro del iframe
        # Asegúrate de que el elemento que buscas es único en ese iframe
        if driver.find_elements(By.XPATH, 'XPATH_DEL_ELEMENTO_DENTRO_DEL_IFRAME'):
            print(f"Se encontró el iframe deseado en el índice {index}")
            # Si se encuentra el elemento, significa que este es el iframe correcto
            # Realiza las operaciones que necesites aquí
            break
    except Exception as e:
        print(f"No se pudo cambiar al iframe con índice {index}: {e}")
    finally:
        # Vuelve al contenido principal antes de pasar al siguiente iframe
        driver.switch_to.default_content()

# Cierra el navegador al finalizar
driver.quit()





