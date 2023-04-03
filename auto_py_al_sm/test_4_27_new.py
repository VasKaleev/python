from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from datetime import datetime
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
time.sleep(2)
password = browser.find_element(By.XPATH,'//input[@id="password"]')
password.send_keys(password_all)
print("Input password all")
time.sleep(2)
password = browser.find_element(By.XPATH,'//input[@id="login-button"]')
password.click()
print("Click login button")
time.sleep(2)

print("Приветствую тебя в нашем интернет магазине")
print("""Выбери один из следующих товаров и укажи его номер:
1 - Sauce Labs Backpack,
2 - Sauce Labs Bike Light,
3 - Sauce Labs Bolt T-Shirt,
4 - Sauce Labs Fleece Jacket,
5 - Sauce Labs Onesie,
6 - Test.allTheThings() T-Shirt (Red).""")
product = input()
print(product)

print("--------------------")
prod_id = {
    "1":"item_4_title_link",
    "2":"item_0_title_link",
    "3":"item_1_title_link",
    "4":"item_5_title_link",
    "5":"item_2_title_link",
    "6":"item_3_title_link"
}
print(prod_id)
print(prod_id["1"])
print(prod_id[product])
print("--------------------")

""" INFO Product #1 """
#product_1 = browser.find_element(By.XPATH,'//a[@id="item_4_title_link"]')
product_1 = browser.find_element(By.XPATH,'//a[@id=' + prod_id[product] + ']')
value_product_1 = product_1.text
print(value_product_1)

#price_product_1 = browser.find_element(By.XPATH,'//div[@class="inventory_item_price"]')
price_product_1 = browser.find_element(By.XPATH,'(//div[@class="inventory_item_price"])['+ product +']')
#(By.XPATH,'(//div[@class="inventory_item_price"])[2]')
value_price_product_1 = price_product_1.text
print(value_price_product_1)

select_product_1 = browser.find_element(By.XPATH,'//button[@id="add-to-cart-sauce-labs-backpack"]').click()
print('Select product_1')

cart = browser.find_element(By.XPATH,'//span[@class="shopping_cart_badge"]').click()
print('Enter cart')
time.sleep(2)

""" INFO Cart Product #1 """
cart_product_1 = browser.find_element(By.XPATH,'//a[@id="item_4_title_link"]')
value_cart_product_1 = cart_product_1.text
print(value_cart_product_1)
assert value_product_1 == value_cart_product_1
print("INFO Cart Product #1 GOOD") 

price_cart_product_1 = browser.find_element(By.XPATH,'//div[@class="inventory_item_price"]')
value_cart_price_product_1 = price_cart_product_1.text
print(value_cart_price_product_1)
assert value_price_product_1 == value_cart_price_product_1
print("INFO Cart Price Product #1 GOOD") 

button_checkout = browser.find_element(By.XPATH,'//button[@id="checkout"]').click()
print("Print checkout")
time.sleep(2)

""" Select User INFO  """
first_name = browser.find_element(By.XPATH,'//input[@id="first-name"]').send_keys("Vasily")
print("Input first name")
time.sleep(2)

last_name = browser.find_element(By.XPATH,'//input[@id="last-name"]').send_keys("Petrov")
print("Input last name")
time.sleep(2)

zip = browser.find_element(By.XPATH,'//input[@id="postal-code"]').send_keys("247250")
print("Input zip")
time.sleep(2)

Button_continue = browser.find_element(By.XPATH,'//input[@id="continue"]').click()
print("Click continue")
time.sleep(2)

""" INFO Finish Product #1 """
finish_product_1 = browser.find_element(By.XPATH,'//a[@id="item_4_title_link"]')
value_finish_product_1 = finish_product_1.text
print(value_finish_product_1)
assert value_product_1 == value_finish_product_1
print("INFO finish Product #1 GOOD") 
time.sleep(2)
price_finish_product_1 = browser.find_element(By.XPATH,'//div[@class="inventory_item_price"]')
value_finish_price_product_1 = price_finish_product_1.text
print(value_finish_price_product_1)
assert value_price_product_1 == value_finish_price_product_1
print("INFO finish Price Product #1 GOOD") 
time.sleep(2)

summary_price = browser.find_element(By.XPATH,'//div[@class="summary_subtotal_label"]')
value_summary_price = summary_price.text
print(value_summary_price)
time.sleep(2) 
item_total = "Item total: " + value_finish_price_product_1
print(item_total)
assert item_total == value_summary_price
print("Total summary_price Good")