from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options, executable_path='C:\\Users\\kaleev.BSW\\environments\\selenium_env\\Scripts\\chromedriver.exe')
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()
login_standart_user = "standard_user"
password_all = "secret_sauce"

user_name = driver.find_element(By.XPATH,"//*[@id='user-name']")
user_name.send_keys(login_standart_user)
print("Input login")
pasw = driver.find_element(By.XPATH,"//*[@id='password']")
pasw.send_keys(password_all)
print("Input Password")
but_login = driver.find_element(By.XPATH,"//input[@id='login-button']").click()
print("Click Login Button")



