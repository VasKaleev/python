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
    yield browser
    print("\nЗакрываю после успешного теста")
    browser.quit()


class TestMainPage1():

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        print('Браузер', browser.name)
        print('Титл проекта', browser.title)
        time.sleep(5)
        browser.find_element(
            By.CSS_SELECTOR, ".MuiInputBase-input.MuiOutlinedInput-input").send_keys("Gw1pqh5yxQ")
        browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(5)
