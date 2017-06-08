import unittest
from selenium import webdriver
import random


class Register(unittest.TestCase):
    _base_url = "https://www.moo.com/uk/account/signin.php?state=signUp"
    driver = webdriver.Firefox()

    @classmethod
    def setUpClass(self):
        self.driver.maximize_window()

    def setUp(self):
        self.driver.get(self._base_url)

    @classmethod
    def tearDownClass(self):
        self.driver.close()

    def test_succesfull_register(self):
        rnd = random.randrange(10000, 100000)
        email = "testemail%d@mailinator.com" % rnd
        passwd = "Test12345"

        # self.driver.find_element_by_xpath('//label[@data-webdriver-automation-id="signup-option"]').click()
        self.driver.find_element_by_xpath('//input[@data-webdriver-automation-id="signup-first-name"]').send_keys("ina")
        self.driver.find_element_by_xpath('//input[@data-webdriver-automation-id="signup-last-name"]').send_keys("ina")
        self.driver.find_element_by_xpath('//input[@data-webdriver-automation-id="signup-email"]').send_keys(email)
        self.driver.find_element_by_xpath('//input[@data-webdriver-automation-id="signup-password"]').send_keys(passwd)
        self.driver.find_element_by_xpath('//input[@data-webdriver-automation-id="signup-password2"]').send_keys(passwd)

        self.driver.find_element_by_xpath('//div[@data-webdriver-automation-id="country-dropdown"]').find_element_by_tag_name("select").send_keys("United Kingdom")
        self.driver.find_element_by_xpath('//div[@data-webdriver-automation-id="industry-dropdown"]').find_element_by_tag_name("select").send_keys("Prefer not to say")

        self.driver.find_element_by_xpath('//label[@for="chkNewsletter"]').click()
        self.driver.find_element_by_id('btnSignup').click()
        # need to click twice on that button. probably a bug
        self.driver.find_element_by_id('btnSignup').click()

        self.assertIn("Account identity", self.driver.page_source)

    def test_required_fields(self):
        self.driver.find_element_by_id('btnSignup').click()

        # first_name_input = self.driver.find_element_by_xpath('//input[@data-webdriver-automation-id="signup-first-name"]')
        # parent_fn = first_name_input.find_element_by_xpath("../..") #class="col-7"
        # err_msg = parent_fn.find_element_by_xpath("(//div[@class=\"has-error-msg\"])") #class="has-error-msg"
        # self.assertEqual(err_msg.text, "Please enter your first name")
        # parent2_fn = parent_fn.find_element_by_xpath("..") #class="form-group has-error"
        # self.assertEqual(parent2_fn.get_attribute("class"), "form-group has-error")

        self.checkInputElement("signup-first-name", "Please enter your first name")
        self.checkInputElement("signup-last-name", "Please enter your last name")
        self.checkInputElement("signup-email", "Please enter a valid email address")
        self.checkInputElement("signup-password", "Please enter a password")
        self.checkInputElement("signup-password2", "Please repeat the password")

        elem = self.driver.find_element_by_xpath('//div[@data-webdriver-automation-id="industry-dropdown"]')
        err_msg = elem.find_element_by_class_name("has-error-msg")
        self.assertEqual(err_msg.text, "Sorry, you have to choose a valid industry sector")



    def checkInputElement(self, wd_id, message):
        #find element
        elem = self.driver.find_element_by_xpath('//input[@data-webdriver-automation-id="' + wd_id + '"]')
        #find 2nd parent element
        parent = elem.find_element_by_xpath("../..") #class="col-7"
        #find element containing the error message
        err_msg = parent.find_element_by_xpath("(div[@class=\"has-error-msg\"])") #class="has-error-msg"

        # check the error message exists
        self.assertEqual(err_msg.text, message)

        #find 3rd parent element
        parent2 = parent.find_element_by_xpath("..") #class="form-group has-error"

        #check elements container has class
        self.assertEqual(parent2.get_attribute("class"), "form-group has-error")


    





