import time 
import math 
from selenium import webdriver


link = "http://suninjuly.github.io/find_link_text"
link1 = "http://suninjuly.github.io/simple_form_find_task.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    sum=str(math.log(abs((12 * math.sin(float(279))))))
    #browser.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000))).click()
    print(sum)
    # bb = browser.find_element_by_link_text("sum")
    # bb.click()
    
    
    # browser.get(link1)
    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("form-control.city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

