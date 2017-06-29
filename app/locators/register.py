from selenium.webdriver.common.by import By
from app.locators.base import BasePageLocators


class RegisterPageLocators(BasePageLocators):
    FIRSTNAME_FIELD     = (By.XPATH, '//input[@data-webdriver-automation-id="signup-first-name"]')
    LASTNAME_FIELD      = (By.XPATH, '//input[@data-webdriver-automation-id="signup-last-name"]')
    EMAIL_FIELD         = (By.XPATH, '//input[@data-webdriver-automation-id="signup-email"]')
    PASSWORD_FIELD      = (By.XPATH, '//input[@data-webdriver-automation-id="signup-password"]')
    PASSWORD_CONFIRM_FIELD = (By.XPATH, '//input[@data-webdriver-automation-id="signup-password2"]')
    COUNTRY_SELECT      = (By.ID, 'ddlCountry')
    INDUSTRY_SELECT     = (By.ID, 'ddlIdentityIndustry')
    PROFESSION_SELECT   = (By.ID, 'ddlIdentityProfession2')
    COMPANY_SIZE_SELECT = (By.ID, 'ddlIdentityCompanySize')
    NEWSLETTER_CKB      = (By.XPATH, '//label[@for="chkNewsletter"]')
    SUBMIT_BTN          = (By.ID, 'btnSignup')
