from selenium import webdriver
import time
import os 
try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_css_selector('input.form-control:nth-child(2)')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector('input.form-control:nth-child(4)')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector('input.form-control:nth-child(6)')
    input3.send_keys("123@qwe.com")
    #time.sleep(10)
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'test.txt')           # добавляем к этому пути имя файла 
    #element = browser.find_element(By.cssSelector, "[type='file']") #file
    #element =  browser.find_element(By.cssSelector("input[name='file']"));
    element = browser.find_element_by_css_selector("input[name='file']")
    element.send_keys(file_path)
    
    print(os.path.abspath(__file__))
    print(os.path.abspath(os.path.dirname(__file__)))

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector(".btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(3)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name('h1')
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    
    # закрываем браузер после всех манипуляций
    browser.quit()
    