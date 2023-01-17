import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(2)

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("https://stepik.org/lesson/25969/step/12")
time.sleep(20)

#Нажимаем кнопку войти на сайте
submit_button = driver.find_element_by_id("ember127")
submit_button.click()
time.sleep(2)

#Вводим логин
textarea = driver.find_element_by_id("id_login_email") 
textarea.send_keys("kaleev.fam@mail.ru")
time.sleep(2)

#Вводим email
textarea = driver.find_element_by_id("id_login_password") 
textarea.send_keys("19721972v")
time.sleep(2)

#Нажимаем войти
submit_button = driver.find_element_by_css_selector(".sign-form__btn.button_with-loader")
submit_button.click()
time.sleep(10)


# Метод find_element_by_css_selector позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
# Ищем поле для ввода текста
textarea = driver.find_element_by_css_selector(".textarea")

# Напишем текст ответа в найденное поле
textarea.send_keys("get()")
time.sleep(10)

# Найдем кнопку, которая отправляет введенное решение
submit_button = driver.find_element_by_css_selector(".submit-submission")

# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
submit_button.click()
time.sleep(2)




# # После выполнения всех действий мы не должны забыть закрыть окно браузера
# driver.quit()

# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# time.sleep(5)
# driver.get("http://svitanok.01sh.ru/")
# time.sleep(5)
# textarea = driver.find_element_by_name("search_q") 
# textarea.send_keys("Мог")
# time.sleep(5)
# submit_button = driver.find_element_by_css_selector(".kn")
# submit_button.click()
# time.sleep(5)

