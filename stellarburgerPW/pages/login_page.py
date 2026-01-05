from stellarburgerPW.pages.basepage import BasePage
from playwright.sync_api import Page
from stellarburgerPW.locators.login_locators import LoginLocators as LL


class LoginPage(BasePage):
    def __init__(self, page:Page, base_url):
        super().__init__(page, base_url)

class LoginPage(BasePage):
    def fill_login_fields(self, auth_api):
        self.page.locator(LL.EMAIL_FIELD).fill(auth_api["email"])
        self.page.locator(LL.PASSWORD_FIELD).fill(auth_api["password"])



