# python -m pytest -s -v
#pip list Посмотреть что установлено для python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from base.base_class import Base
class Login_page(Base):

    url = 'https://www.saucedemo.com/'

    """ def __init__(self, browser):
        super.__init__(browser)
        self.browser = browser """

    #Locators
    user_name = '//input[@id="user-name"]'
    password =  '//input[@id="password"]'
    login_button = '//input[@id="login-button"]'
    main_word = "//span[@class='title']"

    #Getters
    def get_user_name(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))
    def get_password(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))
    def get_login_button(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))
    def get_main_word(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))
    
    #Actions
    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input user name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click login_button")

    #Methods
    def authorization(self):
        self.browser.get(self.url)
        self.browser.maximize_window() 
        self.get_current_url()
        self.input_user_name("standard_user")
        self.input_password("secret_sauce")
        self.click_login_button()
        self.assert_word(self.get_main_word(), "Products")