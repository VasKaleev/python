from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

class Login_page():
    def __init__(self, browser):
        self.browser = browser

    def authorization(self, login_name, login_password):
        user_name = WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.XPATH,'//input[@id="user-name"]')))
        user_name.send_keys(login_name)

        password = WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.XPATH,'//input[@id="password"]')))
        password.send_keys(login_password)
        print("Input password all")

        button_login = WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.XPATH,'//input[@id="login-button"]')))
        button_login.click()
        print("Click login button")

        
            

