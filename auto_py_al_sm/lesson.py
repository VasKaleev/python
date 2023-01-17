from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path='C:\\Users\\kaleev.BSW\\environments\\selenium_env\\Scripts\\chromedriver.exe')
driver.get('https://www.saucedemo.com/')
driver.maximize_window()
time.sleep(10)
driver.close()

