from .base_page import Base_Page
from selenium.webdriver.common.by import By


class Main_Page(Base_Page):
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#registration_link")
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link_invalid"), "Login link is not presented"

