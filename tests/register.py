from app.pages.register import Register
from tests.testcase import TestCase


class Signup(TestCase):

    page = Register()

    def test_succesfull_register(self):
        email, passwd = self.page.generate_credentials()

        self.page.register_as(
            "Firstname",
            "Lastname",
            email,
            passwd,
            passwd,
            "United Kingdom",
            "Prefer not to say"
        )

        self.assertIn("Account identity", self.page.get_source())
        self.page.logout()

    def test_succesfull_register_with_industry(self):
        email, passwd = self.page.generate_credentials()

        self.page.register_as(
            "Firstname",
            "Lastname",
            email,
            passwd,
            passwd,
            "United Kingdom",
            "Design & Creative Services",
            "Advertising & Media", #Advertising & Media
            "I work for myself"
        )

        self.assertIn("Account identity", self.page.get_source())
        self.page.logout()

    def test_required_fields(self):
        pass
