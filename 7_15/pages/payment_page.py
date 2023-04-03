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
class Payment_page(Base):

    #Locators
    finish_button = "//button[@id='finish']"
       
    #Getters
    def get_finish_button(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.finish_button))) 
    
    #Actions
    def click_finish_button(self):
        self.get_finish_button().click()
        print("Click finish_button")

    #Methods
    def payment(self):
        self.get_current_url()
        self.click_finish_button()