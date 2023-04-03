from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
#user_name.send_keys(Keys.BACKSPACE*2)
#time.sleep(5)
#user_name.send_keys("er")
#print("Input login")
password = browser.find_element(By.XPATH,'//input[@id="password"]')
password.send_keys(password_all)
print("Input password all")

password.send_keys(Keys.RETURN)

filter = browser.find_element(By.XPATH,"//select[@data-test='product_sort_container']")
filter.click()
print("Click filter")
time.sleep(5)
filter.send_keys(Keys.DOWN)
#filter.send_keys(Keys.PAGE_DOWN)
#filter = browser.find_element(By.XPATH, "//option[@value='lohi']")
time.sleep(5)
filter.send_keys(Keys.RETURN)
time.sleep(5)
print("Click filter1")
now_date = datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
name_screenshot = 'screenshot'+ now_date + '.png'
#browser.save_screenshot("d:\\Python\\avtom_selen_smit\\screen\\" + name_screenshot)
#browser.save_screenshot(".\\screen\\" + name_screenshot)
browser.save_screenshot(f'./screen/screenshot{now_date}.png')
#password = browser.find_element(By.XPATH,'//input[@id="login-button"]')
#password.click()
#print("Click login button")
#warring_text = browser.find_element(By.XPATH,'//h3[@data-test="error"]')
#//*[@id="login_button_container"]/div/form/div[3]/h3
#value_warring_text = warring_text.text
#assert value_warring_text == "Epic sadface: Username and password do not match any user in this service"
#print("Good test")
#browser.refresh()