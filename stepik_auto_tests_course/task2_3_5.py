from selenium import webdriver
import time
import math 
try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #Нажимаем на кнопку
    button = browser.find_element_by_css_selector(".trollface")
    button.click()

    # Находим второе открывшееся окно
    browser.switch_to.window(browser.window_handles[1])
      
    # Ваш код, который заполняет обязательные поля    
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    # y = str(math.log(abs(12*math.sin(int(x)))))
       
    print(x_element)
     
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(str(math.log(abs(12*math.sin(int(x))))))
    
    button = browser.find_element_by_css_selector(".btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    
    # закрываем браузер после всех манипуляций
    browser.quit()
    