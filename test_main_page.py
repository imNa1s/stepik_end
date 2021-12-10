import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_diff_language(browser):
    browser.get(link)
    browser.implicitly_wait(10)
    check = browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert len(check) > 0, "can't find button"
    time.sleep(5)
