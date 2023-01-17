from selenium import webdriver
import time
import math 
try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #Нажимаем на кнопку
    button = browser.find_element_by_css_selector(".btn")
    button.click()

    # ждем загрузки страницы
    
    
    confirm = browser.switch_to.alert
    confirm_text = confirm.text
    confirm.accept() 
    print("Текст из confirm", confirm)
    
    # Ваш код, который заполняет обязательные поля    
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    # y = str(math.log(abs(12*math.sin(int(x)))))
       
    # print(y)
     
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(str(math.log(abs(12*math.sin(int(x))))))
    
    button = browser.find_element_by_css_selector(".btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    
    # закрываем браузер после всех манипуляций
    browser.quit()
    