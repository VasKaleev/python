# python -m pytest -s -v -p no:warnings d:\Python\auto_py_al_sm\7_15_1\pages\test_2.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from win32api import GetSystemMetrics
#from webdriver_manager.firefox import GeckoDriverManager
import time

#Запуск браузера Chrome
def runChromeDriverManager():
    return webdriver.Chrome(ChromeDriverManager().install())
browser = runChromeDriverManager()    

#Запуск браузера Firefox
#browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())

#driver = webdriver.Chrome(executable_path='C:\\Users\\kaleev.BSW\\environments\\selenium_env\\Scripts\\chromedriver.exe')
url = "https://5element.by/cart/"
browser.get(url)
browser.maximize_window()
browser.delete_all_cookies()
cooki = "//button[@class='js-cookie-popup-close btn btn--block']"
cooki_button = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH,cooki)))
cooki_button = browser.find_element(By.XPATH,"//button[@class='js-cookie-popup-close btn btn--block']")
cooki_button.click()
print("Нажали кнопку принять куки")

nam_cart_prod_1 = "(//a[@href='/products/721273-igrovoy-noutbuk-2-v-1-asus-rog-flow-x13-gv301qh-k6231t'])[2]"
name_prod_1 = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH,nam_cart_prod_1)))
name_product_1 = name_prod_1.text
print("Название товара в корзине", name_prod_1)
time.sleep(2)
pric_cart_prod_1 = "(//div[@class='c-price'])[1]"
price_prod_1 = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH,pric_cart_prod_1)))
price_product_1 = price_prod_1.text
print("Цена товара в корзине", price_product_1)
time.sleep(2)

