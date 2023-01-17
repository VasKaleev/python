import pytest

# from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage1:
    # вызываем фикстуру в тесте, передав ее как параметр
    @pytest.mark.usefixtures("browser")
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")
        print("Тест ссылки #login_link")
        print("Из файла test_fixture3.py")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
        print("Тест ссылки .basket-mini .btn-group > a")
        print("Из файла test_fixture3.py")
        print("Завершение теста")

    # @pytest.mark.usefixtures("quit")
    # def test_quit(self, browser):
    #    browser.quit
