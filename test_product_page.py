from .Page.product_page import Product_NY


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    Page = Product_NY(browser, link)
    Page.open()
    Page.try_find_add()
    Page.add_to_basket()
    Page.solve_quiz_and_get_code()

