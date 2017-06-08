from selenium import webdriver


class BasePage(object):
    browser = webdriver.Firefox()
    browser.implicitly_wait(10)
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