#Запускаем тест с помощью команды в терминале:
#python -m pytest -s -v d:\Python\python_avotest\MineplexAutoTest\test_loginv1.py
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

""" options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options, executable_path='C:\\Users\\kaleev.BSW\\environments\\selenium_env\\Scripts\\chromedriver.exe') 
 """

def runChromeDriverManager():
    return webdriver.Chrome(ChromeDriverManager().install())

link = "https://dev.mineplex.io/"

@pytest.fixture(scope="class")
def browser():
    print("\nОткрываю браузер для теста логина")
    browser = runChromeDriverManager()
    #print("title project", browser.title)
    browser.implicitly_wait(5)
    yield browser
    print("\nЗакрываю после успешного теста")
    print("title project", browser.title)
    print("current_url", browser.current_url)
    browser.save_screenshot('./Autotest.png')
    print("cookies", browser.get_cookies()) 

    #Проверяем попали ли мы на нужную страницу
    url = "https://dev.mineplex.io/"
    urlt = browser.current_url
    assert url == urlt, "Тест1 не прошел"
    print('Попали на искомую страницу!')

    #Проверяем есть ли заголовок на нужной странице
    url_test = 'All operations - in one click'
    #url_test = """All operations -
    #in one click"""
    value_test = browser.find_element(By.XPATH,"//h3[@class='introSectionContent_title']").text
    print('Искомый текст на странице:', value_test[:16])
    assert url_test[:16] == value_test[:16], "Тест2 не прошел"
    print('Нашли искомый заголовок на странице!!')

    #browser.quit()

class TestMainPage1(): 
    #pa= "Gw1pqh5yxQ"  
    #pa = input("\nВведите пароль:") 
    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        #print("title project", browser.title)
        #print("current_url", browser.current_url)
        #print("platformName", browser.get_cookies())
        #browser.save_screenshot('./image.png') 
        browser.set_window_size(1024, 600)
        #browser.set_window_position(900,10)
        #browser.maximize_window()
        #browser.fullscreen_window()
        #time.sleep(5)
        browser.find_element(
        By.CSS_SELECTOR, ".MuiInputBase-input.MuiOutlinedInput-input").send_keys("Gw1pqh5yxQ")
        #browser.find_element(
        #    By.CSS_SELECTOR, ".MuiInputBase-input.MuiOutlinedInput-input").send_keys(self.pa)    
        browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        #time.sleep(5)

        

#pytest -s -v -m smoke d:\Python\python_avotest\MineplexAutoTest\test_loginv.py
