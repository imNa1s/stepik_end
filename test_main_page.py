from .Page.main_page import Main_Page


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    Page = Main_Page(browser, link)
    Page.open()
    Page.go_to_login_page()
    Page.should_be_login_link()
