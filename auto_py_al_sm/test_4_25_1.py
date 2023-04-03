from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime,timedelta
from webdriver_manager.chrome import ChromeDriverManager
import time

#Запуск браузера Chrome
def runChromeDriverManager():
    return webdriver.Chrome(ChromeDriverManager().install())
browser = runChromeDriverManager()    

#Запуск браузера Firefox
#browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())

#driver = webdriver.Chrome(executable_path='C:\\Users\\kaleev.BSW\\environments\\selenium_env\\Scripts\\chromedriver.exe')
base_url = 'https://demoqa.com/dynamic-properties'
browser.get(base_url)
browser.maximize_window()
""" try:
    visible_button = browser.find_element(By.XPATH,'//button[@id="visibleAfter"]')
    visible_button.click()
except NoSuchElementException as exception:
    print('NoSuchElementException exception')
    time.sleep(10)
    visible_button = browser.find_element(By.XPATH,'//button[@id="visibleAfter"]')
    visible_button.click()
    print('Click visible button') """


