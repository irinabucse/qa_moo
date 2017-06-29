from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from app.locators.login import LoginPageLocators


class BasePage(object):
    browser = webdriver.Remote(
           command_executor='http://192.168.0.10:4444/wd/hub',
           desired_capabilities=DesiredCapabilities.CHROME)
    base_url = 'https://www.moo.com/uk'

    def get_browser(self):
        return self.browser

    def close(self):
        """
        close the webdriver instance
        """
        self.browser.quit()

    def visit(self, location=''):
        """
        navigate webdriver to different pages
        """
        url = self.base_url + location
        self.browser.get(url)

    def find_element(self, selector, value):
        return self.browser.find_element(selector, value)

    def get_source(self):
        return self.browser.page_source

    def get_error(self, selector, value):
        el = self.find_parent(selector, value)
        return el.find_element_by_class_name("has-error-msg").text

    def find_parent(self, selector, value):
        # return elem with class "col-7"
        return self.find_element(selector, value).find_element(*LoginPageLocators.PARENT)

    def logout(self):
        self.visit(self.LOGOUT_URL)
