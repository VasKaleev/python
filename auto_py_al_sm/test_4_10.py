from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.firefox import GeckoDriverManager
import time

#Запуск браузера Chrome
def runChromeDriverManager():
    return webdriver.Chrome(ChromeDriverManager().install())
browser = runChromeDriverManager()    

#Запуск браузера Firefox
#browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())

#driver = webdriver.Chrome(executable_path='C:\\Users\\kaleev.BSW\\environments\\selenium_env\\Scripts\\chromedriver.exe')
base_url = 'https://www.saucedemo.com/'
browser.get(base_url)
browser.maximize_window()
user_name = browser.find_element(By.XPATH,'//input[@id="user-name"]')
login_standard_user = "standard_use"
password_all = "secret_sauce"
#password_all = ''
user_name.send_keys(login_standard_user)
print("Input login")
password = browser.find_element(By.XPATH,'//input[@id="password"]')
password.send_keys(password_all)
print("Input password all")
password = browser.find_element(By.XPATH,'//input[@id="login-button"]')
password.click()
print("Click login button")
warring_text = browser.find_element(By.XPATH,'//h3[@data-test="error"]')
#//*[@id="login_button_container"]/div/form/div[3]/h3
value_warring_text = warring_text.text
assert value_warring_text == "Epic sadface: Username and password do not match any user in this service"
print("Good test")
browser.refresh()


