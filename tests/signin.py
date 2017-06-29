from app.pages.login import Login
from tests.testcase import TestCase


class Signin(TestCase):

    page = Login()

    def test_succesfull_login(self):
        self.page.log_in_as(self.page.VALID_EMAIL, self.page.VALID_PASSWD)
        self.assertIn("Sign out", self.page.get_source())
        self.page.logout()

    def test_required_fields(self):
        self.page.log_in_as("", "")
        self.assertEqual("Please enter your email address", self.page.get_email_error())
        self.assertEqual("Please enter your password", self.page.get_password_error())

    def test_invalid_email(self):
        self.page.log_in_as("invalid_email", "some password")
        self.assertEqual("Please enter a valid email address", self.page.get_email_error())

    def test_wrong_passwd(self):
        self.page.log_in_as(self.page.VALID_EMAIL, "wrong password")
        self.assertIn("Your password or email doesn't match what we have for you. Please try again. ", self.page.get_source())

