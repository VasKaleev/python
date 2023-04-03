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
login_standard_user = "standard_user"
password_all = "secret_sauce"
user_name.send_keys(login_standard_user)
print("Input login")
password = browser.find_element(By.XPATH,'//input[@id="password"]')
password.send_keys(password_all)
print("Input password all")
password = browser.find_element(By.XPATH,'//input[@id="login-button"]')
password.click()
print("Click login button")
""" text_products = browser.find_element(By.XPATH,'//span[@class="title"]')
value_text_products = text_products.text
print(value_text_products)
assert value_text_products == "PRODUCTS"
print("GOOD!") """
url = "https://www.saucedemo.com/inventory.html"
get_url = browser.current_url
print(get_url)
assert url == get_url
print("GOOD URL")
time.sleep(10)
#browser.close() 

