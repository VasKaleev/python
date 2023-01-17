import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def runChromeDriverManager():
    return webdriver.Chrome(ChromeDriverManager().install())

link = "https://dev.mineplex.io/"

@pytest.fixture(scope="class")
def browser():
    print("\nОткрываю браузер для теста логина")
    browser = runChromeDriverManager()
    #print("title project", browser.title)
    browser.implicitly_wait(5)
    #yield pasw
    yield browser
    print("\nЗакрываю после успешного теста")
    browser.quit()

class TestMainPage1(): 
    #pa= "Gw1pqh5yxQ"  
    pa = input("\nВведите пароль:") 
    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.set_window_size(1024, 600)
        #browser.set_window_position(900,10)
        #browser.maximize_window()
        #browser.fullscreen_window()
        time.sleep(5)
        #browser.find_element(
        #    By.CSS_SELECTOR, ".MuiInputBase-input.MuiOutlinedInput-input").send_keys("Gw1pqh5yxQ")
        browser.find_element(
            By.CSS_SELECTOR, ".MuiInputBase-input.MuiOutlinedInput-input").send_keys(self.pa)    
        browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(5)
#pytest -s -v -m smoke d:\Python\python_avotest\MineplexAutoTest\test_login.py
