from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from login_page import Login_page
import time
class Test_2():
    def test_select_product(self):
        #Запуск браузера Chrome
        def runChromeDriverManager():
            return webdriver.Chrome(ChromeDriverManager().install())
        browser = runChromeDriverManager() 
        #Запуск браузера Firefox
        #browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())

        #driver = webdriver.Chrome(executable_path='C:\\Users\\kaleev.BSW\\environments\\selenium_env\\Scripts\\chromedriver.exe')
        base_url = 'https://www.saucedemo.com/'
        browser.get(base_url)
        browser.maximize_window()
        time.sleep(5)

        print("Start test")
        browser.implicitly_wait(10)

        login_problem_user = "problem_user"
        password_all = "secret_sauce"

        login = Login_page(browser)
        #login.authorization(login_name = "standard_user", login_password = "secret_sauce")
        login.authorization(login_problem_user, password_all)

        select_product = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH,'//button[@id="add-to-cart-sauce-labs-backpack"]')))
        select_product.click()
        print("Click select_product")

        enter_shopping_cart = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH,'//div[@id="shopping_cart_container"]')))
        enter_shopping_cart.click()
        print("Click enter_shopping_cart")

        success_test = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH,'//span[@class="title"]')))
        value_success_test = success_test.text
        assert value_success_test == 'Your Cart'
        print('Test success')


test = Test_2()
test.test_select_product()

