import random

from app.locators.register import RegisterPageLocators
from app.pages.base_page import BasePage


class Register(BasePage):

    URL = "/account/signin.php?state=signUp"

    def register_as(self, firstname, lastname, email, password, password2, country, industry, profession="", company_size=""):
        """
        Locate, fill form and click submit
        """
        self.visit(self.URL)  # make sure we are on right page
        self.find_element(*RegisterPageLocators.FIRSTNAME_FIELD).send_keys(firstname)
        self.find_element(*RegisterPageLocators.LASTNAME_FIELD).send_keys(lastname)
        self.find_element(*RegisterPageLocators.EMAIL_FIELD).send_keys(email)
        self.find_element(*RegisterPageLocators.PASSWORD_FIELD).send_keys(password)
        self.find_element(*RegisterPageLocators.PASSWORD_CONFIRM_FIELD).send_keys(password2)
        self.find_element(*RegisterPageLocators.INDUSTRY_SELECT).send_keys(industry)
        self.find_element(*RegisterPageLocators.COUNTRY_SELECT).send_keys(country)
        self.find_element(*RegisterPageLocators.PROFESSION_SELECT).send_keys(profession)
        self.find_element(*RegisterPageLocators.COMPANY_SIZE_SELECT).send_keys(company_size)
        self.find_element(*RegisterPageLocators.NEWSLETTER_CKB).click()
        self.find_element(*RegisterPageLocators.SUBMIT_BTN).click()

    def generate_credentials(self):
        rnd = random.randrange(10000, 100000)
        email = "testemail%d@mailinator.com" % rnd
        return email, "Test12345"
