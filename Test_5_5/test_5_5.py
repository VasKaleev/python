from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from login_page import Login_page
from selenium.common.exceptions import TimeoutException
class Test_5_5():
    def test_select_product(self):
        #Запуск браузера Chrome
        def runChromeDriverManager():
            return webdriver.Chrome(ChromeDriverManager().install())
        browser = runChromeDriverManager()
        base_url = 'https://www.saucedemo.com/'
        browser.get(base_url)
        browser.maximize_window()
        login_name = ["standard_user", "locked_out_user", "problem_user", "performance_glitch_user"]
        password_all = "secret_sauce"
        for i in login_name:
            try:
                print("Выводим логин: ",i)
                login = Login_page(browser)
                login.authorization(i, password_all)
                success_test = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH,'//span[@class="title"]')))
                value_success_test = success_test.text
                assert value_success_test == 'Products'
                print('Test success')
                print("---------------------")
                burger_menu_button = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH,'//button[@id="react-burger-menu-btn"]')))
                burger_menu_button.click()
                print("Click burger_menu_button")  
                logout = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH,'//a[@id="logout_sidebar_link"]')))
                logout.click()
                print("Click logout")
            except TimeoutException:
                browser.refresh()
                continue
            print("End test")

test = Test_5_5()
test.test_select_product()


