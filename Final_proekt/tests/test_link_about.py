from selenium import webdriver
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

def test_link_about(set_up):
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
       

    print("Start test")
    login = Login_page(browser)
    login.authorization()

    mp = Main_page(browser)
    mp.select_menu_about()

    time.sleep(10)
#test = Test_1()
#test.test_select_product()

