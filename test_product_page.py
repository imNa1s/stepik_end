import pytest
from .Page.product_page import Product_NY
import time


@pytest.mark.parametrize('end', ["0", "1", "3", "4",  "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, end):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{end}'
    Page = Product_NY(browser, link)
    Page.open()
    Page.try_find_add()
    Page.add_to_basket()
    Page.solve_quiz_and_get_code()
    Page.check_basket_equal_by_name()
    Page.check_basket_equal_by_prise()
