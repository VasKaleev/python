from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
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
#browser.maximize_window()
#print("Start test")
#browser.implicitly_wait(10)
#visible_checkbox = browser.find_element(By.XPATH,'//button[@id="visibleAfter"]')
#visible_checkbox.click()
#print("Finish test")

print("Start test")
visible_checkbox = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH,'//button[@id="visibleAfter"]')))
visible_checkbox.click()
print("Finish test")
