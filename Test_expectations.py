import pytest
from .Page.product_page import Product_NY


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/'
    Page = Product_NY(browser, link)
    Page.open()
    Page.try_find_add()
    Page.add_to_basket()
    Page.check_add_book_in_basket()


def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/'
    Page = Product_NY(browser, link)
    Page.open()
    Page.check_add_book_in_basket()


def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/'
    Page = Product_NY(browser, link)
    Page.open()
    Page.try_find_add()
    Page.add_to_basket()
    Page.check_disappear_msg()
