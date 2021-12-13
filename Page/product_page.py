from selenium.common.exceptions import NoAlertPresentException
from .base_page import BasePage
from .locators import ProdNYLocators
import math


class Product_NY(BasePage):
    def add_to_basket(self):
        basket_add = self.browser.find_element(*ProdNYLocators.FIND_BASKET)
        basket_add.click()

    def try_find_add(self):
        assert self.is_element_present(*ProdNYLocators.FIND_BASKET), "can't see add button"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")