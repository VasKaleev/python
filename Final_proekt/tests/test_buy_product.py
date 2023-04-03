#python -m pytest -s -v  -p no:warnings .\tests\test_buy_product.py
# python -m pytest -s -v  -p no:warnings .\tests\test_buy_product.py::test_buy_product_1
from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager
#from selenium import webdriver
#from selenium.webdriver.chrome.service import Service as ChromeService
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.cart_page import Cart_page
from pages.client_information_page import Client_information_page
from pages.payment_page import Payment_page
from pages.finish_page import Finish_page
import time
#from ..pages import login_page
import warnings

#@pytest.mark.run(order=3)
def test_buy_product_1(set_up, set_group):
    options = Options()
    options.add_argument("--test-type")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    #options.add_argument('--headless')
    options.add_argument('--log-level=3')
    #Запуск браузера Chrome
    def runChromeDriverManager():
        return webdriver.Chrome(ChromeDriverManager().install(),options=options)
        #return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser = runChromeDriverManager()  
        #Запуск браузера Firefox
        #browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())

        #driver = webdriver.Chrome(executable_path='C:\\Users\\kaleev.BSW\\environments\\selenium_env\\Scripts\\chromedriver.exe')
       

    print("Start test 1")
    login = Login_page(browser)
    login.authorization()

    mp = Main_page(browser)
    mp.select_products_1()

    cp = Cart_page(browser)
    cp.product_confirmation()

    cip =  Client_information_page(browser)
    cip.input_information()

    p = Payment_page(browser)
    p.click_finish_button()

    f = Finish_page(browser)
    f.finish() 
    print("Finish test 1")
    time.sleep(3)
    browser.quit()

#@pytest.mark.run(order=1)
def test_buy_product_2(set_up, set_group):
    options = Options()
    options.add_argument("--test-type")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    #options.add_argument('--headless')
    options.add_argument('--log-level=3')
    #Запуск браузера Chrome
    def runChromeDriverManager():
        return webdriver.Chrome(ChromeDriverManager().install(),options=options)
        #return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser = runChromeDriverManager() 
        #Запуск браузера Firefox
        #browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())

        #driver = webdriver.Chrome(executable_path='C:\\Users\\kaleev.BSW\\environments\\selenium_env\\Scripts\\chromedriver.exe')
       

    print("Start test 2")
    login = Login_page(browser)
    login.authorization()

    mp = Main_page(browser)
    mp.select_products_2()

    cp = Cart_page(browser)
    cp.product_confirmation()
    
    print("Finish test 2")
    time.sleep(3)

#@pytest.mark.run(order=2)
def test_buy_product_3(set_up, set_group):
    options = Options()
    options.add_argument("--test-type")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    #options.add_argument('--headless')
    options.add_argument('--log-level=3')
    #Запуск браузера Chrome
    def runChromeDriverManager():
        return webdriver.Chrome(ChromeDriverManager().install(),options=options)
        #return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser = runChromeDriverManager() 
        #Запуск браузера Firefox
        #browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())

        #driver = webdriver.Chrome(executable_path='C:\\Users\\kaleev.BSW\\environments\\selenium_env\\Scripts\\chromedriver.exe')
       

    print("Start test 3")
    login = Login_page(browser)
    login.authorization()

    mp = Main_page(browser)
    mp.select_products_3()

    cp = Cart_page(browser)
    cp.product_confirmation()
 
    print("Finish test 3") 
    time.sleep(3)