from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("num1")
    x = x_element.text
    x_element1 = browser.find_element_by_id("num2")
    x1 = x_element1.text
    
    # x_element = browser.find_element_by_id("treasure")
    # valuex = x_element.get_attribute("valuex")
    # x = valuex
        
    print(type(x))
    print(int(x1))
    sum=int(x)+int(x1)
    sum1=str(sum)
    print('Сумма', sum, 'Тип', type(sum))
        
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(sum1) # ищем элемент с текстом 

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector(".btn")
    button.click()
    # ждем загрузки страницы
    time.sleep(1)

   
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    
    # закрываем браузер после всех манипуляций
    browser.quit()
    
    