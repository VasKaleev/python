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
#user_name.clear()
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
menu = browser.find_element(By.XPATH,'//button[@id="react-burger-menu-btn"]').click()
print("Click menu button")
time.sleep(2)
link_about = browser.find_element(By.XPATH,'//a[@id="about_sidebar_link"]').click()
time.sleep(2)
browser.back()
print("Go back")
time.sleep(10)
browser.forward()
print("Go forward")
time.sleep(10)
