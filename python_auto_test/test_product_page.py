from pages.product_page import ProductPage
from pages.login_page import LoginPage
#from pages.basket_page import BasketPage
import pytest
import time
#@pytest.mark.login
class TestUserAddToBasketFromProductPage(): 
    def test_guest_can_add_product_to_basket(browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        #page.should_not_be_success_message()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        #page.should_be_message_about_product_added_to_basket()
        #page.should_be_message_basket_total()

