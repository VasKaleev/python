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
base_url = 'https://testpages.herokuapp.com/styled/basic-html-form-test.html'
browser.get(base_url)
browser.maximize_window()
time.sleep(10)
checkbox1 = browser.find_element(By.XPATH,'//input[@value="cb1"]')
checkbox1.click()
print("Checkbox1 нажат!")

time.sleep(10)
checkbox3 = browser.find_element(By.XPATH,'//input[@value="cb3"]')
checkbox3.click()
print("Checkbox3 нажат!")
time.sleep(2)
