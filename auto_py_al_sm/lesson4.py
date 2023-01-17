from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path='C:\\Users\\kaleev.BSW\\environments\\selenium_env\\Scripts\\chromedriver.exe')
driver.get('https://www.saucedemo.com/')
driver.maximize_window()
#user_name = driver.find_element_by_id("user-name")
user_name = driver.find_element(By.ID,"user-name")
user_name.send_keys("standard_user")



""" time.sleep(10)
driver.close() """

