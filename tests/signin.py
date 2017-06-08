from app.pages.login import Login
from tests.testcase import TestCase


class Signin(TestCase):

    page = Login()

    def test_succesfull_login(self):
        email = "irinabucse.qa@gmail.com"
        passwd = "test12345"

        self.page.log_in_as(email, passwd)
        self.assertIn("Sign out", self.page.get_source())
