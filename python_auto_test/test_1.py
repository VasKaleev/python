from selenium import webdriver
import time 

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

try:
    browser = webdriver.Chrome()
    browser.get(link)
 
    input3 = browser.find_element_by_class_name("button.btn.btn-lg.btn-primary")
    

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    #browser.quit()

# не забываем оставить пустую строку в конце файла
