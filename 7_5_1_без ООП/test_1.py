from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
#from webdriver_manager.firefox import GeckoDriverManager
import time

#Запуск браузера Chrome
def runChromeDriverManager():
    return webdriver.Chrome(ChromeDriverManager().install())
browser = runChromeDriverManager()    

#Запуск браузера Firefox
#browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())

#driver = webdriver.Chrome(executable_path='C:\\Users\\kaleev.BSW\\environments\\selenium_env\\Scripts\\chromedriver.exe')
url = "https://5element.by/"
browser.get(url)
browser.maximize_window()
browser.delete_all_cookies()
cooki = "//button[@class='js-cookie-popup-close btn btn--block']"
cooki_button = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH,cooki)))
#cooki_button = browser.find_element(By.XPATH,"//button[@class='js-cookie-popup-close btn btn--block']")
cooki_button.click()
print("Нажали кнопку принять куки")
vhod = "//span[@class='ic-h-user']"
vhod_button = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH,vhod)))
vhod_button.click()
print("Нажали кнопку Вход")

user_name = "//input[@name='login']"
vvod_user_name = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH,user_name)))
vvod_user_name.send_keys("kaleev.fam@mail.ru")
password =  "//input[@type='password']"
vvod_password = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH,password)))
vvod_password.send_keys("Lytghlytgh1")
login_button = "//span[text()='Войти']"
voiti = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH,login_button)))
voiti.click()
#modal_popap = "(//button[@class='modal-popup-close ic-close'])[1]"
#modal_popap = "/html/body/div[1]/div[24]/div/button"
#modal_popap = "div.modal-popup-wrap:nth-child(26) > div:nth-child(1) > button"
modal_popap = "(//button[@type='button'])[36]"
popap = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH,modal_popap)))
popap.click()
print("Закрыли модальное окно бонусы")
#popap.send_keys(Keys.ESCAPE)
#webdriver.ActionChains(browser).send_keys(Keys.ESCAPE).perform()
#time.sleep(10)
#browser.find_element_by_xpath("//button[@aria-label='close modal']").click()

""" login_standard_user = "standard_user"
password_all = "secret_sauce"
user_name.send_keys(login_standard_user)
print("Input login")
password = browser.find_element(By.XPATH,'//input[@id="password"]')
password.send_keys(password_all)
print("Input password all")
password = browser.find_element(By.XPATH,'//input[@id="login-button"]')
password.click()
print("Click login button")
text_products = browser.find_element(By.XPATH,'//span[@class="title"]')
value_text_products = text_products.text
print(value_text_products)
assert value_text_products == "PRODUCTS"
print("GOOD!") 
url = "https://www.saucedemo.com/inventory.html"
get_url = browser.current_url
print(get_url)
assert url == get_url
print("GOOD URL")
time.sleep(10)
#browser.close()  """