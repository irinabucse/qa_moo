from app.locators.login import LoginPageLocators
from app.pages.base_page import BasePage


class Login(BasePage):
    def __init__(self):
        self.URL = "/account/signin.php"

    def log_in_as(self, username, password):
        """
        Locate, send credentials and click submit
        """
        self.visit(self.URL)  # make sure we are on right page
        self.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(username)
        self.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        self.find_element(*LoginPageLocators.SUBMIT_BTN).click()

    def get_source(self):
        return self.browser.page_source
