import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def runChromeDriverManager():
    return webdriver.Chrome(ChromeDriverManager().install())


@pytest.fixture(scope="class")
def browser():
    print("\nОткрываю браузер для теста логина")
    browser = runChromeDriverManager()
    #print("title project", browser.title)
    browser.implicitly_wait(5)
    yield browser
    print("\nЗакрываю после успешного теста")
    browser.quit()
