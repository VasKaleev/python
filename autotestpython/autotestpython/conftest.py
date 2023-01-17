import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome", \
                      help="Choose browser: chrome")  
    parser.addoption('--language', action='store', default='en',
        help="Choose Choose language: es of fr")    

@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")
    browser_name = request.config.getoption("browser_name")
    #Указываем язык браузера с помощью WebDriver
    #используем класс Options и метод add_experimental_option
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    
    yield browser
    print("\nquit browser..")
    browser.quit()
