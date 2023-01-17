from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
""" browser.get("https://www.wildberries.by/catalog/38947926/detail.aspx?targetUrl=MI")
time.sleep(5)
button1 = browser.find_element(By.CSS_SELECTOR,".sizes-list__item:nth-child(3) .sizes-list__size")
#.sizes-list__item:nth-child(4) > .j-size
button1.click()
time.sleep(5)
button2 = browser.find_element(By.CSS_SELECTOR,".product-page__order-container > .order .hide-mobile")
#.product-page__order-container > .order .hide-mobile
time.sleep(5)
button2.click()
time.sleep(5) """
browser.get("https://www.mvideo.ru")
time.sleep(10)
button1 = browser.find_element(By.CSS_SELECTOR,".input input").send_keys("телевизоры samsung")
time.sleep(3)
button2 = browser.find_element(By.CSS_SELECTOR,".search-icon-wrap mvid-icon").click()
elems = browser.find_elements(By.CSS_SELECTOR, "a.product-title__text")
time.sleep(3)
print("Сюда мы попали")
print(elems)
time.sleep(10)
for elem in elems:
    print(elem.text)
    print("Сюда мы попали1")
print("Сюда мы попали2")   
time.sleep(3) 
#print(*elems, sep='\n')
#time.sleep(25)
#browser.close()
#browser.quit()

 
