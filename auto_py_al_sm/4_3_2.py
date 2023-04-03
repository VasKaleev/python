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
browser.get('https://www.saucedemo.com/')
browser.maximize_window()
user_name = browser.find_element(By.ID,"user-name")
user_name.send_keys("standard_user")
time.sleep(10)
#browser.close() 

