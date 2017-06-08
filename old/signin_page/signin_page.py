import unittest
from selenium import webdriver
import random

class Login(unittest.TestCase):
    _base_url = "https://www.moo.com/uk/account/signin.php"
    driver = webdriver.Firefox()

    def __init__(self, *args, **kwargs):
        super(Login, self).__init__(*args, **kwargs)


    @classmethod
    def setUpClass(cls):
        cls.driver.maximize_window()

    def setUp(self):
        self.driver.get(self._base_url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


    def test_succesfull_login(self):
        email = "irinabucse.qa@gmail.com"
        passwd = "test12345"
        self.driver.find_element_by_class_name("fancy-radio").click()
        self.driver.find_element_by_xpath('//input[@data-webdriver-automation-id="signin-email"]').send_keys(email)
        self.driver.find_element_by_xpath('//input[@data-webdriver-automation-id="signin-password"]').send_keys(passwd)
        self.driver.find_element_by_xpath('//button[@data-webdriver-automation-id="signin-button"]').click()
        self.assertIn("Sign out", self.driver.page_source)

    def test_required_fields(self):
        self.driver.find_element_by_xpath('//button[@data-webdriver-automation-id="signin-button"]').click()

        # 1. Check email address
        # find input element
        input = self.driver.find_element_by_xpath('//input[@data-webdriver-automation-id="signin-email"]')
        # find the 2nd parent of it
        parent = input.find_element_by_xpath('../..') # return elem with class "col-7"
        # this parent contains the element that have the error message inside
        # get it's text
        text = parent.find_element_by_class_name("has-error-msg").text
        self.assertEqual(text, "Please enter your email address")

        # find the parent of the element with class "col-7"
        container = parent.find_element_by_xpath('..') # return elem with class "form-group has-error"
        self.assertEqual("form-group has-error", container.get_attribute("class"))

        # 2. Check password
        # find input element
        input = self.driver.find_element_by_xpath('//input[@data-webdriver-automation-id="signin-password"]')
        # find the 2nd parent of it
        parent = input.find_element_by_xpath('../..')
        # this parent contains the element that have the error message inside
        # get it's text
        text = parent.find_element_by_class_name("has-error-msg").text
        # assert
        self.assertEqual(text, "Please enter your password")
        # find the parent of the element with class "col-7"
        container = parent.find_element_by_xpath('..') #parintele lu col-7
        # assert
        self.assertEqual("form-group has-error", container.get_attribute("class"))

    def test_invalid_email(self):
        email = "gigel"
        passwd = "test12345"
        self.driver.find_element_by_xpath('//input[@data-webdriver-automation-id="signin-email"]').send_keys(email)
        self.driver.find_element_by_xpath('//input[@data-webdriver-automation-id="signin-password"]').send_keys(passwd)
        self.driver.find_element_by_xpath('//button[@data-webdriver-automation-id="signin-button"]').click()
        # find input element
        input = self.driver.find_element_by_xpath('//input[@data-webdriver-automation-id="signin-email"]')
        # find the 2nd parent of it
        parent = input.find_element_by_xpath('../..')
        # this parent contains the element that have the error message inside
        # get it's text
        text = parent.find_element_by_class_name("has-error-msg").text
        # assert
        self.assertEqual(text, "Please enter a valid email address")
        # find the parent of the element with class "col-7"
        container = parent.find_element_by_xpath('..')  # parintele lu col-7
        # assert
        self.assertEqual("form-group has-error", container.get_attribute("class"))

    def test_wrong_passwd(self):
        email = "irinabucse.qa@gmail.com"
        passwd = "12"
        self.driver.find_element_by_xpath('//input[@data-webdriver-automation-id="signin-email"]').send_keys(email)
        self.driver.find_element_by_xpath('//input[@data-webdriver-automation-id="signin-password"]').send_keys(passwd)
        self.driver.find_element_by_xpath('//button[@data-webdriver-automation-id="signin-button"]').click()
        # 2. Check password
        # find input element
        input = self.driver.find_element_by_xpath('//input[@data-webdriver-automation-id="signin-password"]')
        # find the 2nd parent of it
        parent = input.find_element_by_xpath('../..')
        # this parent contains the element that have the error message inside
        # get it's text
        text = parent.find_element_by_class_name("has-error-msg").text
        # find the parent of the element with class "col-7"
        container = parent.find_element_by_xpath('..')
        self.assertIn("Your password or email doesn't match what we have for you. Please try again. ", self.driver.page_source)

