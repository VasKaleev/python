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
class Main_page(Base):

    #Locators
    select_product_1 = "//button[@id='add-to-cart-sauce-labs-backpack']"
    select_product_2 = "//button[@id='add-to-cart-sauce-labs-bike-light']"
    select_product_3 = "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"
    cart =  "//a[@class='shopping_cart_link']"
    menu = "//button[@id='react-burger-menu-btn']"
    link_about = "//a[@id='about_sidebar_link']"
   
    #Getters
    def get_select_products_1(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_1)))
    def get_select_products_2(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_2)))
    def get_select_products_3(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_3)))
    def get_cart(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))
    def get_menu(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu)))
    def get_link_about(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_about)))
  
    
    #Actions
    def click_select_product_1(self):
        self.get_select_products_1().click()
        print("Click select_product_1")
    def click_select_product_2(self):
        self.get_select_products_2().click()
        print("Click select_product_2")
    def click_select_product_3(self):
        self.get_select_products_3().click()
        print("Click select_product_3")    
    def click_get_cart(self):
        self.get_cart().click()
        print("Click cart")
    def click_menu(self):
        self.get_menu().click()
        print("Click menu")
    def click_link_about(self):
        self.get_link_about().click()
        print("Click link_about")    

    #Methods
    def select_products_1(self):
        self.get_current_url()
        self.click_select_product_1()
        self.click_get_cart()

    def select_products_2(self):
        self.get_current_url()
        self.click_select_product_2()
        self.click_get_cart()

    def select_products_3(self):
        self.get_current_url()
        self.click_select_product_3()
        self.click_get_cart()       

    def select_menu_about(self):
        self.get_current_url()
        self.click_menu()
        self.click_link_about()
        self.assert_url('https://saucelabs.com/')