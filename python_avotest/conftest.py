import pytest
from selenium import webdriver

# from selenium.webdriver.common.by import By


@pytest.fixture
def browser():
    print("\nЗапускаем раузер Google Chrome для автотеста...")
    print("Из фикстуры в файле conftest.py")
    browser = webdriver.Chrome()
    return browser


@pytest.fixture
def quit():
    browser.quit()
