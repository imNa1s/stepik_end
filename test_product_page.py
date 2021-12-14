import pytest
from Page.login_page import LoginPage
from .Page.product_page import Product_NY
from .Page.base_page import BasePage


@pytest.mark.parametrize('end', ["0", "1", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, end):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{end}'
    Page = Product_NY(browser, link)
    Page.open()
    Page.try_find_add()
    Page.add_to_basket()
    Page.solve_quiz_and_get_code()
    Page.check_basket_equal_by_name()
    Page.check_basket_equal_by_prise()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasePage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasePage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
