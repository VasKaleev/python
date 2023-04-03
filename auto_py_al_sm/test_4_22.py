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
base_url = 'https://demoqa.com/date-picker'
browser.get(base_url)
browser.maximize_window()
time.sleep(5)

action = ActionChains(browser)
new_date = browser.find_element(By.XPATH,'//input[@id="datePickerMonthYearInput"]')
""" new_date.send_keys(Keys.BACKSPACE*10)
time.sleep(5)
new_date.send_keys('06/17/2023')
new_date.send_keys(Keys.RETURN)
time.sleep(5) """
#new_date.clear()
time.sleep(5)
#date_17 = browser.find_element(By.XPATH,"//div[@aria-label='Choose Saturday, March 11th, 2023']")
#date_17.click()
#react-datepicker__day--selected
#react-datepicker__day--today
#//div[contains(@class,'react-datepicker__day--today')]
#new_date = driver.find_element(By.XPATH, "//*[@id = 'datePickerMonthYearInput']") #поиск поля календаря
#date_value = new_date.get_attribute('value') # получение значения из этого поля
#clear_symbol = (len(date_value)) # подсчет количества символов в значение
#new_date.send_keys(Keys.BACKSPACE*clear_symbol) # удаления значения, где переменная clear_symbol означает сколько нажать BACKSPACE
#date_17 = browser.find_element(By.XPATH,"//div[contains(@class,'react-datepicker__day--today')]")
#now_date = datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
new_date.click()
now_date = datetime.utcnow().strftime("%d")
print(now_date)
date = int(now_date) + 1
locator = "//div[@aria-label='Choose Saturday, March " + str(date) +"th, 2023']"
print(locator)
time.sleep(5)
date_17 = browser.find_element(By.XPATH,locator)
date_17.click()
print(date_17)
time.sleep(5)



