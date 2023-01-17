from selenium import webdriver
import time
import pickle

driver = webdriver.Chrome(executable_path='C:\\Users\\kaleev.BSW\\environments\\selenium_env\\Scripts\\chromedriver.exe')
driver.get('https://beonmax.com/')
for cookie in pickle.load(open('session','rb')):
    driver.add_cookie(cookie)
print('куки считаны с файла session')
driver.get('https://beonmax.com/')

