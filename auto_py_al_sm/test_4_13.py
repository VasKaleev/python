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
base_url = 'https://www.saucedemo.com/'
browser.get(base_url)
browser.maximize_window()
user_name = browser.find_element(By.XPATH,'//input[@id="user-name"]')
login_standard_user = "standard_user"
password_all = "secret_sauce"
#password_all = ''
user_name.send_keys(login_standard_user)
time.sleep(5)
password = browser.find_element(By.XPATH,'//input[@id="password"]')
password.send_keys(password_all)
print("Input password all")
time.sleep(5)
print("Click filter1")

password = browser.find_element(By.XPATH,'//input[@id="login-button"]')
password.click()
print("Click login button")
#browser.execute_script('window.scrollTo(0, 200)')
time.sleep(2)

action = ActionChains(browser)
red_t_shirt = browser.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-onesie"]')
action.move_to_element(red_t_shirt).perform()

now_date = datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
#name_screenshot = 'screenshot'+ now_date + '.png'
#browser.save_screenshot("d:\\Python\\avtom_selen_smit\\screen\\" + name_screenshot)
#browser.save_screenshot(".\\screen\\" + name_screenshot)
browser.save_screenshot(f'./screen/screenshot{now_date}.png')
time.sleep(5)
