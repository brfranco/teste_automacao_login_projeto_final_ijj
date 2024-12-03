from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def login(url, username, password):
    driver = webdriver.Firefox()
    driver.get(url)
    
    try:
        # Esperar um pouco para garantir que a página carregou
        time.sleep(5)
        
        # Encontrar e preencher o campo de e-mail
        user_field = driver.find_element(By.XPATH, "//input[@placeholder='Digite seu e-mail!']")
        user_field.send_keys(username)
        print("Campo de e-mail encontrado e preenchido.")
        
        # Encontrar e preencher o campo de senha
        password_field = driver.find_element(By.XPATH, "//input[@type='password']")
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