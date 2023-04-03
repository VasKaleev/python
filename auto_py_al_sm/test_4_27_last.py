from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
#browser.maximize_window()
browser.set_window_size(1980, 800)
browser.delete_all_cookies()
browser.implicitly_wait(10)
user_name = browser.find_element(By.XPATH,'//input[@id="user-name"]')
login_standard_user = "standard_user"
password_all = "secret_sauce"
user_name.send_keys(login_standard_user)
#time.sleep(2)
password = browser.find_element(By.XPATH,'//input[@id="password"]')
password.send_keys(password_all)
print("Input password all")
#time.sleep(2)
password = browser.find_element(By.XPATH,'//input[@id="login-button"]')
password.click()
print("Click login button")
#time.sleep(2)

print("Приветствую тебя в нашем интернет магазине")
print("""Выбери один из следующих товаров и укажи его номер:
1 - Sauce Labs Backpack,
2 - Sauce Labs Bike Light,
3 - Sauce Labs Bolt T-Shirt,
4 - Sauce Labs Fleece Jacket,
5 - Sauce Labs Onesie,
6 - Test.allTheThings() T-Shirt (Red).""")
try:
    product = input()
    print("Выбранный номер товара: ",product)
    locator = ""


    #locator Name tovar
    prod_id = {
    "1":"item_4_title_link",
    "2":"item_0_title_link",
    "3":"item_1_title_link",
    "4":"item_5_title_link",
    "5":"item_2_title_link",
    "6":"item_3_title_link"
    }
    #Button Add to card
    button_id = {
    "1":"add-to-cart-sauce-labs-backpack",
    "2":"add-to-cart-sauce-labs-bike-light",
    "3":"add-to-cart-sauce-labs-bolt-t-shirt",
    "4":"add-to-cart-sauce-labs-fleece-jacket",
    "5":"add-to-cart-sauce-labs-onesie",
    "6":"add-to-cart-test.allthethings()-t-shirt-(red)"
    }
    print("--------------------")

    """ INFO Product #1 """
    locator = '//a[@id="' + prod_id[product] + '"]'
    product_1 = browser.find_element(By.XPATH, locator)
    value_product_1 = product_1.text
    print(value_product_1)
    price_product_1 = browser.find_element(By.XPATH,'(//div[@class="inventory_item_price"])['+ product +']')
    value_price_product_1 = price_product_1.text
    print(value_price_product_1)
    print("Название кнопки",button_id[product])
    select_product_1 = browser.find_element(By.XPATH, '//button[@id="' + button_id[product] + '"]').click()
    print('Select product' + product)
    cart = browser.find_element(By.XPATH,'//span[@class="shopping_cart_badge"]').click()
    print('Enter cart')
    #time.sleep(2)
    print("--------------------")


    """ INFO Cart Product #1 """
    browser.set_window_size(1980, 800)
    #time.sleep(2)
    cart_product_1 = browser.find_element(By.XPATH, locator)
    #time.sleep(2)
    value_cart_product_1 = cart_product_1.text
    print(value_cart_product_1)
    assert value_product_1 == value_cart_product_1
    print("INFO Cart Product ",product," GOOD")
    price_cart_product_1 = browser.find_element(By.XPATH,'//div[@class="inventory_item_price"]')
    value_cart_price_product_1 = price_cart_product_1.text
    print(value_cart_price_product_1)
    assert value_price_product_1 == value_cart_price_product_1
    print("INFO Cart Price Product ",product," GOOD")


    button_checkout = browser.find_element(By.XPATH,'//button[@id="checkout"]').click()
    print("Print checkout")
    #time.sleep(2)
    print("--------------------")

    """ Select User INFO  """
    first_name = browser.find_element(By.XPATH,'//input[@id="first-name"]').send_keys("Vasily")
    print("Input first name")
    #time.sleep(2)
    last_name = browser.find_element(By.XPATH,'//input[@id="last-name"]').send_keys("Petrov")
    print("Input last name")
    #time.sleep(2)
    zip = browser.find_element(By.XPATH,'//input[@id="postal-code"]').send_keys("247250")
    print("Input zip")
    #time.sleep(2)
    Button_continue = browser.find_element(By.XPATH,'//input[@id="continue"]').click()
    print("Click continue")
    #time.sleep(2)
    print("--------------------")
 
    """ INFO Finish Product #1 """
    finish_product_1 = browser.find_element(By.XPATH, locator)
    value_finish_product_1 = finish_product_1.text
    print(value_finish_product_1)
    assert value_product_1 == value_finish_product_1
    print("INFO finish Product ", product, " GOOD")
    #time.sleep(2)
    price_finish_product_1 = browser.find_element(By.XPATH,'//div[@class="inventory_item_price"]')
    value_finish_price_product_1 = price_finish_product_1.text
    print(value_finish_price_product_1)
    assert value_price_product_1 == value_finish_price_product_1
    print("INFO finish Price Product ",product," GOOD")
    #time.sleep(2)
    print("--------------------")

    summary_price = browser.find_element(By.XPATH,'//div[@class="summary_subtotal_label"]')
    value_summary_price = summary_price.text
    print(value_summary_price)
    #time.sleep(2)
    item_total = "Item total: " + value_finish_price_product_1
    print(item_total)
    assert item_total == value_summary_price
    print("Total summary_price Good")
except KeyError:
    print("**********************************************")
    print("* Выбран номер товара не из диапазона 1 - 6  *")
    print("* Перезапустите тест и                       *") 
    print("* выберите один из товаров в диапазоне 1 - 6 *")
    print("**********************************************")
print("End test")

