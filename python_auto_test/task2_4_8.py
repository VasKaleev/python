from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
btn = browser.find_element_by_id("book") 
btn.click()

#Код, который заполняет обязательные поля    
x_element = browser.find_element_by_id("input_value")
x = x_element.text
       
print(x_element)
     
input1 = browser.find_element_by_id("answer")
input1.send_keys(str(math.log(abs(12*math.sin(int(x))))))
    
button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "solve"))
    )
button.click()

