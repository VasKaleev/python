from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from datetime import datetime,timedelta
from webdriver_manager.chrome import ChromeDriverManager
import time

#Запуск браузера Chrome
def runChromeDriverManager():
    return webdriver.Chrome(ChromeDriverManager().install())
browser = runChromeDriverManager()    

#Запуск браузера Firefox
#browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())

#driver = webdriver.Chrome(executable_path='C:\\Users\\kaleev.BSW\\environments\\selenium_env\\Scripts\\chromedriver.exe')
base_url = 'https://demoqa.com/date-picker'
browser.get(base_url)
browser.maximize_window()
time.sleep(2)
now_date = browser.find_element(By.XPATH,'//input[@id="datePickerMonthYearInput"]')
time.sleep(2)
now_date.click()
date_value = now_date.get_attribute('value')
print(date_value)
print(type(date_value))

date_string = "03/10/2023"
date_object = datetime.strptime(date_string, "%d/%m/%Y").date()
print(date_object)

#data1 = datetime.strptime(date_value, '%d/%m/%y %H:%M:%S')
#print(data1)

#now_date = datetime.utcnow().strftime("%d")
#now = datetime.now()
#print(type(now))
#print(type(now_date))
#now_date = datetime.utcnow().strftime("%d")
#end_date = date_value + timedelta(days=11)

#print(end_date)
#day_now_date = end_date.strftime("%A")
#print(day_now_date)

""" date = int(now_date) + 1
locator = "//div[@aria-label='Choose Saturday, March " + str(date) +"th, 2023']"
print(locator)
time.sleep(5)
date_17 = browser.find_element(By.XPATH,locator)
date_17.click()
print(date_17)
time.sleep(5) """



