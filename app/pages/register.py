import random

from app.locators.login import LoginPageLocators
from app.pages.base_page import BasePage


class Register(BasePage):

    URL = "/account/signin.php?state=signUp"

    def register_as(self, firstname, lastname, username, password, password2):
        """
        Locate, fill form and click submit
        """
        self.visit(self.URL)  # make sure we are on right page
        self.find_element(*LoginPageLocators.FIRSTNAME_FIELD).send_keys(firstname)
        self.find_element(*LoginPageLocators.LASTNAME_FIELD).send_keys(lastname)
        self.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(username)
        self.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        self.find_element(*LoginPageLocators.PASSWORD_CONFIRM_FIELD).send_keys(password2)
        self.find_element(*LoginPageLocators.SUBMIT_BTN).click()

    def generate_credentials(self):
        rnd = random.randrange(10000, 100000)
        return ("testemail%d@mailinator.com" % rnd, "Test12345")
