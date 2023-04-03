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
class Cart_page(Base):

    #Locators
    checkout_button = "//button[@id='checkout']"
   
    #Getters
    def get_checkout_button(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))
    
    #Actions
    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("Click checkout_button")
  
    #Methods
    def product_confirmation(self):
        #self.browser.get(self.url)
        self.click_checkout_button()
    