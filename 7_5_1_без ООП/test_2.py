# python -m pytest -s -v -p no:warnings d:\Python\auto_py_al_sm\7_15_1\pages\test_2.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from win32api import GetSystemMetrics
#from webdriver_manager.firefox import GeckoDriverManager
import time

#Запуск браузера Chrome
def runChromeDriverManager():
    return webdriver.Chrome(ChromeDriverManager().install())
browser = runChromeDriverManager()    

#Запуск браузера Firefox
#browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())

#driver = webdriver.Chrome(executable_path='C:\\Users\\kaleev.BSW\\environments\\selenium_env\\Scripts\\chromedriver.exe')
url = "https://5element.by/catalog/1383-noutbuki"
browser.get(url)
browser.maximize_window()
browser.delete_all_cookies()
cooki = "//button[@class='js-cookie-popup-close btn btn--block']"
cooki_button = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH,cooki)))
cooki_button = browser.find_element(By.XPATH,"//button[@class='js-cookie-popup-close btn btn--block']")
cooki_button.click()
print("Нажали кнопку принять куки")
tovar_s_vitriny = "(//div[@class='inp-box__text filter-label'])[2]"
tovar_s_vitriny = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, tovar_s_vitriny)))
tovar_s_vitriny.click()
print("Нажали checkbox Товар c витрины")
time.sleep(2)
checkbox_filter_tov_v_rassr = "//div[text()='Товары в рассрочку']"
checkbox_filter_tov_v_rassr = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH,checkbox_filter_tov_v_rassr)))
checkbox_filter_tov_v_rassr.click()
print("Нажали checkbox Товары в рассрочку")
time.sleep(2)
filter_uchebn = "//a[@href='https://5element.by/catalog/1383-noutbuki/diagonal-ekrana=11-6,13-3,13-4,13-5,13-9,14-0,14-1,15-6;installment=1']"
filter_uchebn = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH,filter_uchebn)))
filter_uchebn.click()
print("Нажали filter_uchebn")
button_sort = "//span[@class='ic-sort']"
time.sleep(2)
button_sort = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH,button_sort)))
button_sort.click()
time.sleep(2)
print("Нажали кнопку сортировка")
sort_reiting = "//div[text()='По рейтингу']"
sort_reiting = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH,sort_reiting)))
sort_reiting.click()
time.sleep(2)
print("Нажали кнопку сортировка по рейтингу")
vid = "//button[@class='btn btn--index btn--square']"
vid = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH,vid)))
vid.click()
time.sleep(2)
print("Нажали кнопку vid товаров")
print("Monitor Height =", GetSystemMetrics(1))
SCROLL_PAUSE_TIME = 1
browser.execute_script("window.scrollTo(0, window.scrollY + 500)")
print("Click chekbox filter tovar v rassrochku down")
#webdriver.ActionChains(browser).send_keys(Keys.PAGE_DOWN).perform()

#Название товара перед добавлением в корзину
naz_prod_1 = "(//a[@class='c-text'])[1]"
nazv_prod_1 = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH,naz_prod_1)))
nazv_product_1 = nazv_prod_1.text
print("Название товара перед добавлением в корзину", nazv_product_1)

#Сумма товара перед добавлением в корзину
value_price_prod_1 = "(//div[@class='c-price'])[1]"
value_price_prod_1 = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH,value_price_prod_1)))
value_price_product_1 = value_price_prod_1.text
print("Сумма товара перед добавлением в корзину", value_price_product_1)

#Добавляем товар в корзину
cart = "(//button[@class='btn c-cart ec-add-to-cart'])[1]"
cart = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH,cart)))
cart.click()
time.sleep(2)
print("Нажали кнопку добавить в корзину")
time.sleep(5)


#Проверка после добавления товара в козину
#Проверяем название товара после добавления в корзину
cart_product_1 = browser.find_element(By.XPATH,'(//a[@href="/products/756280-ultrabuk-msi-prestige-14evo-a12m-244xby"])[4]')
nazv_cart_product_1 = cart_product_1.text
print("Название товара: ",nazv_cart_product_1)
assert nazv_cart_product_1 == nazv_product_1
print("INFO Название товара на сайте и в корзине совпадают") 
time.sleep(2)
#Проверяем цену товара после добавления в корзину
price_cart_product_1 = browser.find_element(By.XPATH,"//div[@class='m-price']")
value_cart_price_product_1 = price_cart_product_1.text
print("Цена товара: ",value_cart_price_product_1)
sum_tov1 = float(value_cart_price_product_1[1:])
#print("Тип переменной суммы товаров",type(sum_tov1))
assert value_price_product_1 == value_cart_price_product_1
print("Цена на сайте и после добавления в корзину совпадает") 
time.sleep(2)

browser.quit()
""" user_name = "//input[@name='login']"
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
print("Закрыли модальное окно бонусы") """
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