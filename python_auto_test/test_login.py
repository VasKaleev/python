import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options, executable_path='C:\\Users\\kaleev.BSW\\environments\\selenium_env\\Scripts\\chromedriver.exe') 

#def runChromeDriverManager():
#    return webdriver.Chrome(ChromeDriverManager().install())

link = "https://dev.mineplex.io/"
browser.get(link)
@pytest.fixture(scope="class")
def browser():
    print("\nОткрываю браузер для теста логина")
    #browser = runChromeDriverManager()
    #print("title project", browser.title)
    time.sleep(2)
    #browser.implicitly_wait(15)
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
        #print("title project", browser.title)
        #print("current_url", browser.current_url)
        #print("platformName", browser.get_cookies())
        #browser.save_screenshot('./image.png') 
        browser.set_window_size(1024, 600)
        #browser.set_window_position(900,10)
        #browser.maximize_window()
        #browser.fullscreen_window()
        time.sleep(2)
        browser.find_element(
            By.CSS_SELECTOR, ".MuiInputBase-input.MuiOutlinedInput-input").send_keys("Gw1pqh5yxQ")
        #browser.find_element(
        #    By.CSS_SELECTOR, ".MuiInputBase-input.MuiOutlinedInput-input").send_keys(self.pa)    
        browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(2)
#pytest -s -v -m smoke d:\Python\python_avotest\MineplexAutoTest\test_login.py
