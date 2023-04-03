from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def runChromeDriverManager():
    return webdriver.Chrome(ChromeDriverManager().install())
browser = runChromeDriverManager()    

#driver = webdriver.Chrome(executable_path='C:\\Users\\kaleev.BSW\\environments\\selenium_env\\Scripts\\chromedriver.exe')
browser.get('https://www.saucedemo.com/')
browser.maximize_window()
time.sleep(10)
#user_name = driver.find_element_by_id("user-name")
#user_name = driver.find_element(By.ID,"user-name")
#user_name = browser.find_element(By.NAME,"user-name")
#user_name = browser.find_element(By.XPATH,"//input[@id='user-name']")
#user_name = browser.find_element(By.XPATH,"//*[@id='user-name']")
user_name = browser.find_element(By.XPATH,"//*[@data-test='username']")
user_name.send_keys("standard_user")
password = browser.find_element(By.CSS_SELECTOR,"#password")
password.send_keys("secret_sauce")
button_login = browser.find_element(By.XPATH,"//input[@value='Login']").click()
time.sleep(10)




time.sleep(10)
#driver.close() 

