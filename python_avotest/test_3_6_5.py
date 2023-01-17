"""
pytest -s -v test_parameters.py
The owls are not what they seem! OvO
"""
from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver

import time
import math
from webdriver_manager.chrome import ChromeDriverManager


def runChromeDriverManager():
    return webdriver.Chrome(ChromeDriverManager().install())


@pytest.fixture(scope="function")
def browser():
    #    print("\nstart browser for test..")
    browser = runChromeDriverManager()
    browser.implicitly_wait(5)
    yield browser
#    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('url', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
#@pytest.mark.parametrize('url', ["236895"])
def test_guest_should_see_login_link(browser, url):
    link = "https://stepik.org/lesson/{}/step/1".format(url)
    browser.get(link)
    browser.implicitly_wait(5)
    answer = math.log(int(time.time()))
    print(answer, 'проверяем переменную')
    time.sleep(10)
    #browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
    browser.find_element(By.CSS_SELECTOR, ".ember-text-area").send_keys(
        str(answer))  # ember-auto-resize ember-view")
    time.sleep(2)
    #browser.find_element_by_class_name("submit-submission").click()
    browser.find_element(By.CSS_SELECTOR, ".submit-submission").click()
    time.sleep(10)
    # hints__component hints__component_showed ember-view")
    message = browser.find_element_by_class_name("smart-hints__feedback").text
    #time.sleep(2)
    assert message == "Correct!", "Attention, aliens!"  # - {}".format(message)
