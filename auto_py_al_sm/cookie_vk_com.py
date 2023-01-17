from selenium import webdriver
import time
import pickle

driver = webdriver.Chrome(executable_path='C:\\Users\\kaleev.BSW\\environments\\selenium_env\\Scripts\\chromedriver.exe')
driver.get('https://beonmax.com/')
time.sleep(100)
pickle.dump(driver.get_cookies(), open('session','wb'))
print('куки загружены в файл session')

