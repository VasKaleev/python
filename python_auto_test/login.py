import pytest
from selenium import webdriver
class TestLogin(object):
def test_guest_should_see_login_link(cls, browser, language): 
print("# номер 4")
cls.browser = webdriver.Chrome()
