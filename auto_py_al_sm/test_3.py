from selenium import webdriver
#from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options, executable_path='C:\\Users\\kaleev.BSW\\environments\\selenium_env\\Scripts\\chromedriver.exe')
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()
login_standart_user = "standard_user"
password_all = "secret_sauce"

user_name = driver.find_element(By.XPATH,"//input[@id='user-name']")
user_name.send_keys(login_standart_user)
print("Input login")
pasw = driver.find_element(By.XPATH,"//*[@id='password']")
pasw.send_keys(password_all)
pasw.send_keys(Keys.RETURN)
time.sleep(5)
filter = driver.find_element(By.XPATH,"//*[@id='password']")



""" time.sleep(5)
#user_name = driver.find_element(By.XPATH,"//*[@id='password']")
#user_name.send_keys(password_all)
print("Input Password")
user_name.send_keys(Keys.BACKSPACE)
time.sleep(5)
user_name.send_keys(Keys.BACKSPACE)
time.sleep(5)
user_name.send_keys("er")
time.sleep(5) """
""" but_login = driver.find_element(By.XPATH,"//input[@id='login-button']").click()
print("Click Login Button") """



""" text_products =  driver.find_element(By.XPATH,"//span[@class='title']")
value_text_products = text_products.text
print(value_text_products)
assert value_text_products == 'PRODUCT'
print("GOOD") """

""" url = "https://www.saucedemo.com/inventory.html"
get_url = driver.current_url
print(get_url)
assert url == get_url
print("GOOD_URL") """




