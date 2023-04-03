from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
#from webdriver_manager.firefox import GeckoDriverManager
import time

#Запуск браузера Chrome
def runChromeDriverManager():
    return webdriver.Chrome(ChromeDriverManager().install())
browser = runChromeDriverManager()    

#Запуск браузера Firefox
#browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())

#driver = webdriver.Chrome(executable_path='C:\\Users\\kaleev.BSW\\environments\\selenium_env\\Scripts\\chromedriver.exe')
base_url = 'https://html5css.ru/howto/howto_js_rangeslider.php'
browser.get(base_url)
browser.maximize_window()
action = ActionChains(browser)
price = browser.find_element(By.XPATH,'//input[@type="range"]')
#action.click_and_hold(price).move_by_offset(30, 0).release().perform()
action.drag_and_drop_by_offset(price, 20, 0).perform()

print("Price +++")



