from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля    
    x_element = browser.find_element_by_id("input_value")
  
    x = x_element.text
        
    print(x)
         
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(str(math.log(abs(12*math.sin(int(x))))))

    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
    
    browser.execute_script("window.scrollBy(0, 200);")
    
    #browser.execute_script("button = document.getElementsByTagName("button")[0];button.scrollIntoView(true);")

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
    