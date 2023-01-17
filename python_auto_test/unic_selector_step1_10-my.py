from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    elements = browser.find_element(By.CSS_SELECTOR,".first_block > div:nth-child(1) > input").send_keys("Иванов")
    #elements = browser.find_element(By.CSS_SELECTOR,"form>div.first_block>div>input.first").send_keys("Иванов")
    
    
    #elements = browser.find_element(By.CSS_SELECTOR,".first_block > div:nth-child(2) > input").send_keys("Иван")
    #elements = browser.find_element(By.CSS_SELECTOR,"form>div.first_block>div>input.second").send_keys("Иван")
    elements = browser.find_element(By.CSS_SELECTOR,".form-control.second").send_keys("Иван")
    
    #elements = browser.find_element(By.CSS_SELECTOR,".first_block > div:nth-child(3) > input").send_keys("nety@mail.ru")
    elements = browser.find_element(By.CSS_SELECTOR,"form >div.first_block>div>input.third").send_keys("nety@mail.ru")
    
    elements = browser.find_element(By.CSS_SELECTOR,"form>div.second_block>div.first_class>input").send_keys("+375 29 333 22 11")
    #elements = browser.find_element(By.CSS_SELECTOR,".second_block div:nth-child(1) input").send_keys("+375 29 333 22 11")
    
    #elements = browser.find_element(By.CSS_SELECTOR,"form>div.second_block>div.second_class>input").send_keys("Minsk")
    elements = browser.find_element(By.CSS_SELECTOR,".second_block div:nth-child(2) input").send_keys("Minsk")
    
    time.sleep(1)
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()