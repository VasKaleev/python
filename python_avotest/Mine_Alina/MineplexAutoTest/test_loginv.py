#python -m pytest -s -v  d:\Python\python_avotest\MineplexAutoTest\test_login.py
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import hashlib

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
    print("title project", browser.title)
    print("current_url", browser.current_url)
    browser.save_screenshot('./Autotest.png')
    print("cookies", browser.get_cookies())  
    browser.quit()

class TestMainPage1(): 
    #pa= "Gw1pqh5yxQ"  
    #pa = input("\nВведите пароль:")
    
    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.set_window_size(1024, 600)
        pa =  "9c826670020f31438b49f47d392f8a2f" 
        input_password_encode = hashlib.md5(bytes(pa, 'utf-8')).hexdigest()
        #browser.set_window_position(900,10)
        time.sleep(5)
        #browser.find_element(
        #    By.CSS_SELECTOR, ".MuiInputBase-input.MuiOutlinedInput-input").send_keys("..........")
        browser.find_element(
            By.CSS_SELECTOR, ".MuiInputBase-input.MuiOutlinedInput-input").send_keys(hashlib.md5(bytes(pa, 'utf-8')).hexdigest())    
        browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(5)

