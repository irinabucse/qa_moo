from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    EMAIL_FIELD = (By.XPATH, '//input[@data-webdriver-automation-id="signin-email"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@data-webdriver-automation-id="signin-password"]')
    SUBMIT_BTN = (By.XPATH, '//button[@data-webdriver-automation-id="signin-button"]')
