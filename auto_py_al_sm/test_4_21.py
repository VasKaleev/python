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
base_url = 'https://demoqa.com/buttons'
browser.get(base_url)
browser.maximize_window()
time.sleep(5)

action = ActionChains(browser)
double = browser.find_element(By.XPATH,'//button[@id="doubleClickBtn"]')
action.double_click(double).perform()
print("button1 нажат!")
time.sleep(5)

right_click = browser.find_element(By.XPATH,'//button[@id="rightClickBtn"]')
action.context_click(right_click).perform()
print("button2 нажат!")
time.sleep(5)
