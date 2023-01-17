import time
import math
import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
@pytest.mark.parametrize('url', ["236895/step/1", "236896/step/1", "236897/step/1", "236898/step/1", "236899/step/1", "236903/step/1", "236904/step/1", "236905/step/1"])
def test_guest_should_see_login_link(browser, url):
    link = f"https://stepik.org/lesson/{url}/"
    browser.get(link)
    #browser.implicity_wait(12)
    #textarea = WebDriverWait(browser, 5).until(
    #    EC.element_to_be_clickable((By.cssSelector, "ember-text-area"))
    #)
    time.sleep(12)
    text_area = browser.find_element_by_tag_name('textarea')
    #browser.find_element_by_css_selector(".ember-text-area")
    #answer = math.log(int(time.time()))
    text_area.send_keys(str(math.log(int(time.time()))))
    time.sleep(12)
    # Отправляем заполненную форму
    but = browser.find_element_by_tag_name('button')
    time.sleep(12)
    but.click()
    time.sleep(10)
    #but = WebDriverWait(browser, 10).until(
    #    EC.element_to_be_clickable((By.CSS_SELECTOR, "submit-submission")
    #but.click() 
    #button = WebDriverWait(browser, 5).until(
    #    EC.element_to_be_clickable((By.CSS_SELECTOR, "submit-submission"))
    #)
    #button.click()
