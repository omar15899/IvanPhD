from selenium import webdriver
from selenium.webdriver.common.by import By  # Importa By para las búsquedas de elementos
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time

def descargar_imagen(url, nombre_archivo):
    time.sleep(2)
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        with open(nombre_archivo, 'wb') as file:
            file.write(respuesta.content)

# Configura la URL de la página
url_pagina = 'https://www.tripadvisor.es/Attraction_Review-g187514-d2452516-Reviews-Iglesia_de_San_Andres-Madrid.html'

# Inicia el navegador Safari
driver = webdriver.Safari()

# Navega a la página
driver.get(url_pagina)

# Espera hasta que el botón de cookies esté presente
espera = WebDriverWait(driver, 10)
boton_cookies = espera.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')))
boton_cookies.click()

# Espera a que la página cargue completamente
time.sleep(5)

# Ciclo para navegar y descargar imágenes
for i in range(10):  # Ajusta el rango según el número de imágenes que quieras descargar
    # Localiza y haz clic en la imagen
    imagen = driver.find_element(By.XPATH, '//*[@id="lithium-root"]/main/div[1]/div[2]/div[2]/div[2]/div/div[1]/section[2]/div/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div[1]/div/div[2]')
    imagen.click()
    time.sleep(5)  # Espera para que la imagen se cargue

    # Como nos encontramos con un iframe (una especie de página dentro de otra), lo que hay que hacer ahora es cambiar de frame para entrar en esa nueva pag
    driver.switch_to.frame('nombre_del_iframe_o_indice')

    # Localiza y haz clic en la imagen
    WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="lithium-root"]/main/div[1]/div[2]/div[2]/div[2]/div/div[1]/section[2]/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[2]/div/div/div[1]/div/div/div/div/picture/img'))
    ) # Esperamos a que aparezca el xpath correspondiente.
    imagen = driver.find_element(By.XPATH, '//*[@id="lithium-root"]/main/div[1]/div[2]/div[2]/div[2]/div/div[1]/section[2]/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[2]/div/div/div[1]/div/div/div/div/picture/img')
    time.sleep(2)  # Espera para que la imagen se cargue

    # Obtiene la URL de la imagen y la descarga
    url_imagen = imagen.get_attribute('src')
    descargar_imagen(url_imagen, f'imagen_{i}.jpg')

    # Navega a la siguiente imagen
    flecha_derecha = driver.find_element(By.XPATH, '//*[@id="lithium-root"]/main/div[1]/div[2]/div[2]/div[2]/div/div[1]/section[2]/div/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div[1]/div/div[5]/button/svg')
    flecha_derecha.click()
    time.sleep(2)  # Espera a que la siguiente imagen se cargue

