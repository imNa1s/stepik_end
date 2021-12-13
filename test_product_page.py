from .Page.product_page import Product_NY
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    Page = Product_NY(browser, link)
    Page.open()
    Page.try_find_add()
    Page.add_to_basket()
    Page.solve_quiz_and_get_code()
    Page.check_basket_equal_by_name()
    Page.check_basket_equal_by_prise()


