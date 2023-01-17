from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля    
    # x_element = browser.find_element_by_id("input_value")
    # x = x_element.text
    x_element = browser.find_element_by_id("treasure")
    valuex = x_element.get_attribute("valuex")
    x = valuex
        
    print(x)
    # def calc(x):
       # return str(math.log(abs(12*math.sin(int(x)))))
    y = str(math.log(abs(12*math.sin(int(x)))))
    
    
    print(y)
     
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()

    option2 = browser.find_element_by_css_selector("[value='robots']")
    option2.click()      

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector(".btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

   
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    
    # закрываем браузер после всех манипуляций
    browser.quit()
    