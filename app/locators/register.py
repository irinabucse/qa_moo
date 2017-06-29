from selenium.webdriver.common.by import By
from app.locators.base import BasePageLocators


class RegisterPageLocators(BasePageLocators):
    EMAIL_FIELD = (By.XPATH, '//input[@data-webdriver-automation-id="signin-email"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@data-webdriver-automation-id="signin-password"]')
    SUBMIT_BTN = (By.XPATH, '//button[@data-webdriver-automation-id="signin-button"]')
