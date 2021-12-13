from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOG_PAGE_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")


class ProdNYLocators:
    FIND_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, '.row h1')
    ADD_NAME_BOOK = (By.CSS_SELECTOR, ".alertinner>strong")
    BOOK_PRICE = (By.CSS_SELECTOR, ".p.price_color")
    PRICE_ADD_BOOK = (By.CSS_SELECTOR, ".alertinner p strong")

