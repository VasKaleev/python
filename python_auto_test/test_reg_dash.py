# для того, чтобы использовать функцию времени нужно импортировать библиотеку time 
import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(10)

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("https://authdev.mineplex.io/ru/auth/login")
time.sleep(10)

# Метод find_element_by_css_selector позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
# Ищем поле для ввода текста
input = driver.find_element_by_id("#loginForm_email")

# Напишем текст ответа в найденное поле
#input.send_keys("Kaleevaalina.fam@gmail.com")
#time.sleep(10)

# Найдем кнопку, которая отправляет введенное решение
#submit_button = driver.find_element_by_css_selector(".submit-submission")

# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
#submit_button.click()
#time.sleep(5)

# После выполнения всех действий мы должны не забыть закрыть окно браузера
#driver.quit()