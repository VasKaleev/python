from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def runChromeDriverManager():
    return webdriver.Chrome(ChromeDriverManager().install())
browser = runChromeDriverManager()    

#driver = webdriver.Chrome(executable_path='C:\\Users\\kaleev.BSW\\environments\\selenium_env\\Scripts\\chromedriver.exe')
base_url = 'https://www.saucedemo.com/'
browser.get(base_url)
browser.maximize_window()
time.sleep(10)

login_standard_user = "standard_user"
password_all = "secret_sauce"
user_name = browser.find_element(By.XPATH,"//input[@id='user-name']")
user_name.send_keys(login_standard_user)
print("Input Login")
password = browser.find_element(By.XPATH,"//input[@id='password']")
password.send_keys(password_all)
print("Input Password")
button_login = browser.find_element(By.XPATH,"//input[@id='login-button']").click()
print("Click login batton")

""" text_products = browser.find_element(By.XPATH,"//span[@class='title']")
value_text_products = text_products.text
print(value_text_products)
assert value_text_products =="Products"
print("Good") """

url = "https://www.saucedemo.com/inventory.html"
get_url = browser.current_url
assert url == get_url
print("Good url")
time.sleep(10)





