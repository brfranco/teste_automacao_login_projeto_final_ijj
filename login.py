from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def login(url, username, password):
    driver = webdriver.Firefox()
    driver.get(url)
    
    try:
        # Esperar até que o campo de e-mail esteja presente e visível
        user_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Digite seu e-mail!']"))
        )
        user_field.send_keys(username)
        print("Campo de e-mail encontrado e preenchido.")
        
        # Esperar até que o campo de senha esteja presente e visível
        password_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@type='password']"))
        )
        password_field.send_keys(password)
        print("Campo de senha encontrado e preenchido.")
        
        # Submeter o formulário
        password_field.send_keys(Keys.RETURN)
        print("Formulário submetido.")
        
        # Esperar um pouco para a página carregar
        time.sleep(5)
        
        # Verificar se o login foi bem-sucedido
        success = "Dashboard" in driver.title
        print("Verificação de login bem-sucedido realizada.")
        
    except Exception as e:
        print(f"Erro durante o login: {e}")
        success = False
    
    driver.quit()
    
    return success