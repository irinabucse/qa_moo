from app.locators.login import LoginPageLocators
from app.pages.base_page import BasePage


class Login(BasePage):

    VALID_EMAIL = "irinabucse.qa@gmail.com"
    VALID_PASSWD = "test12345"
    URL = "/account/signin.php"

    def log_in_as(self, username, password):
        """
        Locate, send credentials and click submit
        """
        self.visit(self.URL)  # make sure we are on right page
        self.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(username)
        self.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        self.find_element(*LoginPageLocators.SUBMIT_BTN).click()

    def logout(self):
        self.visit(self.LOGOUT_URL)

    def get_email_error(self):
        return self.get_error(*LoginPageLocators.EMAIL_FIELD)

    def get_password_error(self):
        return self.get_error(*LoginPageLocators.PASSWORD_FIELD)


