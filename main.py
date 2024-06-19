import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv

load_dotenv()

# * RUTA DE TU WEB DRIVER
driver_path = os.getenv('DRIVER_PATH')

# * CONFUURACION DEL SERVICIO 
service = Service(driver_path)
service.start()

# * CONFUGURAR LAS OPCONES DEL NAVEGADOR
options = webdriver.ChromeOptions()
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# * INICIALIZA EL DRIVER CON EL SERVICIO Y LAS OPCIONES
driver = webdriver.Chrome(service=service, options=options)

# * URL DEL SITIO WEB
url = os.getenv('URL')

# * LAS CREDENCIALES
matricula = os.getenv('CONTROL_NUMBER')
contrasena = os.getenv('PASSWORD')

# ? ACA ABRE LA URL DEL SISTEMA
driver.get(url)
time.sleep(2)  # ! ESPERAR A QUE LA PAGINA CARGUE

# ! ENCUENTRA Y COMPLETA LOS CAMPOS BUSCANDOLOS POR NOMBRE DE LA ETIQUERTA HTML = (name)
# ? ejemplo <input name="frmLogin:login">
login_input = driver.find_element(By.NAME, 'frmLogin:login')
password_input = driver.find_element(By.NAME, 'frmLogin:password')

login_input.send_keys(matricula)
password_input.send_keys(contrasena)
password_input.send_keys(Keys.RETURN)

# ? ESPERA UN MOMENTO PARA VER EL RESULTADO DE LA APLICACION
time.sleep(5)

# ! CIERRA EL NAVEGADOR
driver.quit()
